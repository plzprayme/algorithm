def solution (number, k):    
    def removeMin(j, s):
        if j == 0:
            return s[1:]
        elif j == len(s) - 1:
            return s[:-1]
        else:
            return s[:j] + s[j+1:]

    i = 0
    while k > 0:
        print(f'k: {k}, i: {i}, number[i]: {number[i]}, number: {number}', end=" ")
        if number[i] < max(number[i+1: i+k+1]):
            number = removeMin(i, number)
            k -= 1
        else:
            i+=1
        print()


    return number


def solution2(number, k):    
    i = 0
    while k > 0:
        try:
            if number[i] < number[i+1]:
                if i == 0:
                    number = number[1:]
                elif j == len(number) - 1:
                    number = number[:-1]    
                else:
                    number = number[:i] + number[i+1:]
                k -= 1
                i = 0
                continue
            else:
                i += 1
        except:
            j = number.index(min(number))
            if j == 0:
                number = number[1:]
            elif j == len(number) - 1:
                number = number[:-1]
            else:
                number = number[:j] + number[j+1:]
            k-=1


    return number

print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))