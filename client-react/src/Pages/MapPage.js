import React from 'react'
import LeafletMap from '../LeafletMap'
import SideBar from '../SideBar'

const MapPage = props => {
  return (
    <div>
      <SideBar />
      <LeafletMap position={{ lat: 40.6881, lng: -73.9671 }} zoom={13} store={props.store} />
    </div>
  )
}

export default MapPage
