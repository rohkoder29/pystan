import sys

print("WELCOME TO THE CURRENCY CONVERTER APP\n")

MENU = """
Chose an option:
1. EUR >> USD
2. USD >> EUR
3. USD >> ARS
4. ARS >> USD
5. EUR >> ARS
6. ARS >> EUR
7. QUIT

>>>>>>>> """

# exchange rates
EUR_TO_USD = 1.1804011
USD_TO_EUR = 0.847064
USD_TO_ARS = 96.436852
ARS_TO_USD = 0.010364229
EUR_TO_ARS = 113.89184
ARS_TO_EUR = 0.0087804635


# control whether user selects valid option
def validate_option_input(option):
    while isinstance(option, (int, float, str)):
        option = int(option)
        if option not in range(1, 8):
            print("ERROR. Plase select an option between 1 and 7.")
            option = input(MENU)
        break
    return option


# control whether user puts a numer as amount
def validate_amount_input(amount):
    while not isinstance(amount, (int, float, str)):
        print("ERROR. Amount must be a number.")
        amount = input("Input the amount: ")
    return float(amount)


# convert EUR to USD
def eur_usd(amount):
    change = amount * EUR_TO_USD
    print(f"{amount:.2f} EUR equals to {change:.2f} USD.")
    return change


# convert USD to EUR
def usd_eur(amount):
    change = amount * USD_TO_EUR
    print(f"{amount:.2f} USD equals to {change:.2f} EUR.")
    return change


# convert USD to ARS
def usd_ars(amount):
    change = amount * USD_TO_ARS
    print(f"{amount:.2f} USD equals to {change:.2f} ARS.")
    return change


# convert ARS to USD
def ars_usd(amount):
    change = amount * ARS_TO_USD
    print(f"{amount:.2f} ARS equals to {change:.2f} USD.")
    return change


# convert EUR to ARS
def eur_ars(amount):
    change = amount * EUR_TO_ARS
    print(f"{amount:.2f} EUR equals to {change:.2f} ARS.")
    return change


# convert ARS to EUR
def ars_eur(amount):
    change = amount * ARS_TO_EUR
    print(f"{amount:.2f} ARS equals to {change:.2f} EUR.")
    return change


# put all fonctions in a list
exchange = [eur_usd, usd_eur, usd_ars, ars_usd, eur_ars, ars_eur]


# main program loop
while True:
    option = input(MENU)
    o_p = validate_option_input(option)
    if o_p in range(1, 7):
        amount = input("Input the amount: ")
        money = validate_amount_input(amount)
        exchange[o_p - 1](money)
    else:
        print("See you soon, amigo!")
        sys.exit()
