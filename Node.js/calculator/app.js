const express = require("express");
const { calculator } = require("./calculator");
const PORT = 3000;
const app = express();
app.set('view engine', 'ejs');

app.use(express.json());


const urlencodedParser = express.urlencoded({ extended: false });

app.get('/', function (request, response) {
    console.log(request.method, "has come to server from /");
    response.render('calculator');
});

app.post('/', urlencodedParser, function (req, res) {
    console.log(req.method, "has come to server from /");
    console.log(req.body.in_string);
    if (!req.body) return res.sendStatus(400);

    let result;
    try {
        result = calculator(req.body.in_string) ;
    }
    catch (err) {
        result = err.message;
    }
    let answer = { ans: result };
    return res.send(answer);
})

app.listen(PORT, function (err) {
    if (err) console.log(err);
    else console.log("Server listening on Port", PORT);
});