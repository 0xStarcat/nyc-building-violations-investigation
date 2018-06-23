const convert_rows_to_geojson = rows => {
  return {
    features: rows.map(row => {
      return {
        type: 'Feature',
        geometry: JSON.parse(row['geometry']),
        properties: {
          name: row['name']
        }
      }
    })
  }
}

module.exports = {
  convert_rows_to_geojson: convert_rows_to_geojson
}
