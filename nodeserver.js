const express = require('express');
var mysql = require('mysql');
var cors = require('cors');
const https = require('https');

const mySqlAuth = {
    host: "localhost",
    user: "root",
    password: "1234",
    database: "pokemonDB"
};

const mySqlConnection = mysql.createConnection(mySqlAuth);
mySqlConnection.connect(
    function(err)
    {
        if(err)
        {
            throw err;
        }
        console.log("yay we connected");
    }
);

const app = express(),
    bodyParser = require("body-parser"),
    port = 3080;

app.use(bodyParser.urlencoded({extended:true}));
app.use(cors());
//app.get('/evs/(hpyield|attackyield|defenseyield|spattackyield|spdefenseyield|speedyield)', (req,res) => {
//    console.log(req.params);
//    const splitPath = req.path.split('/');
//    const chosenYield = splitPath[splitPath.length - 1];
//    mySqlConnection.query(
//        'SELECT * FROM Pokemon WHERE ' + chosenYield + ' > 0;',
//        function(err, result)
//        {
//            if(err)
//            {}
//            else
//            {
//                console.log(result);
//                res.send(result);
//            }
//        }
//    );
//});

//app.get('/evs/types?hpyield=:hpbool&attackyield&=:attackbool&defenseyield=:defensebool&spattackyield=:spattackbool&spdefenseyield=:spdefensebool&speedyield=:speedbool', (req,res) => {
app.get('/evs/types?', (req,res) => {
    console.log(req.query);
    var sqlString = "SELECT * FROM Pokemon WHERE ";
    var paramCount = 0;
    queryEntries = Object.entries(req.query);
    for (const [key,value] of queryEntries)
    {
        if (paramCount > 0)
        {
            sqlString+=' AND ';
        }
        sqlString+=key+' > 0';
        paramCount+=1;
    }
    sqlString+=';'
    console.log(sqlString);
    mySqlConnection.query(
        sqlString,
        function(err, result)
        {
            if(err)
            {
                res.send(err);
            }
            else
            {
                console.log(result);
                res.send(result);
            }
        }
    ); 
});

function listenFunction()
{
    console.log("hehe we just listen");
}

app.listen(port, listenFunction);
