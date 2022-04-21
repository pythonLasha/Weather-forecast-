from tkinter import *
import requests

root = Tk()


def get_weather():
    city = cityField.get()
    key = '673b437e527764a3f7a70ee33cdc1ddd'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': key, 'q': city, 'units': 'metric'}
    result = requests.get(url, params = params)
    weather = result.json()

    info['text'] = f"{str(weather['name'])}: {weather['main']['temp']}"


root['bg'] = '#E0FFFF'
root.title('Погодное приложение')
root.geometry('300x250')

root.resizable(width=True, height=True)

frame_top = Frame(root, bg='#ffb700', bd=5) # Область для размещения др. обьектов
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25) # его расположение

frame_bottom = Frame(root, bg='#ffb700', bd=5)
frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)

cityField = Entry(frame_top, bg='white', font=30) # Получение данных от пользователя
cityField.pack()

btn = Button(frame_top, text='Посмотреть погоду', command = get_weather)
btn.pack()

info = Label(frame_bottom, text= ' Погодная информация ', bg='#ffb700', font=40)
info.pack()

root.mainloop() # постоянный цикл