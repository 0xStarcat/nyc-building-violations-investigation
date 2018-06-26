module.exports = function(sequelize, DataTypes) {
  return sequelize.define(
    'census_tract',
    {
      id: {
        type: DataTypes.INTEGER,
        field: 'id',
        primaryKey: true
      },
      name: {
        type: DataTypes.STRING,
        field: 'name'
      },
      geometry: {
        type: DataTypes.JSON,
        field: 'geometry'
      },
      neighborhood_id: {
        type: DataTypes.INTEGER,
        field: 'neighborhood_id'
      }
    },
    {
      tableName: 'census_tracts',
      timestamps: false,
      classMethods: {}
    }
  )
}
