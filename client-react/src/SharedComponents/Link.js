import React from 'react'
import PropTypes from 'prop-types'

import { push } from 'react-router-redux'
import { connect } from 'react-redux'

class Link extends React.Component {
  constructor(props) {
    super(props)
    this.clickLink = this.clickLink.bind(this)
  }

  clickLink(e) {
    e.preventDefault()
    this.props.dispatch(push(`/${this.props.href}`))
  }

  render() {
    return (
      <a className={`link-element ${this.props.className || ''}`} href={this.props.href} onClick={this.clickLink}>
        {this.props.children}
      </a>
    )
  }
}

Link.propTypes = {
  href: PropTypes.string
}

export default connect()(Link)
