#This program will generate how much you have to pay tip

print ("Welcome to tip calculator")
bill = input ("What was total bill? ")
bill = float (bill)


percentage_of_tip = input("What percentage of tip would you like to pay? example 10, 12, or 15  ")
percentage_of_tip = int (percentage_of_tip)
percentage_of_tip /= 100
percentage_of_tip += 1


split_people = input ("How many people split the bills? ")
split_people = int (split_people)

each_person_pay = (bill/split_people) * percentage_of_tip
roundedNumber = round(each_person_pay, 2)

print (f"Each person should pay",format(each_person_pay,".2f"))
