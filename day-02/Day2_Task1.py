def amount_due(facility_code, hours):
   #code = ""
   facility_code_list = ["squa", "swim", "gym", "wei"]
   facility =["squash court", "swimming pool", "Gymnasium", "Weights"]
   rates = [13.00,12.00,11.00,8.00]
   
   print("Facility","\t\t","Facility_code","\t","Rate per hour")
   for n in range(len(facility_code_list)):
      print(f'{facility[n]:<30} {facility_code_list[n]:<18} {rates[n]:<8}')
   for n in range(len(facility_code_list)):    
      if  facility_code == facility_code_list[n] :
        return hours * rates[n]
        
   print("invalid facility code")
   return 0              

def final_amount_due(amount):
   VAT = 0.14
   return amount+(amount * VAT)

def display(name,final_amount):
  print(f'Customer name :  {name}')
  print(f'Final Amount :  R{final_amount:.2f}')
  
def process_payment():
  name = input(" Enter the customer name :  ")
  code = input("Enter code : ")
  hours =float(input( "Enter hours: "))
  
  amount = amount_due(code,hours)
  final_amount = final_amount_due(amount)
  display(name,final_amount)
 
process_payment()  