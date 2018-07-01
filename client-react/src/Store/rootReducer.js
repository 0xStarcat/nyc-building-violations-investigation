import { combineReducers } from 'redux'
import { censusTractsReducer } from './CensusTracts/reducers/censusTractsReducer'

export default combineReducers({
  censusTracts: censusTractsReducer
})
