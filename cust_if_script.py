#!/usr/bin/env python3

user_temp = input('what temperature (in degrees F) is your thermostat set on? ')

if user_temp == "72":
    print('just right')
elif user_temp >= "73":
    print("too hot")
elif user_temp <= "66":
    print("too cold!")
elif user_temp <= "71":
    print("a little cool")
