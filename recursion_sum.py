def _sum(_list):
    if not _list:
        return 0

    if len(_list) == 1:
        return _list[0]
    else:
        return _list.pop() + _sum(_list)

print(_sum([1,2,3,4,5])) # => 15
print(_sum([2,4,6])) # => 12
