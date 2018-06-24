const { CensusTract } = require('../models/CensusTract.js')

const { convert_rows_to_geojson } = require('../db/helpers')

module.exports = {
  index: async (req, res) => {
    CensusTract.findAll().then(data => {
      res.json(convert_rows_to_geojson(data))
    })
  }
}
