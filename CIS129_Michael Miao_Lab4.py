# Module 4




def main():
    monthlySales = 0.0  
    storeAmount = 0.0  
    empAmount = 0.0   
    salesIncrease = 0.0  
    monthlySales = getSales("Enter the monthly sales amount: ")
    salesIncrease = getIncrease("Enter the percent of sales increase : ")
    storeAmount = calcStoreBonus(monthlySales)
    empAmount = calcEmpBonus(salesIncrease)
    printBonus(storeAmount, empAmount)

def getSales(prompt):
    monthlySales = float(input(prompt))
    return monthlySales

def calcStoreBonus(monthlySales):
    if monthlySales >= 110000:
        storeAmount = 6000
    elif monthlySales >= 100000:
        storeAmount = 5000
    elif monthlySales >= 90000:
        storeAmount = 4000
    elif monthlySales >= 80000:
        storeAmount = 3000
    else:
        storeAmount = 0
    
    return storeAmount

def getIncrease(prompt):
    salesIncrease = float(input(prompt))
    salesIncrease = salesIncrease / 100  # Convert percentage to decimal
    return salesIncrease

def calcEmpBonus(salesIncrease):
    if salesIncrease >= 0.05:
        empAmount = 75
    elif salesIncrease >= 0.04:
        empAmount = 50
    elif salesIncrease >= 0.03:
        empAmount = 40
    else:
        empAmount = 0
    
    return empAmount

def printBonus(storeAmount, empAmount):
    print("The store bonus amount is $", storeAmount)
    print("The employee bonus amount is $", empAmount)
    
    if (storeAmount == 6000) and (empAmount == 75):
        print('Congrats! You have reached the highest bonus amounts possible!')

main()