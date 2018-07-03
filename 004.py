print((max(map(int, filter(lambda x: x == x[::-1], map(str,[x*y for x in range(900,1000) for y in range(900,1000)]))))))
