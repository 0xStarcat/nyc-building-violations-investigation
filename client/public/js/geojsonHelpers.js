export const styleIncomeLayers = feature => {
        if (feature.properties.median_income_2017 >= 110000) {
            return { 
              color: "white",
              fillColor: "#005a32",
              opacity: 0.5,
              fillOpacity: 0.5,
              weight: 1
            }
        } else if (feature.properties.median_income_2017 >= 90000) {
            return { 
              color: "white",
              fillColor: "#238b45",
              opacity: 0.5,
              fillOpacity: 0.5,
              weight: 1
            }
        } else if (feature.properties.median_income_2017 >= 70000) {
            return { 
              color: "white",
              fillColor: "#41ab5d",
              opacity: 1,
              fillOpacity: 0.5,
              weight: 1
            }
        } else if (feature.properties.median_income_2017 >= 50000) {
            return { 
              color: "white",
              fillColor: "#74c476",
              opacity: 1,
              fillOpacity: 0.5,
              weight: 1
            }
        } else if (feature.properties.median_income_2017 >= 30000) {
            return { 
              color: "white",
              fillColor: "#a1d99b",
              opacity: 1,
              fillOpacity: 0.5,
              weight: 1
            }
        } else if (feature.properties.median_income_2017 >= 10000) {
            return { 
              color: "white",
              fillColor: "#c7e9c0",
              opacity: 1,
              fillOpacity: 0.5,
              weight: 1
            }
        } else if (!feature.properties.median_income_2017) {
            return { 
              color: "#ghowhite",
              fillColor: "#ghostwhite",
              opacity: 1,
              fillOpacity: 0.2,
              weight: 0.5
            }
        } else {
          return { 
              color: "white",
              fillColor: "#edf8e9",
              opacity: 1,
              fillOpacity: 0.5,
              weight: 1
            }
        }
    }