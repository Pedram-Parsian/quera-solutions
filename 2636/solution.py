king, queen, rooks, bishops, knights, pawns = [int(_) for _ in input().split()]
print(
    1 - king,
    1 - queen,
    2 - rooks,
    2 - bishops,
    2 - knights,
    8 - pawns,
)
