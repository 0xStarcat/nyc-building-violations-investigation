import { fetchData } from './fetchData'
import Store from './store'

/* eslint-disable */
var map = L.map('map').setView({ lat: 40.7081, lon: -73.9571 }, 13)

L.tileLayer('https://api.tiles.mapbox.com/v4/mapbox.wheatpaste/{z}/{x}/{y}.png?access_token=pk.eyJ1Ijoic3RhcmNhdCIsImEiOiJjamlpYmlsc28wbjlmM3FwbXdwaXozcWEzIn0.kLmWiUbmdqNLA1atmnTXXA', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox.wheatpaste',
    accessToken: 'pk.eyJ1Ijoic3RhcmNhdCIsImEiOiJjamlpYmlsc28wbjlmM3FwbXdwaXozcWEzIn0.kLmWiUbmdqNLA1atmnTXXA'
}).addTo(map);

setTimeout(() => map.invalidateSize(), 1)

fetchData()
  .then(() => {
    console.log(Store.boundaryData.neighborhoods)
    setupGeoJsonBoundaries()
  })
  .catch(error => {
    console.log("error ", error)
  })

const geojsonMarkerOptions = {
  radius: 1,
  fillColor: "hotpink",
  color: "#000",
  weight: 1,
  opacity: 1,
  fillOpacity: 0.8
};


const setupGeoJsonBoundaries = () => {
  L.geoJSON(Store.boundaryData.censusTracts, {
    onEachFeature: onNeighborhoodFeatureEach
  }).addTo(map)

  // L.geoJSON(violation_data, {
  //   pointToLayer: function (feature, latlng) {
  //         return L.circleMarker(latlng, geojsonMarkerOptions);
  //     },
  //   onEachFeature: onViolationEachFeature
  // }).addTo(map);
}

function onNeighborhoodFeatureEach(feature, layer) {
  layer.on({
    click: onNeighborhoodClick
  })
}

function onViolationEachFeature(feature, layer) {
  layer.on({
        click: onViolationClick
    });
}

function onNeighborhoodClick(e, layer) {
  L.popup()
    .setLatLng(e.latlng)
    .setContent(e.target.feature.properties.neighborhood)
    .openOn(map);
}

function onViolationClick(e) {
  console.log(e.target.feature.geometry.coordinates)
}