import React, { Component } from 'react'
import PropTypes from 'prop-types'
import LayersMenu from './LayersMenu'

import { Map, TileLayer, LayerGroup, GeoJSON, Circle } from 'react-leaflet'

import './index.scss'

export default class LeafletMap extends Component {
  constructor(props) {
    super()
    this.state = {
      lat: props.position.lat,
      lng: props.position.lng,
      zoom: props.zoom
    }

    this.mapRef = React.createRef()
    this.neighborhoodLayerGroupRef = React.createRef()
    this.neighborhoodOverlayRef = React.createRef()
    this.bringNeighborhoodsToFront = this.bringNeighborhoodsToFront.bind(this)
    this.onBaseLayerChange = this.onBaseLayerChange.bind(this)
  }

  bringNeighborhoodsToFront() {
    this.neighborhoodLayerGroupRef.current.leafletElement.eachLayer(layer => {
      if (layer._map) layer.bringToFront()
    })
  }

  onBaseLayerChange(event) {
    if (this.neighborhoodOverlayRef.current.props.checked) this.bringNeighborhoodsToFront()
  }

  render() {
    const position = [this.state.lat, this.state.lng]
    return (
      <Map
        ref={this.mapRef}
        id="leaflet-map"
        center={position}
        zoom={this.state.zoom}
        onBaseLayerChange={this.onBaseLayerChange}
      >
        <TileLayer
          attribution="&amp;copy <a href=&quot;http://osm.org/copyright&quot;>OpenStreetMap</a> contributors"
          url="https://api.tiles.mapbox.com/v4/mapbox.wheatpaste/{z}/{x}/{y}.png?access_token=pk.eyJ1Ijoic3RhcmNhdCIsImEiOiJjamlpYmlsc28wbjlmM3FwbXdwaXozcWEzIn0.kLmWiUbmdqNLA1atmnTXXA"
        />
        <LayersMenu
          neighborhoodOverlayRef={this.neighborhoodOverlayRef}
          neighborhoodLayerGroupRef={this.neighborhoodLayerGroupRef}
          store={this.props.store}
          position="topright"
        />
      </Map>
    )
  }
}

LeafletMap.propTypes = {
  position: PropTypes.shape({
    lat: PropTypes.number,
    lng: PropTypes.number
  }),
  zoom: PropTypes.number
}
