def solution(a, b) :
    conversion = {"kg": lambda x: x, "g": lambda x: x / 1000, "mg": lambda x: x / (10 ** 6),
                 "μg": lambda x: x / (10 ** 9), "lb": lambda x: x * 0.453592,
                 "m": lambda x: x, "cm": lambda x: x/100, "mm": lambda x: x / 1000,
                 "μm": lambda x: x / (10 ** 6), "ft": lambda x: x * 0.3048}
    return 6.67 * (10 ** -11) * (conversion[b[0]](a[0]) * conversion[b[1]](a[1])) / (conversion[b[2]](a[2]) ** 2)
