usernameInput = input("Username : ")
passwordInput = input("Password : ")

if usernameInput == "Hungry" and passwordInput == "5555" :
  print("Welcome", usernameInput)
  print("-------------Hunger Shop-------------")
  print("These are our Menus :")
  print("Mineral Water       |  20  THB")
  print("Soft Drink          |  25  THB")
  print("Potato Chips        |  50  THB")
  print("Candy Bar           |  15  THB")
  print("Popsicle            |  40  THB")
  order = input("Please choose your order: ")
  if order == "Mineral Water":
    price1 = int(input("Amount      : "))
    print("Total       :", price1*20, "THB")
  elif order == "Soft Drink":
    price2 = int(input("Amount      : "))
    print("Total       :", price2*25, "THB")
  elif order == "Potato Chips":
    price3 = int(input("Amount      : "))
    print("Total       :", price3*50, "THB")
  elif order == "Candy Bar":
    price4 = int(input("Amount      : "))
    print("Total       :", price4*15, "THB")
  elif order == "Popsicle":
    price5 = int(input("Amount      : "))
    print("Total       :", price5*40, "THB")
  print("Thank You And Enjoy!")
  print("--------------------------------------")
else:
  print("Log-in Fail")
  print("Please try again !")
