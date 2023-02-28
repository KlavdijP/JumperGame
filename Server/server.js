var express = require('express');
var app = express();
var fs = require('fs');
const bodyParser = require('body-parser');

app.use(bodyParser.json());

// This responds with "Hello World" on the homepage
app.get('/', function (req, res) {
   console.log("Got a GET request for the homepage");
   res.send('Hello GET');
})

function addToData(tmp){
    const filePath = './Scores/data.json';
    try {
        let object = {"player_name":tmp.player_name, "timestamp": tmp.timestamp, "high_score":tmp.high_score}
        const existingData = JSON.parse()
        fs.writeFile(filePath, JSON.stringify(object), (err) => {
            console.log(error);
        });
        console.log("NEW RECORD ADDED");
    } catch (error) {
        console.log(error);
    }
}

// This responds a POST request for the homepage
app.post('/addRecord', function (req, res) {
    const filePath = './Scores/data.json';
    let jsonData = require(filePath);
    console.log(jsonData.scores);
    console.log(req.body);
    addToData(req.body);
    console.log("Got a POST request for the homepage");
    //res.send(jsonData);
})

var server = app.listen(8081, function () {
   var host = server.address().address
   var port = server.address().port
   
   console.log("Example app listening at http://%s:%s", host, port)
})