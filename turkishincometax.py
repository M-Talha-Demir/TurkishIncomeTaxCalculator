"""Turkish income Tax Price List 2022
Gelir dilimleri                                                                             Vergi oranı (%)

0-32.000        Money%15                                                                            15

32.000-70.000   (32000%15) + (Money-32000)%20                                                       20

70.000-170.000  (32000%15) + (38000%20) +(Money-70000)%27                                           27

170.000-880.000 (32000%15) + (38000%20) + (100000%27) + (Money-170000)%35                           35

880.000-        (32000%15) + (38000%20) + (100000%27) + (710000%35) + (Money-880000)%40             40

"""


def incomeTax(money):
    if money > 32000:
        taxes = (32000 * 15)
        if money > 70000:
            taxes += (38000 * 20)
            if money > 170000:
                taxes += (100000 * 27)
                if money > 880000:
                    taxes += (710000 * 35) + ((money - 880000) * 40)
                else:
                    taxes += ((money - 170000) * 35)
            else:
                taxes += ((money - 70000) * 27)
        else:
            taxes += ((money - 32000) * 20)
        return taxes / 100
    else:
        return money * 15 / 100


def printTax(grosIncome):
    tax = int(incomeTax(grosIncome))
    left = int(31900 - tax)
    print(f"Tax for 31900 TL income {tax}, Salary remaining after deduction of income tax is {income}")

incomes = [31900, 32000, 32100, 70000, 70100, 170000, 170100, 880000, 880100]

for income in incomes:
    printTax(income)
