import tkinter as tk
import random

weather_predictions = [
    "Sunny with a chance of dragon sightings.",
    "Cloudy with a 100% chance of wizard battles.",
    "Expect some magical rainbows and unicorns.",
    "Heavy snowfall, perfect for building snow castles.",
    "Thunderstorms with a possibility of Thor's visit.",
    "Hail of candy and chocolate expected in the afternoon.",
    "Mild breeze with fairy dust floating around.",
    "Foggy with random portals to another dimension.",
    "Clear skies, great for stargazing and spotting UFOs.",
    "Tornado of puppies and kittens is on the horizon.",
    "Heatwave with a chance of spontaneous beach parties.",
    "Meteor showers with actual meteors landing in your yard.",
    "today a big meteor will fall in usa",
    "in the region of tokyo it will probably heavy rain",
    "Blizzard of confetti, ideal for impromptu celebrations."
]

def get_weather_prediction():
    return random.choice(weather_predictions)

def update_weather():
    prediction = get_weather_prediction()
    weather_label.config(text=prediction)

root = tk.Tk()
root.title("Unexpected Weather Forecast")

weather_label = tk.Label(root, text="Click the button for today's forecast!", wraplength=300, font=("Helvetica", 16))
weather_label.pack(pady=20)


weather_button = tk.Button(root, text="Get Forecast", command=update_weather, font=("Helvetica", 14))
weather_button.pack(pady=20)


root.mainloop()
