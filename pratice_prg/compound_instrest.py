priciple = 0
rate = 0
time = 0
while priciple <=0:
   priciple = float(input("Enter the principle amount: "))
   if priciple <= 0:
      print("principle can't be less than or equal to zero")
while rate <=0:
   rate = float(input("Enter the rate: "))
   if rate <= 0:
      print("rate can't be less than or equal to zero")
while time <=0:
   time = float(input("Enter the time: "))
   if time <= 0:
      print("time can't be less than or equal to zero")
total = priciple * pow((1 + rate / 100), time )
print(f"Balance afer {time} year/s: ${total:.2f}")