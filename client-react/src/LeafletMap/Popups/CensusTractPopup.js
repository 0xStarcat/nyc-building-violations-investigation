import React from 'react'
import PropTypes from 'prop-types'
import { Popup } from 'react-leaflet'

const CensusTractPopup = props => {
  return (
    <Popup>
      <div>
        Census Tract: {props.feature.properties.name}
        <br />
        Neighborhood: {props.feature.properties.neighborhood}
        <br />
        Median Income 2011: {props.feature.properties.medianIncome2011}
        <br />
        Median Income 2017: {props.feature.properties.medianIncome2017}
        <br />
        Median Income Change, 2011 - 2017 {props.feature.properties.medianIncomeChange20112017}
        <br />
        Median Rent 2011: {props.feature.properties.medianRent2011}
        <br />
        Median Rent 2017: {props.feature.properties.medianRent2017}
        <br />
        Median Rent Change 2011 - 2017: {props.feature.properties.medianRentChange20112017}
        <br />
        % White 2016: {props.feature.properties.raceWhitePercent2016}
        <br />
        % White Change 2011 - 2016: {props.feature.properties.raceWhitePercentChange20112016}
        <br />
        Total Buildings: {props.feature.properties.totalBuildings}
        <br />
        Violation Per Bldg: {props.feature.properties.violationsPerBuilding}
        <br />
        Total Sales: {props.feature.properties.totalSales}
        <br />
        Total Sales with prior violations: {props.feature.properties.totalSalesPriorViolations}
        <br />
        Average Sales w Prior Violations: {props.feature.properties.avgSalesPriorViolations}%
        <br />
        Total Permits: {props.feature.properties.totalPermits}
        <br />
        Avg violation over 3 years before sale: {props.feature.properties.avgViolationCount3YearsBeforeSale}
        <br />
        Total service calls: {props.feature.properties.totalServiceCalls}
        <br />
        service calls resulting in violation: {props.feature.properties.percentServiceCallsWithViolation}%
      </div>
    </Popup>
  )
}

CensusTractPopup.propTypes = {
  feature: PropTypes.object
}

export default CensusTractPopup
