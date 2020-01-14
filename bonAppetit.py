def bonAppetit(bill, k, b):
    bill.remove(bill[k])
    final_bill = sum(bill)//2
    if final_bill == b:
        print ("Bon Appetit")
    else:
        print(b-final_bill)
n = 10
k = 6
bill = [72, 53, 60, 66, 90, 62, 12, 31, 36, 94]
b = 288

bonAppetit(bill, k, b)