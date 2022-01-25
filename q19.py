# def leap():
#     year=int(input("any number"))
#     if   year%400 and year%100!=0  or year%4==0:
#         return True
#     else:
#         return False
# print(leap())


def leap():
    year=int(input("any number"))
    if year%4==0:
        if year%100:
            if year%400:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
print(leap())


