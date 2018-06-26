const { db } = require('../models/sequelize.js')

const constructCensusTractJson = data => {
  return {
    features: data.map(row => {
      return {
        type: 'Feature',
        geometry: JSON.parse(row['geometry']),
        properties: {
          name: row['name']
        }
      }
    })
  }
}

module.exports = {
  index: async (req, res) => {
    db.Neighborhood.findAll().then(data => {
      res.json(constructCensusTractJson(data))
    })
  }
}
