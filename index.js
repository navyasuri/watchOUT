const express = require('express')
const bp = require('body-parser')
const pug = require('pug');
const fs = require('fs')
const path = require('path')
const PORT = process.env.PORT || 5000
const cors = require('cors')
let file = ''

express()
    .use(express.static(path.join(__dirname, 'public')))
    .use(cors())
    .use(bp.json())
    .use(bp.urlencoded({extended: true}))
    .set('views', path.join(__dirname, 'views'))
    .set('view engine', 'pug')

    //.get('/api/*', (req, res) => res.send("Woo!"))
    .get('/', jsonLoad)

    .listen(PORT, () => console.log(`Listening on ${ PORT }`))

// Pull JSON, serve to client:
function jsonLoad(req, res) {
    let data
    //cutPath(req.url)
<<<<<<< HEAD
    fs.readFile("public/data/announcements.json", (err, inData) => {
=======
    fs.readFile('public/data/announcements.json', (err, inData) => {
>>>>>>> 8aca4d933ed0cf06d57ba56b5cc133c232321d53
        // TODO: Edit to avoid hard server crashes:
        if (err) {
            res.status(404).send('Watch out for this Bad Request!')
        }
        data = JSON.parse(inData)
        let pugPath = path.join(__dirname, 'public/views/announcements.pug')
        res.render(pugPath, {"data": data})
    })
}

function cutPath(url) {
    let urlSections = url.split('/');
    let wantedSection = urlSections[urlSections.length - 1];
    file = wantedSection;
}
