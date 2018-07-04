import React, { Component } from 'react'
import SideBar from '../SideBar'

import ScatterPlotWithTooltip from '../Charts/ScatterPlotWithTooltip'

class ChartPage extends Component {
  constructor(props) {
    super(props)
  }

  render() {
    return (
      <div>
        <SideBar />
        <ScatterPlotWithTooltip store={this.props.store} xData="raceWhitePercent2016" yData="medianRent2017" />
        <ScatterPlotWithTooltip
          store={this.props.store}
          xData="medianIncomeChange20112017"
          xThreshold={[-40000]}
          yData="percentServiceCallsWithViolation"
        />
        <ScatterPlotWithTooltip
          store={this.props.store}
          xData="medianIncome2017"
          yData="violationsPerBuilding"
          xThreshold={[-40000, 150000]}
          yThreshold={[null, 80]}
        />
        <ScatterPlotWithTooltip
          store={this.props.store}
          xData="medianIncome2017"
          yData="violationsNonCommunityPerBuilding"
          xThreshold={[-40000, 150000]}
        />
      </div>
    )
  }
}

export default ChartPage
