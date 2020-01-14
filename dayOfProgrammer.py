def dayOfProgrammer(year):
    if year == 1918:
        return("26.09.1918")
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 !=0 and year >= 1918:
            return("13.09."+str(year))
        else:
            return("12.09."+str(year))
    else:
        return("13.09."+str(year))
print(dayOfProgrammer(2019))
