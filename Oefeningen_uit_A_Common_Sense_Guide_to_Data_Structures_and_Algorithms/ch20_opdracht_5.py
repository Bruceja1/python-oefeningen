# Eigen oplossing
steps = 0
def sort_temperature_readings(array):
    global steps

    list_of_97_readings = []
    list_of_98_readings = []
    list_of_99_readings = []

    for temperature in array:
        if temperature < 98:
            list_of_97_readings.append(temperature)
        
        elif temperature > 97 and temperature < 99:
            list_of_98_readings.append(temperature)
        
        else:
            list_of_99_readings.append(temperature)

        steps+=1

    for i in range(0, 10):
        for j in range(0, len(list_of_97_readings) - 1):
            if list_of_97_readings[j] > list_of_97_readings[j + 1]:
                list_of_97_readings[j], list_of_97_readings[j + 1] = list_of_97_readings[j + 1], list_of_97_readings[j]
        steps+=1

        for j in range(0, len(list_of_98_readings) - 1):
            if list_of_98_readings[j] > list_of_98_readings[j + 1]:
                list_of_98_readings[j], list_of_98_readings[j + 1] = list_of_98_readings[j + 1], list_of_98_readings[j]
        steps+=1

        for j in range(0, len(list_of_99_readings) - 1):
            if list_of_99_readings[j] > list_of_99_readings[j + 1]:
                list_of_99_readings[j], list_of_99_readings[j + 1] = list_of_99_readings[j + 1], list_of_99_readings[j]
        steps+=1
    steps+=1

    return list_of_97_readings + list_of_98_readings + list_of_99_readings

myArray = [98.6, 98.0, 97.1, 99.0, 98.9, 97.8, 98.5, 98.2, 98.0, 97.1]
print(f"{sort_temperature_readings(myArray)} \nThe size of the array is {len(myArray)} and the number of steps taken to sort it was {steps}")

