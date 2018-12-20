#!/usr/bin/env python3
import sys

def deposable_income(wage):
	social_security = wage*0.165
	taxable = wage - social_security - 3500
	if taxable > 0:
		if taxable <= 1500:
			tax = taxable*0.03
		elif taxable > 1500 and taxable <= 4500:
			tax = taxable*0.1 - 105
		elif taxable > 4500 and taxable <= 9000:
			tax = taxable*0.2 - 555
		elif taxable > 9000 and taxable <= 35000:
			tax = taxable*0.25 - 1005
		elif taxable > 35000 and taxable <= 55000:
			tax = taxable*0.3 - 2755
		elif taxable > 55000 and taxable <= 80000:
			tax = taxable*0.35 - 5505
		else:
			tax = taxable*0.45 - 13505
		deposable_income = wage - tax - social_security
	else:
		deposable_income = wage - social_security
	return '%.2f' % deposable_income

if __name__ == "__main__":
	for item in sys.argv[1:]:
		agent_num , wage = item.split(':')
		try:
			wage = float(wage)
		except ValueError:
			print('Parameter Error')
			continue
		print('{}:{}'.format(agent_num,deposable_income(wage)))
