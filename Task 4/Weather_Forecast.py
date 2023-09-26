import tkinter as tk
import requests
from tkinter import messagebox

# Function to get weather data from OpenWeatherMap API
def get_weather_data(city):
    api_key = "a2bd44c39b4e010b44556b68408ee32b"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    complete_url = base_url + "?q=" + city + "&appid=" + api_key
    response = requests.get(complete_url)
    return response.json()

# Function to extract weather information from API response
def extract_weather_info(weather_data):
    temperature = weather_data["main"]["temp"] - 273.15
    humidity = weather_data["main"]["humidity"]
    wind_speed = weather_data["wind"]["speed"]
    description = weather_data["weather"][0]["description"]
    return temperature, humidity, wind_speed, description

# Function to display weather information in a messagebox
def display_weather_info(city, temperature, humidity, wind_speed, description):
    messagebox.showinfo("Weather Forecast", f"City: {city}"
                        f"\nTemperature: {temperature:.2f}°C\nHumidity: {humidity}%"
                        f"\nWind Speed: {wind_speed} m/s\nDescription: {description}")

# Function to fetch weather data and display it
def get_weather_and_display(city):
    weather_data = get_weather_data(city)
    if weather_data and 'main' in weather_data:
        temperature, humidity, wind_speed, description = extract_weather_info(weather_data)
        display_weather_info(city, temperature, humidity, wind_speed, description)
    else:
        messagebox.showerror("Error", "Weather data not found. Please check your input.")

# Create the main window
window = tk.Tk()
window.title("Weather Forecast")

# Increase font size
font_size = 14

city_label = tk.Label(window, text="City:", font=("Helvetica", font_size))
city_label.grid(row=0, column=0)

city_entry = tk.Entry(window, font=("Helvetica", font_size))
city_entry.grid(row=0, column=1)

get_weather_button = tk.Button(window, text="Get Weather", command=lambda: get_weather_and_display(city_entry.get()), font=("Helvetica", font_size))
get_weather_button.grid(row=0, column=2)

# Increase width of the Entry widget
city_entry.config(width=20)

# Start the main GUI loop
window.mainloop()
