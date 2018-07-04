module.exports = function(sequelize, DataTypes) {
  return sequelize.define(
    'racial_makeup',
    {
      id: {
        type: DataTypes.INTEGER,
        field: 'id',
        primaryKey: true
      },
      sub_borough_name: {
        type: DataTypes.STRING,
        field: 'sub_borough_name'
      },
      percent_white_2011: {
        type: DataTypes.FLOAT,
        field: 'percent_white_2011'
      },
      percent_white_2016: {
        type: DataTypes.FLOAT,
        field: 'percent_white_2016'
      }
    },
    {
      tableName: 'racial_makeups'
    }
  )
}
