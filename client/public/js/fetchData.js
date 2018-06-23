import axios from 'axios'
import Promise from 'bluebird'

import Store from './store'

export const fetchData = () => {
  return new Promise((resolve, reject) => {
    axios
      .get('/boundaries/geojson/bk_census_tracts_2010')
      .then(response => {
        Store.boundaryData.censusTracts = response.data
        axios
          .get('/neighborhoods')
          .then(response => {
            Store.boundaryData.neighborhoods = response.data
            axios
              .get('/violations/processed_bk_violation_data_2011_2017')
              .then(response => {
                Store.geoJson.violationData = response.data
                axios
                  .get('/buildings/bk_new_buildings')
                  .then(response => {
                    Store.geoJson.newBuildings = response.data
                    resolve()
                  })
                  .catch(error => {
                    reject(error)
                  })
              })
              .catch(error => {
                reject(error)
              })
          })
          .catch(error => {
            reject(error)
          })
      })
      .catch(error => {
        reject(error)
      })
  })
}
