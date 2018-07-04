'use strict';

var express = require('express');
var router = express.Router();
var NeighborhoodController = require('../controllers/NeighborhoodController');

router.get('/', NeighborhoodController.index);
module.exports = router;