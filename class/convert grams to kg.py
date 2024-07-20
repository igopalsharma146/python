# Function to convert grams to kilograms
def grams_to_kilograms(grams):
    return grams / 1000

# Input from the user
grams = float(input("Please enter the weight in grams: "))

# Conversion
kilograms = grams_to_kilograms(grams)

# Output the result
print(f"{grams} grams is equal to {kilograms} kilograms")
