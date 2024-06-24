def calculate_wind_chill(temperature, wind_speed):
    # Celsius formula
    wind_chill_c = 13.12 + 0.6215 * temperature - 11.37 * wind_speed ** 0.16 + 0.3965 * temperature * wind_speed ** 0.16
    # Fahrenheit formula
    wind_chill_f = 35.74 + 0.6215 * temperature - 35.75 * wind_speed ** 0.16 + 0.4275 * temperature * wind_speed ** 0.16
    return wind_chill_c, wind_chill_f

temperature = float(input("What is the temperature: "))
scale = input("Fahrenheit or Celsius (F/C)? ")

if scale.lower() == 'c':
    
    for wind_speed in range(5, 65, 5):
        wind_chill_c, _ = calculate_wind_chill(temperature, wind_speed)
        print(f"At temperature {temperature}°C and wind speed {wind_speed} mph, the wind chill is: {wind_chill_c:.2f} °C")

elif scale.lower() == 'f':
    
    for wind_speed in range(5, 65, 5):
        _, wind_chill_f = calculate_wind_chill(temperature, wind_speed)
        print(f"At temperature {temperature}°F and wind speed {wind_speed} mph, the wind chill is: {wind_chill_f:.2f} °F")

else:
    print("Error!")


