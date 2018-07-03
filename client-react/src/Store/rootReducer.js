import { combineReducers } from 'redux'
import { routerReducer } from 'react-router-redux'

import { censusTractsReducer } from './CensusTracts/reducers/censusTractsReducer'
import { neighborhoodsReducer } from './Neighborhoods/reducers/neighborhoodsReducer'

export default combineReducers({
  routing: routerReducer,
  censusTracts: censusTractsReducer,
  neighborhoods: neighborhoodsReducer
})
