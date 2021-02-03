x = 50
def test():
    global x
    print(f"x :{x}")

    x = 100
    print(f"Changed x to :{x}")

test()
print(x)