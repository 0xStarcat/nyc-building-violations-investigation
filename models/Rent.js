module.exports = function(sequelize, DataTypes) {
  return sequelize.define(
    'rent',
    {
      id: {
        type: DataTypes.INTEGER,
        field: 'id',
        primaryKey: true
      },
      census_tract_id: {
        type: DataTypes.INTEGER,
        field: 'census_tract_id'
      },
      median_rent_2011: {
        type: DataTypes.FLOAT,
        field: 'median_rent_2011'
      },
      median_rent_2017: {
        type: DataTypes.FLOAT,
        field: 'median_rent_2017'
      },
      median_rent_change_2011_2017: {
        type: DataTypes.FLOAT,
        field: 'median_rent_change_2011_2017'
      }
    },
    {
      tableName: 'rents'
    }
  )
}
