# Weather Forecast Web App

## Overview

This web app allows you to check the weather forecast for the next 5 days in any city around the world. It provides information on temperature and sky conditions, helping you stay prepared for changing weather.

## Features

- **City Selection**: Enter the name of the city you want to check the weather for.

- **Forecast Days**: Use the slider to select the number of days you want to see in the weather forecast, up to 5 days.

- **Data Options**: Choose whether you want to view temperature or sky conditions for the selected days.

## How It Works

1. Start the web app using the command `streamlit run main.py`.

2. Enter the name of the city for which you want to check the weather.

3. Use the slider to specify the number of forecast days (up to 5).

4. Select whether you want to view temperature or sky conditions.

5. Click on "Run" to see the weather forecast.

6. The app will display a graph showing temperature trends or images representing sky conditions for the selected days.

## Prerequisites

Before using this web app, make sure you have the following Python libraries installed:

- [streamlit](https://streamlit.io/): To create interactive web apps.
- [plotly](https://plotly.com/python/): For creating interactive plots.
- [requests](https://docs.python-requests.org/en/latest/): For making API requests.

You'll also need to obtain an API key from [OpenWeatherMap](https://openweathermap.org/api) and replace `"API_KEY"` in the `backend.py` file with your actual API key.

## Configuration

1. Obtain an API key from OpenWeatherMap and replace `"API_KEY"` in the `backend.py` file with your API key.

2. Customize the app's appearance, layout, or any additional features according to your preferences.

## Notes

- Ensure that you run the web app using the command specified in the "How It Works" section.

- The weather data is retrieved from the OpenWeatherMap API and is updated dynamically.

- This web app provides a simple yet powerful way to check the weather forecast for any location worldwide.

That's it! Enjoy using the Weather Forecast Web App to stay informed about the weather conditions in any city.

### License
This project is licensed under the MIT License. You are free to use and modify the code for your own purposes.
