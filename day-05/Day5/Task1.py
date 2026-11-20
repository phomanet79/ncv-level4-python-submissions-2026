class product:
    def __init__(self,product_Id,product_Name,price):
       self.product_Id = product_Id,
       self.price = price
       
       if len(product_Name) > 10:
           raise ValueError("Chacter length cannot be greater than 10")
       
       self.product_Name= product_Name
 
def total_price(product1, product2):
 total = product1.price + product2.price
 return total
 
def win_price(product1, product2):
    if total_price(product1,product2) > 5000:
     return "You have won a laptop bag"
    else:
     return "Sorry you didn't win"   

        
product1 = product("2024001","Laptop",5000)
product2 = product("2024002", "Charger", 950)
print(product1.product_Id, product1.product_Name,product1.price)
print(product2.product_Id, product2.product_Name,product2.price)
print(f'TOTAL PRODUCT : R{total_price(product1,product2)}') 
print(win_price(product1,product2))