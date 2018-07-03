print([a * b * (1000 - a - b) for a in range(1, 1000 + 1) for b in range(a + 1, 1000 + 1) if a * a + b * b == (1000 - a - b) * (1000 - a - b)][0])
