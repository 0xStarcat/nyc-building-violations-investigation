import React, { Component } from 'react'
import {
  Circle,
  FeatureGroup,
  LayerGroup,
  LayersControl,
  Marker,
  Popup,
  Rectangle,
  GeoJSON,
  TileLayer
} from 'react-leaflet'
const { BaseLayer, Overlay } = LayersControl

export default class LayersMenu extends Component {
  constructor(props) {
    super(props)
  }
  render() {
    const center = [51.505, -0.09]
    const rectangle = [[51.49, -0.08], [51.5, -0.06]]

    return (
      <LayersControl position={this.props.position}>
        <BaseLayer checked name="Census Tracts">
          <LayerGroup>
            {this.props.store.censusTracts.features.map((feature, index) => {
              return (
                <GeoJSON
                  key={`ct-${index}`}
                  color="white"
                  opacity={1}
                  weight={1}
                  fillOpacity={0.7}
                  fillColor="pink"
                  data={feature['geometry']}
                />
              )
            })}
          </LayerGroup>
        </BaseLayer>
        <BaseLayer name="Census Tracts 2011">
          <LayerGroup>
            {this.props.store.censusTracts.features.map((feature, index) => {
              return (
                <GeoJSON
                  key={`ct-${index}`}
                  color="white"
                  opacity={1}
                  weight={1}
                  fillOpacity={0.7}
                  fillColor="pink"
                  data={feature['geometry']}
                />
              )
            })}
          </LayerGroup>
        </BaseLayer>
        <Overlay name="Marker with popup">
          <Marker position={center}>
            <Popup>
              <span>
                A pretty CSS3 popup. <br /> Easily customizable.
              </span>
            </Popup>
          </Marker>
        </Overlay>
        <Overlay checked name="Layer group with circles">
          <LayerGroup>
            <Circle center={center} fillColor="blue" radius={200} />
            <Circle center={center} fillColor="red" radius={100} stroke={false} />
            <LayerGroup>
              <Circle center={[51.51, -0.08]} color="green" fillColor="green" radius={100} />
            </LayerGroup>
          </LayerGroup>
        </Overlay>
        <Overlay name="Feature group">
          <FeatureGroup color="purple">
            <Popup>
              <span>Popup in FeatureGroup</span>
            </Popup>
            <Circle center={[51.51, -0.06]} radius={200} />
            <Rectangle bounds={rectangle} />
          </FeatureGroup>
        </Overlay>
      </LayersControl>
    )
  }
}
