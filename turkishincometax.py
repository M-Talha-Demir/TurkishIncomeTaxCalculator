"""Turkish income Tax Price List 2022
Gelir dilimleri                                                                             Vergi oranı (%)

0-32.000        Money%15                                                                            15

32.000-70.000   (32000%15) + (Money-32000)%20                                                       20

70.000-170.000  (32000%15) + (38000%20) +(Money-70000)%27                                           27

170.000-880.000 (32000%15) + (38000%20) + (100000%27) + (Money-170000)%35                           35

880.000-        (32000%15) + (38000%20) + (100000%27) + (710000%35) + (Money-880000)%40             40

"""

taxBracketDiffs = [(32000, 15), (38000, 20), (100000, 27), (710000, 35)]
incomes = [31900, 32000, 32100, 70000, 70100, 170000, 170100, 880000, 880100]

def incomeTax(money):
    bracketIndex = 0
    taxes = 0
    while money > 0:
        bracket = taxBracketDiffs[bracketIndex]
        if money > bracket[0]:
            taxes += bracket[0] * bracket[1]
            money -= bracket[0]
            bracketIndex += 1
            if bracketIndex >= len(taxBracketDiffs):
                taxes += money * 40
                break
        else:
            taxes += money * bracket[1]
            break
    return taxes / 100


def printTax(grosIncome):
    tax = int(incomeTax(grosIncome))
    netIncome = int(grosIncome - tax)
    print(f"Tax for {grosIncome} TL income {tax}, Salary remaining after deduction of income tax is {netIncome}")


for income in incomes:
    printTax(income)
