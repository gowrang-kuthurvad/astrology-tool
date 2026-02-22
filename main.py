from chart import generate_chart


def main():
    print("🔮 Astrology Birth Chart Generator 🔮")
    
    date = input("Enter birth date (YYYY/MM/DD): ")
    time = input("Enter birth time (HH:MM in 24hr format): ")
    latitude = float(input("Enter latitude: "))
    longitude = float(input("Enter longitude: "))

    result = generate_chart(date, time, latitude, longitude)

    print("\n✨ Your Core Placements ✨")
    for key, value in result.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
