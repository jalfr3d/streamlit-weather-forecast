import requests

API_KEY = "c93babab5f22a1525d3283f7b8acfa07"


def get_data(place, forecast_days=None, kind_data=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    if kind_data == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if kind_data == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data


if __name__=="__main__":
    print(get_data(place="Tokyo", forecast_days=3, kind_data="Temperature"))
