'use strict';

module.exports = function (sequelize, DataTypes) {
  return sequelize.define('income', {
    id: {
      type: DataTypes.INTEGER,
      field: 'id',
      primaryKey: true
    },
    census_tract_id: {
      type: DataTypes.INTEGER,
      field: 'census_tract_id'
    },
    median_income_2011: {
      type: DataTypes.FLOAT,
      field: 'median_income_2011'
    },
    median_income_2017: {
      type: DataTypes.FLOAT,
      field: 'median_income_2017'
    },
    median_income_change_2011_2017: {
      type: DataTypes.FLOAT,
      field: 'median_income_change_2011_2017'
    }
  }, {
    tableName: 'incomes'
  });
};