# Energy Consumption Building Predictor App with Machine Learning

Project Title: Energy Consumption Prediction in Buildings Using Machine Learning

Buildings are among the largest consumers of energy worldwide, accounting for a significant portion of electricity use in both residential and commercial sectors. A major challenge in energy management is the ability to anticipate consumption patterns in response to dynamic environmental conditions and human activity. Traditional methods of forecasting energy demand often fail to incorporate real-time and granular variables such as user activity and ambient temperature.

With the advent of smart buildings and IoT-enabled sensors, large volumes of time-stamped data can now be collected, making it feasible to leverage machine learning for real-time energy prediction. This project aims to utilize this data to build models that can learn from historical trends and adapt to varying conditions, ultimately contributing to smarter and more sustainable energy use.

Benefits and Impact:
1. Operational Efficiency: By predicting energy usage more accurately, building managers can optimize HVAC systems, lighting, and other electrical components, reducing unnecessary energy consumption.
2. Cost Savings: Improved prediction allows for better demand-side energy planning, potentially lowering peak demand charges and overall utility bills.
3. Sustainability: Efficient energy use contributes to a reduction in carbon footprint and supports broader environmental goals.
4. Scalability: The developed models can be adapted to different types of buildings and integrated with energy management systems in smart cities.

This project focuses on the development and evaluation of machine learning models to predict building energy consumption based on key influencing factors such as time of day, user activity level, and ambient temperature. The primary goal is to create a predictive system that can accurately estimate hourly energy usage, enabling more efficient energy management and planning.

![streamlit](https://github.com/Farhan-Fadillah/picture_list/blob/48306e7e53efbc214b167c9a2cf404d6a536fb8a/app%20building%20consump.png)

Three different modeling approaches will be explored:
Linear Regression – to provide a simple, interpretable baseline.
Decision Tree Regression – to capture non-linear relationships and feature interactions.
Artificial Neural Networks (ANNs) – to model complex patterns in the data for potentially higher predictive accuracy.

The dataset will include historical energy usage logs, time-stamped activity metrics (such as occupancy or device usage), and environmental data (including temperature readings). 

# Dataset Structure and Preprocessing

The dataset consists of the following columns:
- timestamp = Date and time of the recorded data point (used to extract hour and day of the week features)
- temperature = Ambient temperature in degrees Celsius
- user activity level = Numeric value (0.0 to 1.0) representing the level of user activity in the building
- energy_consumption = Energy consumed by the building at the given timestamp (target variable, in kWh)

Preprocessing Steps:
1. Convert the timestamp column to datetime format
2. Extract hour of the day and day of the week from the timestamp to capture temporal patterns
3. Drop the original timestamp column after feature extraction
4. Separate features (temperature, user_activity_level, hour, dayofweek) and target (energy_consumption)
5. Split the dataset into training and testing sets (80% train, 20% test)

This preprocessing ensures the models can learn temporal dependencies and environmental/user factors affecting energy consumption.

# Project Workflow and Flow Mapping
Here is a step-by-step flow of how the project works, from data input to prediction and recommendations:

- STEP 1 : Data Collection
  - Collect raw data with columns: timestamp, temperature, user_activity_level, and energy_consumption.
  
- STEP 2 : Data Preprocessing
  - Extract time features (hour, dayofweek) from timestamp.
  - Prepare feature matrix X and target vector y.
  - Split data into training and testing sets.

- STEP 3 : Model Training
  - Train three models on the training data:
    - Linear Regression: A simple, interpretable model for baseline predictions.
    - Decision Tree Regressor: Captures non-linear relationships and interactions.
    - Neural Network (NN): A deep learning model with two hidden layers for complex pattern recognition.
 
- STEP 4 : Model Evaluation
  - Evaluate each model on the test set using Root Mean Squared Error (RMSE).
  - Compare model performances to select the best or allow user choice.

- STEP 5 : Real-time Prediction Interface (Streamlit App)
  - User inputs:
    1. Time (hour)
    2. Temperature
    3. User activity level
  - The app converts time input to hour and dayofweek.
  - User selects the model to use for prediction.
  - The selected model predicts energy consumption based on inputs.

- STEP 6 : Alert and Recommendation System
  - If predicted energy consumption exceeds a threshold (e.g., 100 kWh), the system triggers an alert to provides actionable recommendations to reduce energy consumption.

# Flow Diagram
![flow](https://github.com/Farhan-Fadillah/picture_list/blob/48306e7e53efbc214b167c9a2cf404d6a536fb8a/FLOW%20PROJECT%20ENERGY%20BUILDING.png)

# Model Implementation Details

![model](https://github.com/Farhan-Fadillah/picture_list/blob/48306e7e53efbc214b167c9a2cf404d6a536fb8a/modeling%20for%20energy%20building%20ML.png)

The neural network is trained for 50 epochs with a batch size of 10. RMSE is calculated on the test set to measure prediction accuracy. The user can select any model for prediction in the app.

# Prediction Alert and Recommendation System

Alert Logic:
- A maximum energy consumption threshold is set (e.g., 100 kWh).
- If the predicted consumption exceeds this threshold, the system triggers a warning.

Recommendations Provided:
1.	Reduce AC temperature: Lowering the air conditioning temperature reduces energy use.
2.	Turn off unused electronic devices: Minimizes unnecessary power consumption.
3.	Adjust user activity levels: Encourage reducing or relocating activities to more energy-efficient areas.
4.	Check lighting systems: Ensure lights are off in unoccupied spaces.

These recommendations are designed to be practical and actionable, helping building managers or occupants reduce energy consumption effectively.

# Additional Features in the Streamlit App

![app](https://github.com/Farhan-Fadillah/picture_list/blob/48306e7e53efbc214b167c9a2cf404d6a536fb8a/app%20building%20consump%20result.png)

1. Historical Energy Consumption Visualization: Users can view a time series chart of past energy consumption data to understand trends.
2. nteractive Inputs: Time, temperature, and activity sliders allow dynamic prediction.
3. Model Selection: Users can compare predictions from different models.

# SUMMARY

This is a multi-model machine learning system that not only predicts building energy consumption but also provides actionable insights to optimize energy use. The integration with Streamlit makes it user-friendly and interactive, suitable for real-time decision-making.





