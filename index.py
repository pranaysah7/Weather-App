from cProfile import label
from cgitb import text
from distutils.text_file import TextFile
from email.mime import image
from enum import Flag
import json
from msilib.schema import Condition
from re import search
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root=Tk()
root.title("WEATHER APP")
root.geometry("900x500+300+200")
root.resizable(False,False)

def getWeather():
    try:
        city=textfield.get()
        geolocator=Nominatim(user_agent="geoapiExercises")
        location=geolocator.geocode(city)
        obj=TimezoneFinder()
        result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
        print(result)

        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=05fd0550c88e3b4566ed10a723b3ca0c"
        json_data=requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description=json_data['weather'][0]['description']
        temp=int(json_data['main']['temp']-273.15)
        pressure=json_data['main']['pressure']
        humidity=json_data['main']['humidity']
        wind=json_data['wind']['speed']

        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
    except Exception as e:
        messagebox.showerror("Weather App","INVALID!!")

Search_image=PhotoImage(file="search.png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()

Searchicon=PhotoImage(file="search_icon.png")
myimage_icon=Button(image=Searchicon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
myimage_icon.place(x=400,y=34)

logo_image=PhotoImage(file="logo.png")
logo1=Label(image=logo_image)
logo1.place(x=150,y=100)

#bottom box
Frame_image=PhotoImage(file="box.png")
Frame_myimage=Label(image=Frame_image)
Frame_myimage.pack(padx=5,pady=5,side=BOTTOM)
#time
name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)


#label part
label1=Label(root,text="WIND",font=("Helvetica",16,'bold'),fg="white",bg="#1ab5ef")
label1.place(x=120,y=400)

label2=Label(root,text="HUMIDITY",font=("Helvetica",16,'bold'),fg="white",bg="#1ab5ef")
label2.place(x=250,y=400)

label3=Label(root,text="DESCRIPTION",font=("Helvetica",16,'bold'),fg="white",bg="#1ab5ef")
label3.place(x=430,y=400)

label4=Label(root,text="PRESSURE",font=("Helvetica",16,'bold'),fg="white",bg="#1ab5ef")
label4.place(x=650,y=400)

t=Label(font=("ariel",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15,"bold"))
c.place(x=400,y=250)

w=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)
h=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=280,y=430)
d=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=450,y=430)
p=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=670,y=430)


root.mainloop()
