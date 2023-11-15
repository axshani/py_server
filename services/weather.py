import random


class WeatherService(object):
    def __init__(self):
        self.weather_data = {
            'Yuma': 'It is a sunny day.',
            'Tórshavn': 'The sky is cloudy.',
            'Bangkok': 'Expect some rain this day.',
            'Reykjavík': 'Get ready for snowfall.',
        }

    def get_weather(self, location):
        # Simulate fetching weather data for the given city
        if location in self.weather_data:
            return self.weather_data[location]
        else:
            return self.get_random_weather()

    def get_random_weather(self):
        # Simulate fetching random weather data
        random_weather = random.choice(list(self.weather_data.values()))
        return random_weather

