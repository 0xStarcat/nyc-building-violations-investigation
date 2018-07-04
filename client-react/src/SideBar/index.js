import React from 'react'
import AppLink from '../SharedComponents/AppLink'

import './style.scss'

const SideBar = () => {
  return (
    <div id="sidebar">
      <AppLink href="about">About</AppLink>
      <AppLink href="">Map</AppLink>
      <AppLink href="charts">Charts</AppLink>
    </div>
  )
}

export default SideBar
