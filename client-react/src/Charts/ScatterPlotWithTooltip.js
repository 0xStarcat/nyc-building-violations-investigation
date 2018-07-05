import React, { Component } from 'react'
import ScatterPlot from './ScatterPlot'

import './style.scss'

class ScatterPlotWithTooltip extends Component {
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
      <ScatterPlot
        data={this.props.data}
        title={this.props.title}
        tooltip={this.state.tooltip}
        showTooltip={this.showTooltip}
        hideTooltip={this.hideTooltip}
        xData={this.props.xData}
        yData={this.props.yData}
        xThreshold={this.props.xThreshold}
        yThreshold={this.props.yThreshold}
      />
    )
  }
}

export default ScatterPlotWithTooltip
