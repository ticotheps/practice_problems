def centuryFromYear(year):
    if ((year > 0) and (year <= 2005)):
        str_year = str(year)  # converts integer input to string type with 'str()'
        len_year = len(str_year)  # finds length of new 'str_year'
        century_arr = []
        century = 0
        # iterates through 'str_year'...
        for digit in range(len_year):
            # appends each digit from 'str_year' to century_arr
            century_arr.append(str_year[digit])
        if len_year == 1:
            century += 1
        if len_year == 2:
            century += 1
        if len_year == 3:
            if ((century_arr[1] == '0') and (century_arr[2] == '0')):
                century = int(century_arr[0])
            else:
                century = int(century_arr[0]) + 1
        if len_year == 4:
            if ((century_arr[2] == '0') and (century_arr[3] == '0')):
                century = int(century_arr[0] + century_arr[1])
            else:
                century = int(century_arr[0] + century_arr[1]) + 1
        return century
    else:
        return "This is not a valid year. Please try again."
  

print(centuryFromYear(1905))  # should print "20"
print(centuryFromYear(12))  # should print "1"
print(centuryFromYear(195))  # should print "2"
print(centuryFromYear(2005))  # should print "21"
print(centuryFromYear(2035))  # should print "This is not a valid year. Please try again."
print(centuryFromYear(1700))  # should print "17"
print(centuryFromYear(45))  # should print "1"