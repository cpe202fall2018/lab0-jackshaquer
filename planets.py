# Lab0
# Name: Jack Shaquer
# Instructor: Paul Hatalsky
# Section: 05

def weight_on_planets():
   weight = float(input("What do you weigh on earth? "))
   print("\n" + "On Mars you would weigh " + format(.38 * weight, ".2f") + " pounds." + "\n" +
         "On Jupiter you would weigh " + format(2.34 * weight, ".2f") + " pounds.")

if __name__ == '__main__':
   weight_on_planets()