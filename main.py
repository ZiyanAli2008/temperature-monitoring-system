# Temperature Monitoring System
# Simulates, stores, and analyzes temperature readings
# Created by Ziyan Ali

import random

global temperatures
temperatures = []
possible_Changes = [-5,-4,-4,-3,-3,-3,-2,-2,-1,0,1,2,2,3,3,3,4,4,5]

def load_data():
    '''Clear the current temperature list and load all temperatures from the file onto the list'''
    temperatures.clear()
    try:
        input_file = open("April 16th/temps.txt", "r")
        stringTemps = input_file.readlines()
        for temp in stringTemps:
            temperatures.append(float(temp))
    except FileNotFoundError:
        pass

def save_data():
    '''Take all the temperatures from the current temperature list and add them to the temperature file'''
    output_file = open("April 16th/temps.txt", "w")
    for i in range(len(temperatures)):
        output_file.write(f"{temperatures[i]}\n")

def look_for_trend(a, b):
    '''Look to see if any trend occurs in simulation or manually adding input values'''
    return (b > a), (a > b), (abs(b-a) >= 5)

def parse_temperature_input(prompt):
    '''Make sure input values are valid inputs'''
    while True:
        value = input(prompt)

        if len(value) == 0:
            print("Please enter a valid input \n")
            continue
        if value[-1].upper() == "Q":
            return None, "Q"

        try:
            unit = value[-1].upper()
            temperature = float(value[:-1])
        except:
            print("Please enter a valid input \n")
            continue

        if unit not in ["F", "C"]:
            print("Please enter a valid input \n")
            continue

        return temperature, unit


running = True
while running:

    while True:
        option = input("1 -> Manual Input\n2 -> Simulate 10 readings\n3 -> View data\n4 -> Average\n5 -> Max/Min\n6 -> Save data\n7 -> Load data\n8 -> Exit\n")
        if option not in ["1","2","3","4","5","6","7","8"]:
            print("Please enter a valid option\n")
            continue
        else:
            break

    option = int(option)
            
    if len(temperatures) > 50:
        temperatures.pop(0)
    
    if option == 1:
        temperature, unit = parse_temperature_input("Enter temperature (e.g., 100F or 37C): ")
        if unit == "C":
            temperatures.append(temperature)
        else:
            temperature = (temperature - 32) * (5/9)
            temperatures.append(temperature)
        if len(temperatures) >= 2:
            inc, dec, spike = look_for_trend(temperatures[-2], temperatures[-1])
            if spike:
                print("Temperature Spike")
            elif inc:
                print("Temperature Increasing")
            elif dec:
                print("Temperature Decreasing")
    elif option == 2:
        for i in range(10):
            if len(temperatures) == 0:
                temperatures.append(random.uniform(20,30))
            else:
                temperatures.append(temperatures[-1] + random.choice(possible_Changes))

            if len(temperatures) > 1:
                inc, dec, spike = look_for_trend(temperatures[-2], temperatures[-1])
                if spike:
                    print("Spike detected during simulation")
    elif option == 3:
        if len(temperatures) == 0:
            print("No readings available")
        else:
            for i in range(len(temperatures)):
                print(f"Reading {i+1}: {temperatures[i]:.2f}C")
    elif option == 4:

        if len(temperatures) > 0:
            print(f"Average: {sum(temperatures)/len(temperatures)}")
        else:
            print("Not enough readings")
    elif option == 5:
        if len(temperatures) > 0:
            print(f"Maximum: {max(temperatures)}")
            print(f"Minimum: {min(temperatures)}")    
        else:
            print("Not enough readings")
    elif option == 6:
        if len(temperatures) == 0:
            print("No available readings")
        else:
            save_data()
    elif option == 7:
        if len(temperatures) != 0:
            loadData = input("Current data will be deleted, type Q to cancel")
            if (loadData.upper() != "Q"):
                load_data()
            else:
                print("Function evaded")
        else:
            load_data()
        
    elif option == 8:
        running = False
