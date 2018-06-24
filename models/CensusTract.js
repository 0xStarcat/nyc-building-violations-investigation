const Sequelize = require('sequelize')
const { Neighborhood } = require('./Neighborhood.js')
const { seq } = require('./sequelize.js')

const CensusTract = seq.define(
  'census_tract',
  {
    name: {
      type: Sequelize.STRING,
      field: 'name'
    },
    geometry: {
      type: Sequelize.JSON,
      field: 'geometry'
    },
    neighborhood_id: {
      type: Sequelize.INTEGER,
      field: 'neighborhood_id'
    }
  },
  {
    timestamps: false
  }
)

// CensusTract.belongsTo(Neighborhood, { foreignKey: 'neighborhood_id', targetKey: 'id' })

module.exports = {
  CensusTract: CensusTract
}
