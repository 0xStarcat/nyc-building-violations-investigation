import React, { Component } from 'react'
import { connect } from 'react-redux'
import SideBar from './SideBar'
import LeafletMap from './LeafletMap'
import { readCensusTracts } from './Store/CensusTracts/actions'
import { readNeighborhoods } from './Store/Neighborhoods/actions'

class App extends Component {
  componentWillMount() {
    this.props.dispatch(readCensusTracts())
    this.props.dispatch(readNeighborhoods())
  }

  render() {
    if (!(this.props.store.censusTracts.initialFetchCompleted || this.props.store.neighborhoods.initialFetchCompleted))
      return null
    return (
      <div className="App">
        <SideBar />
        <LeafletMap position={{ lat: 40.6881, lng: -73.9671 }} zoom={13} store={this.props.store} />
      </div>
    )
  }
}

const mapStateToProps = state => {
  return {
    store: state
  }
}

export default connect(
  mapStateToProps,
  null
)(App)
