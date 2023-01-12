from date import date

dateType = str(type(date))

dateLen = len(dateType)

if (dateLen == 27):
	print('test1 pass')

print (dateLen)


if (dateType == "<class 'datetime.datetime'>"):
	print('test2 pass')


print(dateType)

print(date)

