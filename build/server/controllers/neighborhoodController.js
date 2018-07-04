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
    features: data.map(function (row) {
      return {
        type: 'Feature',
        geometry: JSON.parse(row['geometry']),
        properties: {
          name: row['name']
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
              db.Neighborhood.findAll().then(function (data) {
                res.json(constructCensusTractJson(data));
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