const Sequelize = require('sequelize')
const sequelize = new Sequelize('sqlite://bk_building_violation_project.sqlite', {
  pool: {
    max: 5,
    min: 0,
    acquire: 30000,
    idle: 10000
  },
  define: {
    timestamps: false
  },

  // http://docs.sequelizejs.com/manual/tutorial/querying.html#operators
  operatorsAliases: false
})

const db = {
  Sequelize: Sequelize,
  sequelize: sequelize
}

db.Neighborhood = sequelize.import('./Neighborhood.js')
db.CensusTract = sequelize.import('./CensusTract.js')
db.Building = sequelize.import('./Building.js')

db.Neighborhood.hasMany(db.CensusTract, { foreignKey: 'neighborhood_id', sourceKey: 'id' })
db.Neighborhood.hasMany(db.Building, { foreignKey: 'neighborhood_id', sourceKey: 'id' })

db.CensusTract.belongsTo(db.Neighborhood, { foreignKey: 'neighborhood_id', targetKey: 'id' })
db.CensusTract.hasMany(db.Building, { foreignKey: 'census_tract_id', sourceKey: 'id' })
db.CensusTract.hasMany(db.Income, { foreignKey: 'census_tract_id', sourceKey: 'id' })
db.CensusTract.hasMany(db.Rent, { foreignKey: 'census_tract_id', sourceKey: 'id' })

db.Building.belongsTo(db.Neighborhood, { foreignKey: 'neighborhood_id', targetKey: 'id' })
db.Building.belongsTo(db.CensusTract, { foreignKey: 'census_tract_id', targetKey: 'id' })
db.Building.hasMany(db.Sale, { foreignKey: 'building_id', sourceKey: 'id' })
db.Building.hasMany(db.Permit, { foreignKey: 'building_id', sourceKey: 'id' })
db.Building.hasMany(db.Violation, { foreignKey: 'building_id', sourceKey: 'id' })

db.Income.belongsTo(db.CensusTract, { foreignKey: 'census_tract_id', targetKey: 'id' })

db.Rent.belongsTo(db.CensusTract, { foreignKey: 'census_tract_id', targetKey: 'id' })

db.Sale.belongsTo(db.Building, { foreignKey: 'building_id', targetKey: 'id' })

db.Permit.belongsTo(db.Building, { foreignKey: 'building_id', targetKey: 'id' })

db.Violation.belongsTo(db.Building, { foreignKey: 'building_id', targetKey: 'id' })

module.exports = {
  db: db
}
