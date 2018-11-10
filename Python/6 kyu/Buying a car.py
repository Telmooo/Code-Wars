def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    months = 0
    if startPriceOld < startPriceNew:
        while savingperMonth * months + startPriceOld < startPriceNew:
            months += 1
            percentLossByMonth += 0.5*(months % 2 == 0)
            startPriceOld -= startPriceOld*(percentLossByMonth/100)
            startPriceNew -= startPriceNew*(percentLossByMonth/100)
    return [months, round(startPriceOld + savingperMonth * months - startPriceNew)]
