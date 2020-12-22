f = open('./집콕키워드.txt')

y_20_12 = 0
y_20_11 = 0
y_20_10 = 0
y_20_09 = 0
y_20_08 = 0
y_20_07 = 0
y_20_06 = 0
y_20_05 = 0
y_20_04 = 0
y_20_03 = 0
y_20_02 = 0
y_20_01 = 0
y_19_12 = 0
y_19_11 = 0
y_19_10 = 0
y_19_09 = 0
y_19_08 = 0
y_19_07 = 0
y_19_06 = 0
y_19_05 = 0
y_19_04 = 0
y_19_03 = 0
y_19_02 = 0
y_19_01 = 0

while(True):
    line = f.readline()
    if(line == ''):
        break
    month = line.split()[0]
    year = line.split()[2]
    if(year == '2020'):
        if(month == 'December'):
            y_20_12 += 1
        elif(month == 'November'):
            y_20_11 += 1
        elif (month == 'October'):
            y_20_10 += 1
        elif (month == 'September'):
            y_20_09 += 1
        elif (month == 'August'):
            y_20_08 += 1
        elif (month == 'July'):
            y_20_07 += 1
        elif (month == 'June'):
            y_20_06 += 1
        elif (month == 'May'):
            y_20_05 += 1
        elif (month == 'April'):
            y_20_04 += 1
        elif (month == 'March'):
            y_20_03 += 1
        elif (month == 'February'):
            y_20_02 += 1
        elif (month == 'January'):
            y_20_01 += 1
    elif(year == '2019'):
        if (month == 'December'):
            y_19_12 += 1
        elif (month == 'November'):
            y_19_11 += 1
        elif (month == 'October'):
            y_19_10 += 1
        elif (month == 'September'):
            y_19_09 += 1
        elif (month == 'August'):
            y_19_08 += 1
        elif (month == 'July'):
            y_19_07 += 1
        elif (month == 'June'):
            y_19_06 += 1
        elif (month == 'May'):
            y_19_05 += 1
        elif (month == 'April'):
            y_19_04 += 1
        elif (month == 'March'):
            y_19_03 += 1
        elif (month == 'February'):
            y_19_02 += 1
        elif (month == 'January'):
            y_19_01 += 1

print(y_19_01,y_19_02,y_19_03,y_19_04,y_19_05,y_19_06,y_19_07,y_19_08,y_19_09,y_19_10,y_19_11,y_19_12)
print(y_20_01,y_20_02,y_20_03,y_20_04,y_20_05,y_20_06,y_20_07,y_20_08,y_20_09,y_20_10,y_20_11,y_20_12)