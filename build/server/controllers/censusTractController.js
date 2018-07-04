'use strict';

var _regenerator = require('babel-runtime/regenerator');

var _regenerator2 = _interopRequireDefault(_regenerator);

var _asyncToGenerator2 = require('babel-runtime/helpers/asyncToGenerator');

var _asyncToGenerator3 = _interopRequireDefault(_asyncToGenerator2);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var _require = require(__dirname + '/../models/sequelize.js'),
    db = _require.db;

var constructCensusTractJson = function constructCensusTractJson(data) {
  return {
    features: data.filter(function (row) {
      return row.total_buildings > 55;
    }).map(function (row) {
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
          raceWhitePercent2016: (row.racial_makeup || {}).percent_white_2016 * 100,
          raceWhitePercentChange20112016: ((row.racial_makeup || {}).percent_white_2016 - (row.racial_makeup || {}).percent_white_2011) * 100,
          totalBuildings: row.total_buildings,
          totalViolations: row.total_violations,
          totalSales: row.total_sales,
          totalPermits: row.total_permits,
          totalServiceCalls: row.total_service_calls,
          percentServiceCallsWithViolation: (row.total_service_calls_with_violation_result / row.total_service_calls * 100).toFixed(2),
          percentServiceCallsNoAction: (row.total_service_calls_with_no_action_result / row.total_service_calls * 100).toFixed(2),
          percentServiceCallsUnresolved: (row.total_service_calls_unresolved_result / row.total_service_calls * 100).toFixed(2),
          totalSalesPriorViolations: row.total_sales_prior_violations,
          avgSalesPriorViolations: (row.total_sales_prior_violations / row.total_sales * 100).toFixed(2),
          avgViolationCount3YearsBeforeSale: row.avg_violation_count_3years_before_sale,
          violationsPerBuilding: (row.total_violations / row.total_buildings).toFixed(2),
          violationsNonCommunityPerBuilding: ((row.total_violations - row.total_service_calls_with_violation_result) / row.total_buildings).toFixed(2)
        }
      };
    })
  };
};

module.exports = {
  index: function () {
    var _ref = (0, _asyncToGenerator3.default)( /*#__PURE__*/_regenerator2.default.mark(function _callee(req, res) {
      return _regenerator2.default.wrap(function _callee$(_context) {
        while (1) {
          switch (_context.prev = _context.next) {
            case 0:
              db.CensusTract.findAll({
                include: [{
                  model: db.Neighborhood
                }, {
                  model: db.Income
                }, {
                  model: db.Rent
                }, {
                  model: db.RacialMakeup
                }]
              }).then(function (data) {
                var json = constructCensusTractJson(data);
                // console.log(json)
                res.json(json);
              });

            case 1:
            case 'end':
              return _context.stop();
          }
        }
      }, _callee, undefined);
    }));

    function index(_x, _x2) {
      return _ref.apply(this, arguments);
    }

    return index;
  }()
};