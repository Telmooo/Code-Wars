order_weight = lambda st: " ".join(sorted(st.split(), key=lambda x: (sum(map(int, str(x))), x)))
