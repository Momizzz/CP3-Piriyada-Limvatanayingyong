usernameInput = input("Username : ")
passwordInput = input("Password : ")

if usernameInput == "Piriyada" and passwordInput == "13579" :
  print("Welcome", usernameInput)
  print("------Hunger Shop------")
  print("These are our Menus :")
  print("Mineral Water  |  20  THB")
  print("Soft Drink     |  25  THB")
  print("Potato Chips   |  50  THB")
  print("Candy Bar      |  15  THB")
  print("Popsicle       |  40  THB")
  order = input("Please choose your order: ")
  if order1 == "Mineral Water":
    price1 = int(input("Amount : "))
  elif order == "Soft Drink":
    price2 = int(input("Amount : "))
  elif order == "Potato Chips":
    price3 = int(input("Amount : "))
  elif order == "Candy Bar":
    price4 = int(input("Amount : "))
  elif order == "Popsicle":
    price5 = int(input("Amount : "))
  print("Total        :", 20*price1 + 25*price2 + 50*price3 + 15*price4 + 40*price5)
  print("Thank You And Enjoy!")
  print("---------------------------------------")
else:
  print("Log-in Fail")
  print("Please try again !")
