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
      },
      total_buildings: {
        type: DataTypes.INTEGER,
        field: 'total_buildings'
      },
      total_violations: {
        type: DataTypes.INTEGER,
        field: 'total_violations'
      },
      total_sales: {
        type: DataTypes.INTEGER,
        field: 'total_sales'
      },
      total_permits: {
        type: DataTypes.INTEGER,
        field: 'total_permits'
      },
      total_sales_prior_violations: {
        type: DataTypes.INTEGER,
        field: 'total_sales_prior_violations'
      },
      avg_violation_count_3years_before_sale: {
        type: DataTypes.FLOAT,
        field: 'avg_violation_count_3years_before_sale'
      }
    },
    {
      tableName: 'census_tracts'
    }
  )
}
