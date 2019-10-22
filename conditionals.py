# look at a temperature and figure out what state water is in - solid , liquid or gas

#Set the temperature

temp = int(input("enter a temperature"))

if temp < 4:
	print("water is frozen -  a solid")

elif temp > 4 and temp < 100:
	print("Water is liquid")
elif temp >= 100:
	print("water is gas")

