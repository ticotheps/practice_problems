def centuryFromYear(year):
    century_dict = dict()
    century_dict.update({'1': 1, '2': 2, '3': 3,'4': 4,'5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, '11': 11, '12': 12, '13': 13, '14': 14, '15': 15, '16': 16, '17': 17, '18': 18, '19': 19, '20': 20, '21': 21})

    if ((year > 0) and (year <= 2005)):
        # str_year = str(year)
        # len_year = len(str_year)
        # # return str_year
        # century = []
        # if (len_year > 0) and (len_year <= 3):
        #     for digit in range(str_year):
        #       century.append(str_year)
        # elif len_year == 2:
        # elif len_year == 3:
        # else:
        # return(year)
        return(century_dict)
    else:
        return "This is not a valid year. Please try again."
      
      
print(centuryFromYear(1905))  # should print "20"