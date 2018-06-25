module.exports = function(sequelize, DataTypes) {
  return sequelize.define(
    'neighborhood',
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
      }
    },
    {
      tableName: 'neighborhoods',
      timestamps: false,
      classMethods: {}
    }
  )
}
