from tkinter import *
from tkinter import ttk
import requests

def dataget():
    city = city_name.get()
    api_key = "bc03fe63fe5b9d1c31712896d7e4d9cd"  
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP request errors
        data = response.json()
        
        w_label1.config(text=data["weather"][0]["main"])
        wd_label1.config(text=data["weather"][0]["description"])
        temp1_label.config(text=int(data["main"]["temp"] - 273.15)) 
        p1_label.config(text=data["main"]["pressure"])
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        w_label1.config(text="Error")
        wd_label1.config(text="")
        temp1_label.config(text="")
        p1_label.config(text="")
    
    except KeyError:
        print("Error: City not found or unexpected response format.")
        w_label1.config(text="City not found")
        wd_label1.config(text="")
        temp1_label.config(text="")
        p1_label.config(text="")
     
    #  city = city_name.get()
    #  data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=bca2f894a25fc7b1073760c23a4fed38").json()
    #  w_label1.config(text = data["weather"][0]["main"])
    #  wd_label1.config(text = data["weather"][0]["description"])
    #  temp1_label.config(text = str(int(data["main"]["temp"]-273.15)))
    #  p1_label.config(text = data["main"]["pressure"])




win = Tk() 
win.title("WEATHER APP")
win.config(bg = "lightblue")
win.geometry("500x500")

name_label = Label(win, text = ("WEATHER APP"), font = ("Time New Roman", 20 ,"bold") )
name_label.place(x=25, y=50, height= 50, width=450)

city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win, text = ("Weather App"),values= list_name , font = ("Time New Roman", 20 ,"bold"), textvariable=city_name)

com.place(x=25, y=120, height= 50, width=450)


w_label = Label(win, text = ("Weather Climate"), font = ("Time New Roman", 13) )
w_label.place(x=70, y=260, height= 41, width=180)
w_label1 = Label(win, text = (""), font = ("Time New Roman", 13) )
w_label1.place(x=260, y=260, height= 41, width=180)

wd_label = Label(win, text = ("Weather Description"), font = ("Time New Roman", 11) )
wd_label.place(x=70, y=310, height= 41, width=180)
wd_label1 = Label(win, text = (""), font = ("Time New Roman", 13) )
wd_label1.place(x=260, y=310, height= 41, width=180)

temp_label = Label(win, text = ("Temperature"), font = ("Time New Roman", 13) )
temp_label.place(x=70, y=360, height= 41, width=180)
temp1_label = Label(win, text = (""), font = ("Time New Roman", 13) )
temp1_label.place(x=260, y=360, height= 41, width=180)

p_label = Label(win, text = ("Pressure"), font = ("Time New Roman", 13) )
p_label.place(x=70, y=410, height= 41, width=180)
p1_label = Label(win, text = (""), font = ("Time New Roman", 13) )
p1_label.place(x=260, y=410, height= 41, width=180)

done_button = Button(win, text = ("Done"), font = ("Time New Roman", 20 ,"bold"), command = dataget)
done_button.place(y=190, height = 40 , width =120 , x=200)


win.mainloop()