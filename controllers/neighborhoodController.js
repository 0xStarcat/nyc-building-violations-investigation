const { Neighborhood } = require('../models/Neighborhood.js')

const { convert_rows_to_geojson } = require('../db/helpers')

module.exports = {
  index: async (req, res) => {
    Neighborhood.findAll().then(data => {
      res.json(convert_rows_to_geojson(data))
    })
  }
}
