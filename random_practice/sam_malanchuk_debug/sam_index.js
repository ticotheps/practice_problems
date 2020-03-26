var express = require('express')

var app = express()

app.use(express.json())
app.use(express.urlencoded({ extended: true }))

app.get('/', function(req, res, next) {
    console.log(req.body);
    res.send('SAM MALANCHUK HOME PAGE');
})

app.post('/send', function(req, res, next) {
    console.log(req.body);
    res.json(req.body)
})

app.listen(4000, () => console.log("Running on port 4000"))