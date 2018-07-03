import React, { Component } from 'react'

import ScatterPlot from '../Charts/ScatterPlot'
import SideBar from '../SideBar'

class ChartPage extends Component {
  constructor(props) {
    super(props)

    this.state = {
      tooltip: {
        tooltipOpen: false
      }
    }

    this.showTooltip = this.showTooltip.bind(this)
    this.hideTooltip = this.hideTooltip.bind(this)
  }

  showTooltip(tooltipData) {
    this.setState({ tooltip: { ...tooltipData, tooltipOpen: true } })
  }

  hideTooltip() {
    this.setState({ tooltip: { tooltipOpen: false } })
  }

  render() {
    return (
      <div>
        <SideBar />
        <ScatterPlot
          store={this.props.store}
          tooltip={this.state.tooltip}
          showTooltip={this.showTooltip}
          hideTooltip={this.hideTooltip}
          xData="raceWhitePercent2016"
          yData="medianRent2017"
        />
        <ScatterPlot
          store={this.props.store}
          tooltip={this.state.tooltip}
          showTooltip={this.showTooltip}
          hideTooltip={this.hideTooltip}
          xData="medianRent2017"
          yData="percentServiceCallsUnresolved"
        />
      </div>
    )
  }
}

export default ChartPage
