#!/usr/bin/python3

import requests
import crayons

astrosjson = 'http://api.open-notify.org/astros.json'

def main():
    gotastros = requests.get(astrosjson)
    astros = gotastros.json()

    inspace = str(astros["number"])
    print("There are currently "+ crayons.green(inspace, bold = True) +" people in space.")

    astronauts = astros["people"]
    for astronaut in astronauts:
        name = astronaut["name"]
        craft = astronaut["craft"]
        print(crayons.green(name, bold = True) + " is on board the craft: " + crayons.green(craft, bold = True))

if __name__ == "__main__":
    main()