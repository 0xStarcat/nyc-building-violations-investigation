import React, { Component } from 'react'
import { connect } from 'react-redux'
import LeafletMap from './LeafletMap'
import { readCensusTracts } from './Store/CensusTracts/actions'
class App extends Component {
  componentWillMount() {
    this.props.dispatch(readCensusTracts())
  }

  render() {
    if (!this.props.store.censusTracts.initialFetchCompleted) return null
    return (
      <div className="App">
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
