var express = require('express');
var app = express();
var fs = require('fs');
const bodyParser = require('body-parser');
var http = require('http');

app.use(bodyParser.json());
app.set('view engine', 'ejs');


// This responds with "Hello World" on the homepage
app.get('/', function (req, res) {
   res.render('pages/index');
});

app.get('/about', function (req, res) {
    res.render('pages/about');
});

app.get('/licences', function (req, res) {
    res.render('pages/licences');
});

function addToData(tmp, res){
    const filePath = './Scores/data.json';
    console.log(tmp.high_score);
    try {
        let object = {'player_name':tmp.player_name, 'timestamp': Date.now(), 'high_score':tmp.high_score};

        // fs.appendFileSync(filePath, JSON.stringify(object));
        fs.readFile(filePath, (err, data) => {
            if (err) {
                console.error(err);
                res.sendStatus(500);
                return;
            }
            let json_data = JSON.parse(data);
            json_data.push(object);
            console.log(json_data);

            fs.writeFile(filePath, JSON.stringify(json_data), (err) => {
                if (err){
                    console.log("writefile error");
                    return;
                }
            });
        });
        //     const parsedData = JSON.load(data);
        //     parsedData.append(object);

        //     fs.writeFile(filePath, JSON.stringify(parsedData), (err) => {
        //         if (err){
        //             console.log(err);
        //             res.sendStatus(500);
        //             return;
        //         }
        //         res.sendStatus(200);
        //     });

        //     res.send(JSON.stringify(parsedData));
        // });
        res.sendStatus(200);
    } catch (error) {
        console.log("Error: " + error);
        res.sendStatus(500);
    }
}

// This responds a POST request for the homepage
app.post('/addRecord', function (req, res) {
    const filePath = './Scores/data.json';
    let jsonData = require(filePath);
    console.log(jsonData);
    addToData(req.body, res);
    console.log("Got a POST request for the homepage");
    //res.send(jsonData);
})

var server = app.listen(8081, function () {
   var host = server.address().address
   var port = server.address().port
   
   console.log("Example app listening at http://%s:%s", host, port)
})