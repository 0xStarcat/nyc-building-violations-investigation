const { db } = require('../models/sequelize.js')

const constructCensusTractJson = data => {
  return {
    features: data.map(row => {
      return {
        type: 'Feature',
        geometry: JSON.parse(row['geometry']),
        properties: {
          name: row['name'],
          neighborhood: row.neighborhood.name,
          medianIncome2011: (row.income || {}).median_income_2011,
          medianIncome2017: (row.income || {}).median_income_2017,
          medianIncomeChange20112017: (row.income || {}).median_income_change_2011_2017,
          medianRent2011: (row.rent || {}).median_rent_2011,
          medianRent2017: (row.rent || {}).median_rent_2017,
          medianRentChange20112017: (row.rent || {}).median_rent_change_2011_2017,
          totalBuildings: row.total_buildings,
          totalViolations: row.total_violations,
          totalSales: row.total_sales,
          totalPermits: row.total_permits,
          totalServiceCalls: row.total_service_calls,
          percentServiceCallsWithViolation: (
            (row.total_service_calls_with_violation_result / row.total_service_calls) *
            100
          ).toFixed(2),
          totalSalesPriorViolations: row.total_sales_prior_violations,
          avgSalesPriorViolations: ((row.total_sales_prior_violations / row.total_sales) * 100).toFixed(2),
          avgViolationCount3YearsBeforeSale: row.avg_violation_count_3years_before_sale,
          violationsPerBuilding: (row.total_violations / row.total_buildings).toFixed(2)
        }
      }
    })
  }
}

module.exports = {
  index: async (req, res) => {
    db.CensusTract.findAll({
      include: [
        {
          model: db.Neighborhood
        },
        {
          model: db.Income
        },
        {
          model: db.Rent
        }
      ]
    }).then(data => {
      const json = constructCensusTractJson(data)
      // console.log(json)
      res.json(json)
    })
  }
}
