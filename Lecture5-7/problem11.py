for a in range(1, 51):
    for b in range(1, 51):
        for c in range(1, 51):
            if c ** 3 == a ** 2 + b ** 2:
                print(f"Found results: {a}^2 + {b}^2 = {c}^3")
