const Sequelize = require('sequelize')
const sequelize = new Sequelize('database', 'username', 'password', {
  host: 'localhost',
  dialect: 'sqlite',

  pool: {
    max: 5,
    min: 0,
    acquire: 30000,
    idle: 10000
  },
  define: {
    timestamps: false // true by default
  },

  // SQLite only
  storage: './bk_building_violation_project.sqlite',

  // http://docs.sequelizejs.com/manual/tutorial/querying.html#operators
  operatorsAliases: false
})

const db = {
  Sequelize: Sequelize,
  sequelize: sequelize
}

db.Neighborhood = sequelize.import('./Neighborhood.js')
db.CensusTract = sequelize.import('./CensusTract.js')

db.CensusTract.belongsTo(db.Neighborhood, { foreignKey: 'neighborhood_id', targetKey: 'id' })

module.exports = {
  seq: sequelize,
  db: db
}
