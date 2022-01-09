while True:
    try:
        kageBunshin = int(input())
        original = 0
        while kageBunshin > 1:
            kageBunshin //= 2
            original += 1
        print(original)
    except:
        break