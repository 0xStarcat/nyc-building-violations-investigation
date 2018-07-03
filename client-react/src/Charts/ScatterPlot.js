import React from 'react'
import { AxisLeft, AxisBottom } from '@vx/axis'
import { LinearGradient } from '@vx/gradient'
import { Group } from '@vx/group'
import { appleStock } from '@vx/mock-data'
import { GlyphCircle } from '@vx/glyph'
import { scaleTime, scaleLinear } from '@vx/scale'
import { withTooltip, Tooltip } from '@vx/tooltip'

import { extent, max } from 'd3-array'
const ScatterPlot = props => {
  let tooltipTimeout

  const data = props.store.censusTracts.features.filter(feature => {
    return feature.properties[props.xData] && feature.properties[props.yData]
  })
  const width = 1200
  const height = 500
  const margin = {
    top: 60,
    bottom: 60,
    left: 280,
    right: 80
  }
  const xMax = width - margin.left - margin.right
  const yMax = height - margin.top - margin.bottom

  const x = d => {
    return parseFloat(d.properties[props.xData])
  }

  const y = d => {
    return parseFloat(d.properties[props.yData])
  }

  const xScale = scaleLinear({
    range: [0, xMax],
    domain: extent(data, x)
  })

  const yScale = scaleLinear({
    range: [yMax, 0],
    domain: [0, max(data, y)]
  })

  console.log(xMax)
  return (
    <div>
      <svg width={width} height={height}>
        <Group top={margin.top} left={margin.left}>
          <AxisLeft scale={yScale} top={0} left={0} label={props.yData} stroke={'#1b1a1e'} tickTextFill={'#1b1a1e'} />
          <AxisBottom scale={xScale} top={yMax} label={props.xData} stroke={'#1b1a1e'} tickTextFill={'#1b1a1e'} />

          {data.map((point, i) => {
            return (
              <GlyphCircle
                className="dot"
                key={`point-${point.properties.name}-${i}`}
                fill={'#f6c431'}
                left={xScale(x(point))}
                top={yScale(y(point))}
                size={20}
                onMouseEnter={() => event => {
                  if (tooltipTimeout) clearTimeout(tooltipTimeout)
                  props.showTooltip({
                    tooltipLeft: xScale(x(point)) + 200,
                    tooltipTop: yScale(y(point)) + 20,
                    tooltipData: point
                  })
                }}
                onMouseLeave={() => event => {
                  tooltipTimeout = setTimeout(() => {
                    props.hideTooltip()
                  }, 300)
                }}
              />
            )
          })}
        </Group>
      </svg>
      {props.tooltip.tooltipOpen && (
        <Tooltip left={props.tooltip.tooltipLeft} top={props.tooltip.tooltipTop}>
          <div>
            <strong>Census Tract:</strong> {props.tooltip.tooltipData.properties.name}
          </div>
          <div>
            <strong>Neighborhood:</strong> {props.tooltip.tooltipData.properties.neighborhood}
          </div>
          <div>
            <strong>{props.xData}:</strong> {props.tooltip.tooltipData.properties[props.xData]}
          </div>
          <div>
            <strong>{props.yData}:</strong> {props.tooltip.tooltipData.properties[props.yData]}
          </div>
        </Tooltip>
      )}
    </div>
  )
}

export default ScatterPlot
