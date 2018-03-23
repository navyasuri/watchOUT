const express = require('express')
const bp = require('body-parser')
const py = require('python-shell')
const pug = require('pug')
const fs = require('fs')
const path = require('path')
const PORT = process.env.PORT || 5000
const cors = require('cors')
let file = ''

express()
    .use(express.static(path.join(__dirname, 'public')))
    .use(cors())
    //.use(py())
    .use(bp.json())
    .use(bp.urlencoded({extended: true}))
    .set('views', path.join(__dirname, 'views'))
    .set('view engine', 'pug')

    //.get('/api/*', (req, res) => res.send("Woo!"))
    .get('/', jsonLoad)
    .get('/python', scrape)

    .listen(PORT, () => console.log(`Listening on ${ PORT }`))

// Pull JSON, serve to client:
function jsonLoad(req, res) {
    let data
    fs.readFile('events.json', (err, inData) => {
        // TODO: Edit to avoid hard server crashes:
        if (err) {
            res.status(404).send('Watch out for this Bad Request!')
        }
        data = JSON.parse(inData)
        let pugPath = path.join(__dirname, 'public/views/events.pug')
        res.render(pugPath, {"data": data})
    })
}

// Run python to scrape OrgSync for events, save to data folder:
function scrape(req, res) {
    py.run('python_scripts/selenium_script.py', function (err) {
      if (err) {
            console.log(err)
            res.status(404).send('Watch out for this Bad Request!')
            console.log("End of error, fool")
      }
      console.log('Python ran!');
    })
}
