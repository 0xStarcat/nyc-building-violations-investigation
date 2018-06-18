import axios from 'axios'
import Promise from 'bluebird'

import Store from './store'

export const fetchData = () => {
  return new Promise((resolve, reject) => {
    axios.get('/boundaries/census_tracts/manh_census_tracts_2010').then(response => {
      Store.boundaryData.censusTracts = response.data
      axios.get('/boundaries/neighborhoods/manh_neighborhoods').then(response => {
        Store.boundaryData.neighborhoods = response.data
        resolve()
      }).catch(error => {
        reject(error)
      })
    }).catch(error => {
      reject(error)
    })
  })
}