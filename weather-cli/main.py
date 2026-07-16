from weather import get_weather
from utils import print_weather


def main():
    city = input("Enter city: ")
    try:
        data = get_weather(city)
        print_weather(data)
    except Exception as exc:
        print(exc)


if __name__ == "__main__":
    main()
