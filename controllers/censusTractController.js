const { db } = require('../models/sequelize.js')

const constructCensusTractJson = data => {
  return {
    features: data.map(row => {
      // console.log(row.rent)
      return {
        type: 'Feature',
        geometry: JSON.parse(row['geometry']),
        properties: {
          name: row['name'],
          neighborhood: row.neighborhood.name,
          medianIncome2011: (row.income || {}).median_income_2011,
          medianIncome2017: (row.income || {}).median_income_2017,
          medianIncomeChange20112017: (row.income || {}).median_income_change_2011_2017,
          medianRent2011: (row.rent || {}).median_rent_2011,
          medianRent2017: (row.rent || {}).median_rent_2017,
          medianRentChange20112017: (row.rent || {}).median_rent_change_2011_2017
        }
      }
    })
  }
}

module.exports = {
  index: async (req, res) => {
    db.CensusTract.findAll({
      include: [
        {
          model: db.Neighborhood
        },
        {
          model: db.Income
        },
        {
          model: db.Rent
        }
      ]
    }).then(data => {
      const json = constructCensusTractJson(data)
      // console.log(json)
      res.json(json)
    })
  }
}
