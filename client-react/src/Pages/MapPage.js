import React from 'react'
import LeafletMap from '../LeafletMap'

const MapPage = props => {
  return <LeafletMap position={{ lat: 40.6881, lng: -73.9671 }} zoom={13} store={props.store} />
}

export default MapPage
