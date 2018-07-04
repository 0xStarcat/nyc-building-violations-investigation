'use strict';

var express = require('express');
var router = express.Router();
var CensusTractController = require('../controllers/CensusTractController');

router.get('/', CensusTractController.index);
module.exports = router;