const Sequelize = require('sequelize')

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
    }
  },
  {
    timestamps: false
  }
)

console.log('hi')
CensusTract.findAll().then(data => {
  console.log(data[0])
})

module.exports = {
  CensusTract: CensusTract
}
