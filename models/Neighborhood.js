const Sequelize = require('sequelize')

const { seq } = require('./sequelize.js')

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

module.exports = {
  Neighborhood: Neighborhood
}
