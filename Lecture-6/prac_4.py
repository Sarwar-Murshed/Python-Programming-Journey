# WAF to convert USD to BDT

usd = int(input("Enter $ = "))

def converter(usd_value):
    bdt = 120 * usd_value
    print(usd_value,"$ = ",bdt,"tk") 


converter(usd)