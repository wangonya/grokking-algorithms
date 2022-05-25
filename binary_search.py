def binary_search(_list, item):
    high = len(_list) - 1
    low = 0

    while high >= low:
        mid = (high + low) // 2
        guess = _list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


if __name__ == "__main__":
    position = binary_search(
        [2, 3, 5, 7, 8, 9, 12, 24, 32],
        12,
    )
    print(position)
