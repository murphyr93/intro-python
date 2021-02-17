print("This program calculates how long it takes for an investment to double in size.")

investment = 1000
rate = input("Please enter the annual interest rate: ")
years = 0
value = investment
 
while value <= investment * 2 :
    value = value + value * float(rate)/100
    years = years + 1

print("At", rate, "% interest your investment doubles in", years, "years")