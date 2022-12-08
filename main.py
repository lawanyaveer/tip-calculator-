#2nd day
# 100 days python bootcamp
#tip clcultor


print("welcome to tip calculator")
total_bill = input("what was the total bill")
tip = input("what percentage tip would you like to give? 10,12,15")
percentage_tip = int(tip)/100
print(percentage_tip)
split = input("how many people to split the bill?")
Each_person_should_pay = (int(total_bill) + int(percentage_tip))/int(split)
final_amount = round(Each_person_should_pay,2)
print(f"Each_person_should_pay{final_amount}")
