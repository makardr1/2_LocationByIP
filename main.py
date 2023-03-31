# Location by IP
# Location search by IP address using Python
import requests
import database


def location(ip: str):
    response = requests.get(f"http://ip-api.com/json/{ip}?lang=ru")
    if response.status_code == 404:
        print("Oops")
    result = response.json()
    if result["status"] == "fail":
        return main("Enter the correct IP address")

    record = []

    for key, value in result.items():
        record.append(value)
        print(f"[{key.title()}]: {value}")
    return tuple(record)


def main(start: str):
    print(start)
    ip = input("IP address: ")
    try:
        new_data = location(ip)
        database.base(new_data)
    except ValueError:
        pass


if __name__ == "__main__":
    main("Enter the IP address")
