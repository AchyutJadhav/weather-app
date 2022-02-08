from tkinter import *
import requests
from geopy.geocoders import Nominatim
from tkinter import messagebox
import time
from datetime import datetime

get_location = None


def search_location():
    global get_location
    my_location = Nominatim(user_agent="GetLoc")
    city = location_entry.get()
    try:
        get_location = my_location.geocode(city)
    except:
        messagebox.showerror(title="Weather App", message="Please, Check your internet connection")

    else:
        try:
            address = get_location.address
            lat = get_location.latitude
            log = get_location.longitude

        except AttributeError:
            messagebox.showinfo(title="Weather App", message="Sorry, We can not find weather for your location")

        # except requests.ConnectionError:
        #     messagebox.showerror(title="Weather App", message="Please, Check your internet connection")

        else:
            location1 = Label(text=f"Your Location: {address}", font=("Arial", 22, "bold"), wraplength=900)
            location1.place(x=550, y=00)

            key = "f1ddbc2a6b1fb4703653ffae5e0a4574"
            parameters = {
                "units": "metric"
            }

            response = requests.get(
                f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={log}&appid={key}",
                params=parameters)

            sky_status = response.json()['weather'][0]['description']
            sky_text.config(text=f'Sky: {sky_status}')

            pressure_value = response.json()['main']['pressure']
            pressure_text.config(text=f"Atmospheric Pressure: {pressure_value} hPa")

            average_temp = response.json()['main']['temp']
            average_temp_text.config(text=f"Average Temperature: {average_temp}°C")

            humidity_value = response.json()['main']['humidity']
            humidity_text.config(text=f"Humidity: {humidity_value} %")

            wind_speed_value = response.json()['wind']['speed']
            wind_speed_text.config(text=f"Wind Speed: {wind_speed_value} m/s")

            sunrise = time.ctime(int(response.json()['sys']['sunrise']))
            sunrise_time = sunrise.split(" ")[4]
            d = datetime.strptime(sunrise_time, "%H:%M:%S")
            time_in_12 = d.strftime("%I:%M:%S %p")
            sunrise_text.config(text=f"Sunrise: {time_in_12}")

            sunset = time.ctime(int(response.json()['sys']['sunset']))
            sunset_time = sunset.split(" ")[4]
            sunset_d = datetime.strptime(sunset_time, "%H:%M:%S")
            sunset_time_in_12 = sunset_d.strftime("%I:%M:%S %p")
            sunset_text.config(text=f"Sunset: {sunset_time_in_12}")


window = Tk()
window.title("Weather app")
window.config(padx=50, pady=50)
window.geometry("1500x700")

canvas = Canvas(width=1000, height=500)
logo = PhotoImage(file="weather-icon-png-11072.png")
canvas.create_image(250, 250, image=logo)
canvas.grid(row=0, column=0, rowspan=8, columnspan=2)

sky_text = Label(text="Sky:- - -", font=("Arial", 22, "bold"))
sky_text.place(x=550, y=200)

location = Label(text="Your Location:- - -", font=("Arial", 22, "bold"))
location.place(x=550, y=00)

pressure_text = Label(text="Atmospheric Pressure:- - -", font=("Arial", 22, "bold"))
pressure_text.place(x=950, y=200)

average_temp_text = Label(text="Average Temperature:- - -", font=("Arial", 22, "bold"))
average_temp_text.place(x=550, y=300)

humidity_text = Label(text="Humidity:- - -", font=("Arial", 22, "bold"))
humidity_text.place(x=550, y=400)

wind_speed_text = Label(text="Wind Speed:- - -", font=("Arial", 22, "bold"))
wind_speed_text.place(x=950, y=400)

sunrise_text = Label(text="Sunrise:- - -", font=("Arial", 22, "bold"))
sunrise_text.place(x=550, y=500)

sunset_text = Label(text="Sunset:- - -", font=("Arial", 22, "bold"))
sunset_text.place(x=950, y=500)

city_name = Label(text="City:", font=("Arial", 22, "bold"))
city_name.place(x=0, y=500)

my_name = Label(text="Made by Achyut Jadhav", font=("Arial", 12, "bold"))
my_name.place(x=1200, y=600)

location_entry = Entry(width=27, font=("Arial", 22, "bold"))
location_entry.focus()
location_entry.place(x=0, y=550)

search_button = Button(text="Search", font=("Arial", 15, "bold"), command=search_location)
search_button.place(x=423, y=550)

window.mainloop()
