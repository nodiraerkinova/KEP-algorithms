def month_to_season(month):
    if month == 3 or month == 4 or month == 5:
     return "bahor"
    elif month == 6 or month == 7 or month == 8:
        return "yoz"
    elif month == 9 or month == 10 or month == 11:
       return 'kuz'
    elif month == 12 or month == 1 or month == 2:
       return "qish"
print(month_to_season(4))