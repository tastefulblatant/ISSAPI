import requests
from tkinter import *
import customtkinter
from PIL import Image
#window
window = customtkinter.CTk()
window.resizable(False, False)
window.geometry("700x400")
window.title("ISS")
window.iconbitmap("icon.ico")
customtkinter.set_appearance_mode("dark")

#Functions
def iss_coordinates():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    latitude = data["iss_position"]["latitude"]
    longitude = "The height is: " + data["iss_position"]["longitude"]

    latitude_label.configure(text=f"The latitude of the ISS is {latitude}")
    longitude_label.configure(text=f"The longitude of the ISS is {longitude}")

#Canva
my_image = customtkinter.CTkImage(dark_image=Image.open("iss_gif.gif"),
                                  size=(480,270))
image_label = customtkinter.CTkLabel(window, image=my_image, text="")
image_label.pack()

#Frame 
coordinates_frame = customtkinter.CTkFrame(window)
coordinates_frame.pack()

#Button
recount_button = customtkinter.CTkButton(coordinates_frame, text="Current ISS coordinates", command=iss_coordinates)
recount_button.pack()

#Labels
latitude_label = customtkinter.CTkLabel(window, text="")
latitude_label.pack()

longitude_label = customtkinter.CTkLabel(window, text="")
longitude_label.pack()


#mainloop
window.mainloop()