import random
def get_random_weather_data():
    temp = random.uniform(-50, 50)
    feels_like = temp + random.uniform(-10, 10)
    humidity = random.randint(0, 100)
    pressure = random.randint(990, 1010)
    return {
        'temp': temp,
        'feels_like': feels_like,
        'humidity': humidity,
        'pressure': pressure
    }  
def get_average_temperature(weather_data):
     total_temp = 0
     for  data in weather_data:
            total_temp += data['temp']
     average_temp = total_temp / len(weather_data) if weather_data else 0
     return average_temp
weather_information =[]
for weather in range(1, 101):
      weather_information.append(get_random_weather_data())
print(weather_information)
print("Average Temperature:", get_average_temperature(weather_information))



