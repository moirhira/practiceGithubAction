def print_weather(d):
    print(f"City: {d['name']}, {d['sys']['country']}")
    print(f"Temperature: {d['main']['temp']}°C")
    print(f"Feels like: {d['main']['feels_like']}°C")
    print(f"Humidity: {d['main']['humidity']}%")
    print(f"Wind: {d['wind']['speed']} m/s")
    print(f"Condition: {d['weather'][0]['description']}")
