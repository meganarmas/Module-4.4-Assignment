from weather import WeatherDataFletch

class WeatherForecast:
    def parse_weather_data(self, data, city,):
        # Function to parse weather data
        if not data:
            return "Weather data not available"
        city = data["city"]
        temperature = data["temperature"]
        condition = data["condition"]
        humidity = data["humidity"]
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"


    def get_detailed_forecast(self, city):
        # Function to provide a detailed weather forecast for a city
        data = WeatherDataFletch.fetch_weather_data(self, city)
        return self.parse_weather_data(data, city)

    def display_weather(self, city):
        # Function to display the basic weather forecast for a city
        data = WeatherDataFletch.fetch_weather_data(city)
        if not data:
            print(f"Weather data not available for {city}")
            return self.parse_weather_data(data, city)