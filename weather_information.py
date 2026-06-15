weather_information = []
time = int(input("enter the hour of the day (0-23): "))
temp = float(input("enter the temperature: "))
feels_like = float(input("enter what it  feels like; temperature: "))
while True:
        humidity = int(input("enter the humidity: "))
        if humidity >= 0 and humidity <= 100:
            break
        else:
            print("Invalid humidity value, please enter a value between 0 and 100")
pressure = int(input("enter the pressure: "))
hourly_weather = {'time': time, 'temp': temp , 'feels_like': feels_like , 'humidity': humidity,  'pressure': pressure}
weather_information.append(hourly_weather)
print(weather_information)

                        