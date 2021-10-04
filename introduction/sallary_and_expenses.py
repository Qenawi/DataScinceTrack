from collections import defaultdict

salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

sal_by_tens = defaultdict(list)
for sal, tenures in salaries_and_tenures:
    sal_by_tens[tenures].append(sal)
# print(sal_by_tens)

sal_by_tens_bucket = defaultdict(list)


def tens_bucket(ten):
    if ten < 2:
        return "- 2"
    elif ten < 5:
        return "+ 2"
    else:
        return "+ 5"


for sal, ten in salaries_and_tenures:
    buck = tens_bucket(ten)
    sal_by_tens_bucket[buck].append(sal)

avg = {tm: sum(sal) / len(sal) for tm, sal in sal_by_tens_bucket.items()}

print(avg)
