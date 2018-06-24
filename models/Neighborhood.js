const Sequelize = require('sequelize')

const { seq } = require('./sequelize.js')
const { CensusTract } = require('./CensusTract.js')

const Neighborhood = seq.define(
  'neighborhood',
  {
    name: {
      type: Sequelize.STRING,
      field: 'name'
    },
    geometry: {
      type: Sequelize.JSON,
      field: 'geometry'
    }
  },
  {
    timestamps: false
  }
)

Neighborhood.hasMany(CensusTract, { foreignKey: 'neighborhood_id' })

// Neighborhood.findOne({
//   include: [
//     {
//       model: CensusTract
//     }
//   ]
// }).then(data => {
//   return data
// })

module.exports = {
  Neighborhood: Neighborhood
}
