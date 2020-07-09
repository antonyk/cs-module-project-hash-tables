def no_dups(s):
    arr = s.split(' ') 
    dupes = {}
    result = []
    for v in arr:
    # for _, v in enumerate(arr):
        if v not in dupes:
            # if v != '':
            #     result += ''
            result.append(v)
            dupes[v] = 1
        else:
            dupes[v] += 1

    return ' '.join(result)



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))