"""
    7) An atm contains indian currency notes of 100,500,1000. To withdraw cash from this atm the user has to enter the number of notes.he or she want each currency of 100,500,1000. write a program to calculate total amount withdrawal by the person from the atm in rupees.
    """
n=eval(input("enter the number of notes, notes should be minimum three:"))
if(n<3):
    print("enter minimum three notes.")
    exit(0)
fh=0
h=0
th=0
for i in range (1,n+1):
    if( i%3==0):
        h=h+1
        continue
    if(i%2!=0):
        fh=fh+1
        continue
    if(i%2==0):
        th=th+1
        continue
s="In there {0} notes , you will gate {1} notes of 100 and {2} notes of 500 and {3} notes of 1000."
print(s.format(n,h,fh,th))
total=h*100+fh*500+th*1000
s="total amount withdrawal by the person from the atm in rupees is:{0}"
print(s.format(total))

# Function to calculate total withdrawal amount
def calculate_total_withdrawal(notes_100, notes_500, notes_1000):
    total_amount = (notes_100 * 100) + (notes_500 * 500) + (notes_1000 * 1000)
    return total_amount

# Input: Number of notes for each denomination
notes_100 = int(input("Enter the number of 100 INR notes: "))
notes_500 = int(input("Enter the number of 500 INR notes: "))
notes_1000 = int(input("Enter the number of 1000 INR notes: "))

# Calculate total amount
total_amount = calculate_total_withdrawal(notes_100, notes_500, notes_1000)

# Output the total amount
print(f"Total amount withdrawn: {total_amount} INR")
