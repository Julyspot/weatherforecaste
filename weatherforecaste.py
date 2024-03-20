import tkinter as tk
from tkinter import messagebox
import requests

def get_weather(city):
    api_key = "1b64af5938dc77b222436c981cbb6e9a"  # Replace "YOUR_API_KEY" with your actual OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        if data["cod"] == 200:
            weather_description = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            return {
                "description": weather_description,
                "temperature": temperature,
                "humidity": humidity,
                "wind_speed": wind_speed
            }
        else:
            return None
    except Exception as e:
        print(e)
        return None

def get_weather_info():
    city = city_entry.get()
    weather_data = get_weather(city)
    if weather_data:
        result_text = (f"Weather in {city}:\n"
                       f"Description: {weather_data['description']}\n"
                       f"Temperature: {weather_data['temperature']}°C\n"
                       f"Humidity: {weather_data['humidity']}%\n"
                       f"Wind Speed: {weather_data['wind_speed']} m/s")
        result_label.config(text=result_text, fg="blue")
    else:
        messagebox.showerror("Error", "City not found or error in retrieving data.")

# Create the main window
root = tk.Tk()
root.title("Weather Forecast App")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

# Create and place widgets
city_label = tk.Label(root, text="Enter city name:", bg="#f0f0f0", font=("Arial", 14))
city_label.pack()

city_entry = tk.Entry(root, font=("Arial", 14))
city_entry.pack()

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather_info, font=("Arial", 14), bg="#0080ff", fg="white")
get_weather_button.pack(pady=10)

result_label = tk.Label(root, text="", bg="#f0f0f0", font=("Arial", 12), justify="left")
result_label.pack()

# Run the application
root.mainloop()
