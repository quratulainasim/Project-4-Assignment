from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import requests

cities_in_pakistan = [
    # Punjab
    "Lahore", "Faisalabad", "Rawalpindi", "Gujranwala", "Multan",
    "Sialkot", "Bahawalpur", "Sargodha", "Sheikhupura", "Gujrat",
    "Jhelum", "Kasur", "Chiniot", "Okara", "Mandi Bahauddin",

    # Sindh
    "Karachi", "Hyderabad", "Sukkur", "Larkana", "Nawabshah",
    "Mirpur Khas", "Shikarpur", "Jacobabad", "Badin", "Thatta",

    # Khyber Pakhtunkhwa (KPK)
    "Peshawar", "Abbottabad", "Mardan", "Swat", "Kohat",
    "Dera Ismail Khan", "Bannu", "Mansehra", "Charsadda", "Nowshera",

    # Balochistan
    "Quetta", "Gwadar", "Turbat", "Khuzdar", "Zhob",
    "Sibi", "Dera Murad Jamali", "Chaman", "Pishin", "Kalat",

    # Azad Jammu & Kashmir (AJK)
    "Muzaffarabad", "Mirpur", "Kotli", "Rawalakot", "Bagh",

    # Gilgit-Baltistan
    "Gilgit", "Skardu", "Hunza", "Chilas", "Ghizer",

    # Islamabad Capital Territory
    "Islamabad"
]


win = Tk()
win.title("Ibtisam Weather App")
win.config(bg="lightblue")
win.geometry("500x500")


def get_weather():
    city = city_combobox.get()  # Get city from dropdown

    if city == "":
        messagebox.showwarning("Input Error", "Please select a city.")
        return

  
    api_key = "5dd905e2f520abc56deb020afa4d0b50"  # Replace with your actual API key
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")


    if response.status_code != 200:
        messagebox.showerror("Error", "City not found or invalid API key.")
        return

    data = response.json()


    temp_kelvin = data["main"]["temp"]
    temp_celsius = temp_kelvin - 273.15
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    weather_description = data["weather"][0]["description"].capitalize()

    result_label.config(text=f"Weather in {city.capitalize()}:\n"
                            f"Temperature: {temp_celsius:.2f}°C\n"
                            f"Humidity: {humidity}%\n"
                            f"Wind Speed: {wind_speed} m/s\n"
                            f"Condition: {weather_description}")


title_label = Label(win, text="Ibtisam Weather App",
                    font=("Time New Roman", 24, "bold"), bg="lightblue")
title_label.pack(pady=10)


city_label = Label(win, text="Select a City:",
                   font=("Arial", 14), bg="lightblue")
city_label.pack(pady=5)

city_combobox = Combobox(win, font=("Arial", 14), width=30, state="readonly")
city_combobox['values'] = cities_in_pakistan  # Set city options
city_combobox.pack(pady=5)


city_combobox.set("Select a city")

search_button = Button(win, text="Get Weather",
                       font=("Arial", 14, "bold"), bg="blue", fg="white",
                       command=get_weather)
search_button.pack(pady=10)

result_label = Label(win, text="",
                     font=("Arial", 14), bg="lightblue", fg="darkgreen")
result_label.pack(pady=20)


footer_label = Label(win, text="Powered by Ibtisam",
                     font=("Arial", 10), bg="lightblue", fg="gray")
footer_label.pack(side="bottom", pady=10)

win.mainloop()
