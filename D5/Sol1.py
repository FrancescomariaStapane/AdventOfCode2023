file = open("input.txt", "r")
lines = file.readlines()

seeds = lines[0][7:-1].split(" ")
seed_to_soil=[]
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []


def parseMap(lines_, line_index, map):
    while len((lines[line_index])) > 1:
        map.append(lines[line_index][:-1].split(" "))
        line_index += 1
    line_index += 2
    return line_index


line_index = 3
line_index = parseMap(lines, line_index, seed_to_soil)
line_index = parseMap(lines, line_index, soil_to_fertilizer)
line_index = parseMap(lines, line_index, fertilizer_to_water)
line_index = parseMap(lines, line_index, water_to_light)
line_index = parseMap(lines, line_index, light_to_temperature)
line_index = parseMap(lines, line_index, temperature_to_humidity)
line_index = parseMap(lines, line_index, humidity_to_location)
print(seed_to_soil)
print(soil_to_fertilizer)
print(fertilizer_to_water)
print(water_to_light)
print(light_to_temperature)
print(temperature_to_humidity)
print(humidity_to_location)
