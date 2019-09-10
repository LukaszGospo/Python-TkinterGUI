import  tkinter as tk
import requests

# 54d19948b19d8119c5cab93b62469e81

HEIGHT = 500
WIDTH = 600

def test_function(entry):
    print("This is the entry: ", entry)

def get_weather(city):
    weather_key = '54d19948b19d8119c5cab93b62469e81'
    url = 'https://api.openweathermap.org/data/2.5/forecast'
    params = {'APPID': weather_key, 'q' : city, 'units' : 'imperial'}
    response = requests.get(url, params=params)
    print(response.json())

root = tk.Tk()

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file = 'landscape.png')
background_label = tk.Label(root, image = background_image)
background_label.place(relwidth = 1, relheight = 1)

frame = tk.Frame(root, bg = '#33c4ff', bd = 5)
frame.place(relwidth = 0.75, relheight = 0.1, relx= 0.5, rely = 0.1, anchor = 'n')

entry = tk.Entry(frame, bg = 'green', font = 40)
#entry.grid(row = 0, column = 2)
entry.place(relwidth = 0.65, relheight = 1)

button = tk.Button(frame, text = "Get Weather", bg = 'yellow', fg = 'red', font = 40, command = lambda: get_weather(entry.get()))
button.place(relx = 0.7, rely = 0,  relwidth= 0.3, relheight = 1)

lower_frame = tk.Frame(root, bg = '#33c4ff', bd = 10)
lower_frame.place(relwidth = 0.75, relheight = 0.6, relx= 0.5, rely = 0.25, anchor = 'n')


label = tk.Label(lower_frame)
label.place(relwidth = 1, relheight = 1)




root.mainloop()