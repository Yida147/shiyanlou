#!/usr/bin/env python3

import sys

tax_after = 0
try:
    wage = float(sys.argv[1])
except:
    print('Parameter Error')
if  wage >= 3500:    
    tax_before = wage - 3500
    if tax_before <= 1500:
        tax_after = tax_before*0.03
    elif tax_before > 1500 and tax_before <= 4500:
        tax_after = tax_before*0.1 - 105
    elif tax_before > 4500 and tax_before <= 9000:
        tax_after = tax_before*0.2 - 555
    elif tax_before > 9000 and tax_before <= 35000:
        tax_after = tax_before*0.25 - 1005
    elif tax_before > 35000 and tax_before <= 55000:   
        tax_after = tax_before*0.3 - 2755
    elif tax_before > 55000 and tax_before <= 80000:   
        tax_after = tax_before*0.35 - 5505
    else:
        tax_after = tax_before*0.45 - 13505
else:
    tax_after = wage
print('{:.2f}'.format(tax_after))
