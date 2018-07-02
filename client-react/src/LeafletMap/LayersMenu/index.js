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

import {
  incomeMedianLayerStyle,
  incomeChangeLayerStyle,
  rentMedianLayerStyle,
  rentChangeLayerStyle,
  violationsPerBuildingLayerStyle,
  serviceCallsTotalLayerStyle,
  serviceCallsPercentViolationLayerStyle,
  salesTotalLayerStyle,
  salesWithViolationTotalLayerStyle,
  salesWithViolationPercentLayerStyle,
  violationsCountBeforeSaleLayerStyle,
  permitsTotalLayerStyle
} from '../GeoJsonStyles'

import CensusTractPopup from '../Popups/CensusTractPopup'
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
        <BaseLayer checked name="Median Income, 2017">
          <LayerGroup>
            {this.props.store.censusTracts.features.map((feature, index) => {
              return (
                <GeoJSON
                  key={`ct-${index}`}
                  data={feature['geometry']}
                  {...incomeMedianLayerStyle(feature.properties.medianIncome2017, feature.properties.totalBuildings)}
                >
                  <CensusTractPopup feature={feature} />
                </GeoJSON>
              )
            })}
          </LayerGroup>
        </BaseLayer>
        <BaseLayer name="Income Change, 2011 - 2017">
          <LayerGroup>
            {this.props.store.censusTracts.features.map((feature, index) => {
              return (
                <GeoJSON
                  key={`ct-${index}`}
                  data={feature['geometry']}
                  {...incomeChangeLayerStyle(
                    feature.properties.medianIncomeChange20112017,
                    feature.properties.totalBuildings
                  )}
                >
                  <CensusTractPopup feature={feature} />
                </GeoJSON>
              )
            })}
          </LayerGroup>
        </BaseLayer>
        <BaseLayer name="Median Rent, 2017">
          <LayerGroup>
            {this.props.store.censusTracts.features.map((feature, index) => {
              return (
                <GeoJSON
                  key={`ct-${index}`}
                  data={feature['geometry']}
                  {...rentMedianLayerStyle(feature.properties.medianRent2017, feature.properties.totalBuildings)}
                >
                  <CensusTractPopup feature={feature} />
                </GeoJSON>
              )
            })}
          </LayerGroup>
        </BaseLayer>
        <BaseLayer name="Rent Change, 2011 - 2017">
          <LayerGroup>
            {this.props.store.censusTracts.features.map((feature, index) => {
              return (
                <GeoJSON
                  key={`ct-${index}`}
                  data={feature['geometry']}
                  {...rentChangeLayerStyle(
                    feature.properties.medianRentChange20112017,
                    feature.properties.totalBuildings
                  )}
                >
                  <CensusTractPopup feature={feature} />
                </GeoJSON>
              )
            })}
          </LayerGroup>
        </BaseLayer>
        <BaseLayer name="Violations per Building, 2011 - 2017">
          <LayerGroup>
            {this.props.store.censusTracts.features.map((feature, index) => {
              return (
                <GeoJSON
                  key={`ct-${index}`}
                  data={feature['geometry']}
                  {...violationsPerBuildingLayerStyle(
                    feature.properties.violationsPerBuilding,
                    feature.properties.totalBuildings
                  )}
                >
                  <CensusTractPopup feature={feature} />
                </GeoJSON>
              )
            })}
          </LayerGroup>
        </BaseLayer>
        <BaseLayer name="Total Service Calls, 2011 - 2017">
          <LayerGroup>
            {this.props.store.censusTracts.features.map((feature, index) => {
              return (
                <GeoJSON
                  key={`ct-${index}`}
                  data={feature['geometry']}
                  {...serviceCallsTotalLayerStyle(
                    feature.properties.totalServiceCalls,
                    feature.properties.totalBuildings
                  )}
                >
                  <CensusTractPopup feature={feature} />
                </GeoJSON>
              )
            })}
          </LayerGroup>
        </BaseLayer>
        <BaseLayer name="Percent Service Calls with Violation">
          <LayerGroup>
            {this.props.store.censusTracts.features.map((feature, index) => {
              return (
                <GeoJSON
                  key={`ct-${index}`}
                  data={feature['geometry']}
                  {...serviceCallsPercentViolationLayerStyle(
                    feature.properties.percentServiceCallsWithViolation,
                    feature.properties.totalBuildings
                  )}
                >
                  <CensusTractPopup feature={feature} />
                </GeoJSON>
              )
            })}
          </LayerGroup>
        </BaseLayer>
        <BaseLayer name="Total Sales, 2011 - 2017">
          <LayerGroup>
            {this.props.store.censusTracts.features.map((feature, index) => {
              return (
                <GeoJSON
                  key={`ct-${index}`}
                  data={feature['geometry']}
                  {...salesTotalLayerStyle(feature.properties.totalSales, feature.properties.totalBuildings)}
                >
                  <CensusTractPopup feature={feature} />
                </GeoJSON>
              )
            })}
          </LayerGroup>
        </BaseLayer>
        <BaseLayer name="Total Sales with Prior Violations, 2011-2017">
          <LayerGroup>
            {this.props.store.censusTracts.features.map((feature, index) => {
              return (
                <GeoJSON
                  key={`ct-${index}`}
                  data={feature['geometry']}
                  {...salesTotalLayerStyle(
                    feature.properties.totalSalesPriorViolations,
                    feature.properties.totalBuildings
                  )}
                >
                  <CensusTractPopup feature={feature} />
                </GeoJSON>
              )
            })}
          </LayerGroup>
        </BaseLayer>
        <BaseLayer name="Avg Sales with Prior Violations, 2011-2017">
          <LayerGroup>
            {this.props.store.censusTracts.features.map((feature, index) => {
              return (
                <GeoJSON
                  key={`ct-${index}`}
                  data={feature['geometry']}
                  {...salesWithViolationPercentLayerStyle(
                    feature.properties.avgSalesPriorViolations,
                    feature.properties.totalBuildings
                  )}
                >
                  <CensusTractPopup feature={feature} />
                </GeoJSON>
              )
            })}
          </LayerGroup>
        </BaseLayer>
        <BaseLayer name="Avg # of violations 3 years before sale, 2011-2017">
          <LayerGroup>
            {this.props.store.censusTracts.features.map((feature, index) => {
              return (
                <GeoJSON
                  key={`ct-${index}`}
                  data={feature['geometry']}
                  {...violationsCountBeforeSaleLayerStyle(
                    feature.properties.avgViolationCount3YearsBeforeSale,
                    feature.properties.totalBuildings
                  )}
                >
                  <CensusTractPopup feature={feature} />
                </GeoJSON>
              )
            })}
          </LayerGroup>
        </BaseLayer>
        <BaseLayer name="Total Permits, 2011 - 2017">
          <LayerGroup>
            {this.props.store.censusTracts.features.map((feature, index) => {
              return (
                <GeoJSON
                  key={`ct-${index}`}
                  data={feature['geometry']}
                  {...permitsTotalLayerStyle(feature.properties.totalPermits, feature.properties.totalBuildings)}
                >
                  <CensusTractPopup feature={feature} />
                </GeoJSON>
              )
            })}
          </LayerGroup>
        </BaseLayer>
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
