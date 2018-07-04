import React from 'react'
import AppLink from '../SharedComponents/AppLink'

import './style.scss'

const SideBar = () => {
  return (
    <div id="sidebar">
      <AppLink href="about">About</AppLink>
      <AppLink href="maps">Map</AppLink>
      <AppLink href="">Charts</AppLink>
    </div>
  )
}

export default SideBar
