# Dengue Outbreak Prediction — SDG 3: Good Health and Well-being

## Project Overview
This project uses machine learning to predict dengue fever outbreaks based on environmental and weather data. Accurate predictions help public health officials allocate resources efficiently and prevent the spread of disease, contributing to the UN Sustainable Development Goal 3: Good Health and Well-being.

## Dataset
- Source: Dengue Fever dataset from Kaggle  
- Contains weekly dengue cases by city, along with weather features such as temperature, humidity, and precipitation.

## Approach
- **Model:** Random Forest Regressor  
- **Features:** Air temperature, relative humidity, precipitation, and station temperature/precipitation  
- **Goal:** Predict total dengue cases per week.

## Results
- Visualization of actual vs predicted cases shows good predictive performance.

## Ethical Considerations
- Data may have underreported cases, affecting fairness.  
- Model predictions should support, not replace, expert decisions.

## How to Run
1. Clone the repo.  
2. Run the `dengue_prediction.py` script or Jupyter notebook.  
3. Requirements: Python 3.x, pandas, scikit-learn, matplotlib, seaborn.

## Future Work
- Integrate real-time data via APIs.  
- Deploy as a web app for public health use.

---
