from datetime import date, timedelta as delta

def date_nb_days(a0, a, p):
    days = 0
    pp = p/36000
    while a0<a:
        a0 += (a0*pp)
        days += 1
    return (date(2016, 1, 1) + delta(days=days)).strftime("%Y-%m-%d")
