# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 22:37:27 2019

@author: afzal

Recieved help from PES2201800013 Akshaya. J. with the algorithm
"""


import requests, json
from random import choice
API_key = "727351da20e825b14cb2e83a44ceeeb8"
city_name = input("Enter city name you want:")
url = "http://api.openweathermap.org/data/2.5/weather?appid={}&q={}".format(API_key, city_name)

response_j = requests.get(url) #gets method of requests module
#convert json format data into python format data
response = response_j.json()

if response['weather'][0]['id'] != 404: #the data is given in the form of nested dictionary
    list_data = response['weather'][0]['description'].split(" ")

    kwrds1 = ["clouds", "haze", "rain", "thunderstorm"] 
    kwrds2 = ["scattered", "few"]

    for i in list_data:
        for j in list_data:
            if i in list_data and j in list_data: 
                flag = "Sun"
                break
            elif i in lise_data and j not in list_data:
                flag = "Rain"
                break
            else: flag = "Rain"
    
    if flag == "Rain":
        print("A Possibility of Rainfall - Carry an umbrella")
    elif flag == "Sun":
        out = ["Sunny with High UV - Carry an unbrella and use Sunscreen", "Sunny - Optional umbrella"]
        print(choice(out))
    else:
        print("Moderate weather - Umbrella not needed")
else:
    print("Invalid City")