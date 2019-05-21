var express = require('express');
var router = express.Router();
var mysql = require('mysql');

var con = mysql.createConnection({
    host: "localhost",
    user: "boss",
    password: "123456",
    database: "mangcambien2019"
})
con.connect();
/* GET users listing. */
router.get('/', function(req, res) {
  res.send('respond with a resource');
});
router.get('/sensor2', function(req, res){
    con.query("SELECT * FROM sensor2 where id = (select max(id) from sensor2)", function (err, result, fields) {
    if (err) throw err;
        var a = result[0];
        res.json(a);                
    });
});
router.post('/led1', function(req, res){
  con.query(`INSERT INTO led1(led1) VALUES(${req.body.signal})`, function (err, result, fields) {
      if (err) throw err;
      res.json(result[0]);
  });
});
router.post('/controlled1', function(req, res){
  con.query(`INSERT INTO controlled1(led1) VALUES(${req.body.pwm})`, function (err, result, fields) {
      if (err) throw err;
      res.json({
        message: "success",
        data: result[0]
      });
  });
});
module.exports = router;
