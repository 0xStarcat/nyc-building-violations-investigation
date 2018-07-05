const { db } = require(__dirname + '/../models/sequelize.js')

const constructCensusTractJson = data => {
  return {
    features: data.filter(row => row.total_buildings > 55).map(row => {
      return {
        type: 'Feature',
        geometry: JSON.parse(row['geometry']),
        properties: {
          name: row['name'],
          neighborhood: row.neighborhood.name,
          medianIncome2011: parseFloat((row.income || {}).median_income_2011),
          medianIncome2017: parseFloat((row.income || {}).median_income_2017),
          medianIncomeChange20112017: parseFloat((row.income || {}).median_income_change_2011_2017),
          medianRent2011: parseFloat((row.rent || {}).median_rent_2011),
          medianRent2017: parseFloat((row.rent || {}).median_rent_2017),
          medianRentChange20112017: parseFloat((row.rent || {}).median_rent_change_2011_2017),
          raceWhitePercent2016: parseFloat((row.racial_makeup || {}).percent_white_2016 * 100),
          raceWhitePercentChange20112016: parseFloat(
            ((row.racial_makeup || {}).percent_white_2016 - (row.racial_makeup || {}).percent_white_2011) * 100
          ),
          totalBuildings: parseFloat(row.total_buildings),
          totalViolations: parseFloat(row.total_violations),
          totalSales: parseFloat(row.total_sales),
          totalPermits: parseFloat(row.total_permits),
          totalServiceCalls: parseFloat(row.total_service_calls),
          percentServiceCallsWithViolation: parseFloat(
            ((row.total_service_calls_with_violation_result / row.total_service_calls) * 100).toFixed(2)
          ),
          percentServiceCallsNoAction: parseFloat(
            ((row.total_service_calls_with_no_action_result / row.total_service_calls) * 100).toFixed(2)
          ),
          percentServiceCallsUnresolved: parseFloat(
            ((row.total_service_calls_unresolved_result / row.total_service_calls) * 100).toFixed(2)
          ),
          totalSalesPriorViolations: parseFloat(row.total_sales_prior_violations),
          avgSalesPriorViolations: parseFloat(((row.total_sales_prior_violations / row.total_sales) * 100).toFixed(2)),
          avgViolationCount3YearsBeforeSale: parseFloat(row.avg_violation_count_3years_before_sale),
          violationsPerBuilding: parseFloat((row.total_violations / row.total_buildings).toFixed(2)),
          violationsNonCommunityPerBuilding: parseFloat(
            ((row.total_violations - row.total_service_calls_with_violation_result) / row.total_buildings).toFixed(2)
          )
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
        },
        {
          model: db.RacialMakeup
        }
      ]
    }).then(data => {
      const json = constructCensusTractJson(data)
      // console.log(json)
      res.json(json)
    })
  }
}
