from lib.date import DateCalculator, DateAdapter

a = DateCalculator.get_next_tuesday()
b = DateCalculator.get_next_thursday()

print(DateAdapter(date=a).start())
print(DateAdapter(date=a).finish())

print()

print(DateAdapter(date=b).start())
print(DateAdapter(date=b).finish())