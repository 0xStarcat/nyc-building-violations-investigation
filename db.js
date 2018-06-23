var sqlite3 = require('sqlite3').verbose()
var db = new sqlite3.Database('bk_building_violation_project.sqlite')

const { convert_rows_to_geojson } = require('./db/helpers')

module.exports = {
  get_neighborhoods: async (req, res) => {
    await db.all('SELECT * FROM neighborhoods_table', (err, rows) => {
      res.send(convert_rows_to_geojson(rows))
    })
  }
}
