# Objective: The aim of this assignment is to refactor an 
# existing Python script for a weather forecast application into a more structured, 
# object-oriented, and modular format. 
# The focus will be on identifying parts of the script that can be encapsulated 
# into classes and organizing these classes into appropriate modules to 
# enhance code readability, maintainability, and scalability.

# Task 1: Identifying and Creating Classes Analyze the 
# provided script and identify distinct functionalities that can be encapsulated into classes. 
# Create classes that represent different aspects of the weather forecast application, 
# such as fetching data, parsing data, and user interaction.

# Problem Statement: The existing script for the weather forecast 
# application is written in a procedural style and lacks organization.

# Weather Forecast Application Script

from weather_forecast import WeatherForecast

def main():
    forecast = WeatherForecast()
    while True:
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
        if city.lower() == 'exit':
            break
        detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
        if detailed == 'yes':
            print(forecast.get_detailed_forecast(city))
        else:
            forecast.parse_weather_data

if __name__ == "__main__":
    main()
# Expected Outcome:

# Clear definitions of classes 
# such as `WeatherDataFetcher`, `DataParser`, and `UserInterface`, 
# each handling specific parts of the application.