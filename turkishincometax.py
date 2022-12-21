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
        if money > 70000:
            if money > 170000:
                if money > 880000:
                    return ((32000 * 15) + (38000 * 20) + (100000 * 27) + (710000 * 35) + ((money - 880000) * 40)) / 100
                else:
                    return ((32000 * 15) + (38000 * 20) + (100000 * 27) + ((money - 170000) * 35)) / 100
            else:
                return ((32000 * 15) + (38000 * 20) + ((money - 70000) * 27)) / 100
        else:
            return ((32000 * 15) + ((money - 32000) * 20)) / 100
    else:
        return money * 15 / 100


print(f"Tax for 31900 TL income {int(incomeTax(31900))}, Salary remaining after deduction of income tax is {int(31900-incomeTax(31900))}")
print(f"Tax for 32000 TL income {int(incomeTax(32000))}, Salary remaining after deduction of income tax is {int(32000-incomeTax(32000))}")
print(f"Tax for 32100 TL income {int(incomeTax(32100))}, Salary remaining after deduction of income tax is {int(32100-incomeTax(32100))}")
print(f"Tax for 70000 TL income {int(incomeTax(70000))}, Salary remaining after deduction of income tax is {int(70000-incomeTax(70000))}")
print(f"Tax for 70100 TL income {int(incomeTax(70100))}, Salary remaining after deduction of income tax is {int(70100-incomeTax(70100))}")
print(f"Tax for 170000 TL income {int(incomeTax(170000))}, Salary remaining after deduction of income tax is {int(170000-incomeTax(170000))}")
print(f"Tax for 170100 TL income {int(incomeTax(170100))}, Salary remaining after deduction of income tax is {int(170100-incomeTax(170100))}")
print(f"Tax for 880000 TL income {int(incomeTax(880000))}, Salary remaining after deduction of income tax is {int(880000-incomeTax(880000))}")
print(f"Tax for 880100 TL income {int(incomeTax(880100))}, Salary remaining after deduction of income tax is {int(880100-incomeTax(880100))}")
