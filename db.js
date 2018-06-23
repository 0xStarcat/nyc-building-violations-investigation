const { Neighborhood } = require('./models/Neighborhood.js')

const { convert_rows_to_geojson } = require('./db/helpers')

module.exports = {
  get_neighborhoods: async (req, res) => {
    Neighborhood.findAll().then(data => {
      res.json(convert_rows_to_geojson(data))
    })
  }
}
