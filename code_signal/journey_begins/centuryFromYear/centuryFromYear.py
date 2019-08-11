def centuryFromYear(year):
    if ((year > 0) and (year <= 2005)):
        century = str(year)
        return century
    else:
        return "This is not a valid year. Please try again."
      
print(centuryFromYear(1905))  # should print "20"