const express = require('express')
const router = express.Router()
const NeighborhoodController = require('../controllers/NeighborhoodController')

router.get('/', NeighborhoodController.index)
module.exports = router