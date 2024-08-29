user_input = int(input())
symbol = "#"
for _ in range(user_input):
    print(symbol.center(user_input * 2))
    symbol += "##"
