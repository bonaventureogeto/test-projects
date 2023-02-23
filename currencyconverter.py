def currency_converter(from_currency,to_currency,amount):
    if from_currency == "usd" and to_currency == "ksh":
        conv_rate = 112.50
        ksh = (amount * conv_rate)
        print ksh
    
    elif from_currency == "eur" and to_currency == "ksh":
        conv_rate = 132.45
        ksh = (amount * conv_rate)
        print ksh
    
    elif from_currency == "eur" and to_currency == "usd":
        conv_rate = 1.20
        usd = (amount * conv_rate)
        print usd

    else:
        print("Currency not available")

currency_converter("jap","ksh",20)