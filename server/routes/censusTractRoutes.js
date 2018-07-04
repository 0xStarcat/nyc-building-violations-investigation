const express = require('express')
const router = express.Router()
const CensusTractController = require('../controllers/CensusTractController')

router.get('/', CensusTractController.index)
module.exports = router
