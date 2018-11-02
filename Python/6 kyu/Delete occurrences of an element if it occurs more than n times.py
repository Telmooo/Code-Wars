def delete_nth(order,max_e):
    l = []
    for i in order:
        if l.count(i) < max_e:
            l.append(i)
    return l
