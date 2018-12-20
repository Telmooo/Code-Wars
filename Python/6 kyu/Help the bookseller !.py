def stock_list(listOfArt, listOfCat):
    st = []
    dif0 = False
    for letter in listOfCat:
        t = 0
        for book in listOfArt:
            if letter == book[0]:
                t += int(book.split()[1])
        st.append(f"{letter} : {t}")
        if t!=0: dif0 = True
    return " - ".join(f"({s})" for s in st) if dif0 else ""
