import Store from '../../../store.js'

export const styleRentLayers = feature => {
  if (!feature.properties.medianRent2017 || feature.properties.totalBuildings < Store.buildingThreshold) {
    return {
      color: 'white',
      fillColor: 'white',
      opacity: 1,
      fillOpacity: 0.7,
      weight: 1
    }
  } else if (feature.properties.medianRent2017 >= 2000) {
    return {
      color: 'white',
      fillColor: '#005a32',
      opacity: 0.5,
      fillOpacity: 0.7,
      weight: 1
    }
  } else if (feature.properties.medianRent2017 >= 1800) {
    return {
      color: 'white',
      fillColor: '#238b45',
      opacity: 0.5,
      fillOpacity: 0.7,
      weight: 1
    }
  } else if (feature.properties.medianRent2017 >= 1600) {
    return {
      color: 'white',
      fillColor: '#41ab5d',
      opacity: 1,
      fillOpacity: 0.7,
      weight: 1
    }
  } else if (feature.properties.medianRent2017 >= 1400) {
    return {
      color: 'white',
      fillColor: '#74c476',
      opacity: 1,
      fillOpacity: 0.7,
      weight: 1
    }
  } else if (feature.properties.medianRent2017 >= 1200) {
    return {
      color: 'white',
      fillColor: '#a1d99b',
      opacity: 1,
      fillOpacity: 0.7,
      weight: 1
    }
  } else if (feature.properties.medianRent2017 >= 1000) {
    return {
      color: 'white',
      fillColor: '#c7e9c0',
      opacity: 1,
      fillOpacity: 0.7,
      weight: 1
    }
  } else {
    return {
      color: 'white',
      fillColor: '#edf8e9',
      opacity: 1,
      fillOpacity: 0.7,
      weight: 1
    }
  }
}
