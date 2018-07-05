import React from 'react'
import { AxisLeft, AxisBottom } from '@vx/axis'
import { LinearGradient } from '@vx/gradient'
import { Group } from '@vx/group'
import { appleStock } from '@vx/mock-data'
import { GlyphCircle } from '@vx/glyph'
import { scaleLinear, scaleThreshold } from '@vx/scale'
import { withTooltip, Tooltip } from '@vx/tooltip'
import { LinePath } from '@vx/shape'
import { curveMonotoneX } from '@vx/curve'
import { Legend } from '@vx/legend'
import { extent, max, min } from 'd3-array'

import { calcLinear } from './utils/statisticalAnalysis'
import TrendLine from './TrendLine'
import { TooltipContext } from './context/TooltipContext'

const ScatterPlot = props => {
  if (!props.data) return null
  let tooltipTimeout

  const width = 1000
  const height = 400
  const margin = {
    top: 60,
    bottom: 60,
    left: 280,
    right: 80
  }
  const xMax = width - margin.left - margin.right
  const yMax = height - margin.top - margin.bottom

  const x = d => {
    if (!d) return
    return d.x
  }

  const y = d => {
    if (!d) return
    return d.y
  }

  const xScale = scaleLinear({
    range: [0, xMax],
    domain: extent(props.data, x)
  })

  const yScale = scaleLinear({
    range: [yMax, 0],
    domain: [0, max(props.data, y)]
  })

  const legendThreshold = scaleThreshold({
    range: [0, 100],
    domain: [0, 1]
  })

  const regressionCalculation = calcLinear(props.data, props.xData, props.yData, min(props.data, x), min(props.data, y))
  return (
    <div>
      <h3 className="graph-title">{props.title}</h3>
      <svg width={width} height={height}>
        <Group top={margin.top} left={margin.left}>
          <AxisLeft scale={yScale} top={0} left={0} label={props.yData} stroke={'#1b1a1e'} tickTextFill={'#1b1a1e'} />
          <AxisBottom scale={xScale} top={yMax} label={props.xData} stroke={'#1b1a1e'} tickTextFill={'#1b1a1e'} />
          {regressionCalculation[0].x && (
            <TrendLine data={regressionCalculation} xMax={xMax} yMax={yMax} x={x} y={y} stroke="red" strokeWidth={1} />
          )}
          {props.data.map((point, i) => {
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
                  const rect = event.target.getBoundingClientRect()
                  props.showTooltip({
                    tooltipLeft: rect.left + window.pageXOffset - 100,
                    tooltipTop: rect.top + window.pageYOffset + 50,
                    tooltipData: {
                      name: point.properties.name,
                      neighborhood: point.properties.neighborhood,
                      [props.xData]: point.properties[props.xData],
                      [props.yData]: point.properties[props.yData]
                    }
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
      <Legend scale={legendThreshold} labelMargin="0 0 0 200px" />
      <TooltipContext.Consumer>
        {tooltip =>
          tooltip.tooltipOpen && (
            <Tooltip left={tooltip.tooltipLeft} top={tooltip.tooltipTop}>
              {Object.keys(tooltip.tooltipData).map((key, index) => {
                return (
                  <div key={`${key}-${index}`}>
                    <div>
                      <strong>{key}: </strong>
                      {tooltip.tooltipData[key]}
                    </div>
                  </div>
                )
              })}
            </Tooltip>
          )
        }
      </TooltipContext.Consumer>
    </div>
  )
}

export default ScatterPlot
