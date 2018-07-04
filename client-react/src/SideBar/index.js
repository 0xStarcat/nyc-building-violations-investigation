import React from 'react'
import AppLink from '../SharedComponents/AppLink'

import './style.scss'

const SideBar = () => {
  const baseUrl = process.env.REACT_APP_PUBLIC_URL // will be /hypercomp

  return (
    <div id="sidebar">
      <AppLink href={`${baseUrl}/about`}>About</AppLink>
      <AppLink href={`${baseUrl}/`}>Map</AppLink>
      <AppLink href={`${baseUrl}/charts`}>Charts</AppLink>
    </div>
  )
}

export default SideBar
