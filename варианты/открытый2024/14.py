f = 2 * (729**2014) + 2 * (243**2016) - 2 * (81**2018) + 2 * (27**2020) - 2 * (9**2022) - 2024
k = 0
while f > 0:
    if f % 27 > 9:
        k = k + 1
    f = f // 27
print(k)