def centuryFromYear(year):
    # century_dict = dict()
    # century_dict.update({'1': 1, '2': 2, '3': 3,'4': 4,'5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, '11': 11, '12': 12, '13': 13, '14': 14, '15': 15, '16': 16, '17': 17, '18': 18, '19': 19, '20': 20, '21': 21})

    if ((year > 0) and (year <= 2005)):
        # str_year = str(year)
        # len_year = len(str_year)
        century = 0
        # for digit in range(len_year):
        #     print(str_year[digit])
        if (year > 0) and (year <= 100):
            century += 1
        elif (year > 100) and (year <= 200):
            century += 2
        elif (year > 200) and (year <= 300):
            century += 3
        elif (year > 300) and (year <= 400):
            century += 4
        elif (year > 400) and (year <= 500):
            century += 5
        elif (year > 500) and (year <= 600):
            century += 6
        elif (year > 600) and (year <= 700):
            century += 7
        elif (year > 700) and (year <= 800):
            century += 8
        elif (year > 800) and (year <= 900):
            century += 9
        elif (year > 900) and (year <= 1000):
            century += 10
        elif (year > 1000) and (year <= 1100):
            century += 11
        elif (year > 1100) and (year <= 1200):
            century += 12
        elif (year > 1200) and (year <= 1300):
            century += 13
        elif (year > 1300) and (year <= 1400):
            century += 14
        elif (year > 1400) and (year <= 1500):
            century += 15
        elif (year > 1500) and (year <= 1600):
            century += 16
        elif (year > 1600) and (year <= 1700):
            century += 17
        elif (year > 1700) and (year <= 1800):
            century += 18
        elif (year > 1800) and (year <= 1900):
            century += 19
        elif (year > 1900) and (year <= 2000):
            century += 20
        elif (year > 2000) and (year <= 2100):
            century += 21
        return century
    else:
        return "This is not a valid year. Please try again."
  

print(centuryFromYear(1905))  # should print "20"