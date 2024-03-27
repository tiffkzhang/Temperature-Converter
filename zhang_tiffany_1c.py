f = float(input("Enter a temperature in degrees Fahrenheit: ")) # f is fahrenheit

c = (f - 32) * 5/9
k = c + 273.15
r = f + 459.67

print("\n", f, "° F ...", "\n", sep="")
print("... in Celsius", format(c,'>26,.2f'), "°C", sep="")
print("... in Kelvin ", format(k,'>26,.2f'), "°K", sep="")
print("... in Rankine", format(r,'>26,.2f'), "°R", sep="")

# syntax error, having more than two arguments in the format function
# semantic error, the formula for k is incorrect, instead of +273.15 the user typed +274.15
# runtime error, the second format argument is incorrect