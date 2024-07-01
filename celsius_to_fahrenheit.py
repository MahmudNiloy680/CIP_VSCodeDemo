def convert_C_to_F(temp_in_celsius):
    temp_in_fahrenheit = (temp_in_celsius * 1.8) + 32
    return temp_in_fahrenheit


temp_in_C = float(input("Enter Temperature in Celsius: "))
temp_in_F = convert_C_to_F(temp_in_C)

print(f"{temp_in_C} degree celsius is {temp_in_F} degree in fahrenheit")
