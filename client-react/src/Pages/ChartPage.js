import React, { Component } from 'react'
import SideBar from '../SideBar'
import { filterNumberData } from '../Charts/utils/filterData'
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
          data={filterNumberData(
            this.props.store.censusTracts.features,
            'medianIncomeChange20112017',
            'percentServiceCallsWithViolation',
            [-40000]
          )}
          title="Median Income Change 2011-2017 vs. % of Service Calls resulting in a violation"
          xData="medianIncomeChange20112017"
          yData="percentServiceCallsWithViolation"
        />
        <ScatterPlotWithTooltip
          data={filterNumberData(
            this.props.store.censusTracts.features,
            'medianIncome2017',
            'violationsPerBuilding',
            [-40000, 150000],
            [null, 80]
          )}
          title="Median Income 2017 vs. violations per building"
          xData="medianIncome2017"
          yData="violationsPerBuilding"
        />
        <ScatterPlotWithTooltip
          data={filterNumberData(
            this.props.store.censusTracts.features,
            'medianIncome2017',
            'violationsNonCommunityPerBuilding',
            [-40000, 150000]
          )}
          title="Median Income 2017 vs # of violations originating outside of community per building"
          xData="medianIncome2017"
          yData="violationsNonCommunityPerBuilding"
        />
      </div>
    )
  }
}

export default ChartPage
