import React from 'react'
import AppLink from '../SharedComponents/AppLink'

import './style.scss'

const SideBar = () => {
  return (
    <div id="sidebar">
      <AppLink href={`${baseUrl}/about`}>About</AppLink>
      <AppLink href={`${baseUrl}/`}>Map</AppLink>
      <AppLink href={`${baseUrl}/charts`}>Charts</AppLink>
    </div>
  )
}

export default SideBar
