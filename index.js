const express = require('express')
const bp = require('body-parser')
const py = require('python-shell')
const selenium = new py('python_scripts/selenium_script.py');
const pug = require('pug')
const fs = require('fs')
const path = require('path')
//const prompt = require('prompt');
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
    // var username;
    // var password;
    // prompt('Whats your name?', function (input) {
    //     console.log(input);
    //     process.exit();
    // });


    // prompt.start();
    // prompt.get(['username', 'email'], function (err, result) {
    //     username = result.username;
    //     password = result.password;
    // });
    // console.log(username);


    // if (person == null || person == "") {
    //     res.status(404).send('No name sent. It\'s ok, you don\'t have to trust us.')
    // } else {
    //     var shell = new py('script.py', { mode: 'text '});
    //     shell.send('hello world!');
    // }

    // console.log("Calling selenium")
    // selenium.on('message', function (message) {
    //   // received a message sent from the Python script (a simple "print" statement)
    //   console.log(message);



    // py.run('python_scripts/selenium_script.py', function (err) {
    //   if (err) {
    //         console.log(err)
    //         res.status(404).send('Watch out for this Bad Request!')
    //         console.log("End of error, fool")
    //   }
    //   py.end(jsonLoad);
    // })
}

function prompt(question, callback) {
    var stdin = process.stdin,
        stdout = process.stdout;

    stdin.resume();
    stdout.write(question);

    stdin.once('data', function (data) {
        callback(data.toString().trim());
    });
}
