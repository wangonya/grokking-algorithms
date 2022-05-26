def divide_land(a, b):
    bigger_side = max(a,b)
    smaller_side = min(a,b)

    if smaller_side * 2 == bigger_side:
        return (smaller_side, smaller_side)
    else:
        rem = bigger_side % smaller_side
        return divide_land(rem, smaller_side)

print(divide_land(1680, 640)) # => (160, 80)
print(divide_land(400, 640)) # => (160, 80)
