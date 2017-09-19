# Leslie A Borst
# 9/17/17
# Price of Candy Purchase
# Finding the total price of the candy to be purchased by a customer

# Declair variables

CandyName = str()
WeightLb = int()
WeightOz = int()
TotalPrice = float()
UnitPrice = float()
PricePerLb = float()

# Get inputs from the user

CandyName = str(input('Enter the candy name:'))

PricePerLb = float(input( 'Enter price per pound:'))

WeightLb = int(input('Enter number of pounds:'))

WeightOz = int(input('Enter number of ounces:'))

# Claculate the formulas with user inputs

UnitPrice = PricePerLb / 16
TotalPrice = PricePerLb*(WeightLb + WeightOz / 16)

# Display candy name input and formula results

print('Name of Item:', CandyName)
print('Unit Price: $', UnitPrice)
print('Total Price: $', TotalPrice)
