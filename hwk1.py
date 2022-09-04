# Seymone Gugneja
# Homework 1 - Polymorphism, recursion, and data structures in python
# CSCI 3675

# 1 - use imperative programming to return half of each even number in the list

def halveEvensImperative(evenNums):
    evens = []

    for x in evenNums:
        if (x % 2 == 0):
            halveEvens = x/2
            evens.append(int(halveEvens))

    return evens

# 2 - recursively solve problem 1

def halveEvensRecursive(evenNums):
    if not evenNums:
        return []
    else:
        idx = evenNums[0]
        evens = []
        if idx % 2 == 0:
            idx //= 2
            evens.append(idx)
        result = evens + halveEvensRecursive(evenNums[1:])

    return result

# 3 - use list comprehension to solve problem 1

def halveEvensComprehension(evenNums):

    return [i//2 for i in evenNums if i % 2 == 0]

# 4 - fix casing so first letter is capatalized and the rest are lowercase

def capatalizeImperative(word):
    for x in word.split():
        newWord = x[0].upper() + x[1:].lower()

    return newWord

# 5 - use list comprehension to solve 4

def capatalizeComprehension(word):
    s = word

    return " ".join([s[0].upper() + s[1:].lower() for x in s.split()])

# 6 - use imperative programming to sum all of the numbers in the list

def sumImperative(nums):
    sum = 0
    for i in nums:
        sum += i

    return sum

# 7 - recursively solve problem 6

def sumRecursive(nums):

    #if list empty, return 0 because there is nothing to sum
    if not nums:
        return 0
    else:
        return nums[0] + sumRecursive(nums[1:])

# 8 - use imperative programming to find if the input is a palindrome

def palindromeImperative(word):
    ogString = word
    revString = ogString[::-1]

    return ogString == revString

# 9 - recursively solve problem 8

def palindromeRecursive(word):
    # 0 items means string is palindrome
    if len(word) == 0:
        return True
    # 1 item means string is palindrome
    elif len(word) == 1:
        return True
    # 2 items means check wether true or false
    else:
        #if first and last letter are same, it could be palindrome
        #remove the first and last letters and compare the new first and
        #last letters. keep comparing until base case is reached.
        return word[0] == word[-1] and palindromeRecursive(word[1:-1])

# 10 - write a recursive function inRangeRecursive that takes two inputs and returns an inclusive list within a range of numbers

def inRangeRecursive(start, end, rList):
    while True:
        if not rList:
            return []
        elif(rList[0] >= start) and (rList[0] <= end):
            return [rList[0]] + inRangeRecursive(start, end, rList[1:])
        else:
            rList = rList[1:]

# 11 - use list comprehension to solve problem 10

def inRangeComprehensive(start,end,rList):
    z = [i for i in rList if (i >= start) and (i <= end)]
    return z

def main():
    print(halveEvensImperative([0, 2, 1, 7, 8, 56, 17, 18]))
    print(halveEvensRecursive([0, 2, 1, 7, 8, 56, 17, 18]))
    print(halveEvensComprehension([0, 2, 1, 7, 8, 56, 17, 18]))
    print(capatalizeImperative('grEENVIlle'))
    print(capatalizeComprehension('grEENVIlle'))
    print(sumImperative([0, 2, 1, 7, 8, 56, 17, 18]))
    print(sumImperative([1, 2.0]))
    print(sumRecursive([0, 2, 1, 7, 8, 56, 17, 18]))
    print(sumRecursive([1, 2.0]))
    print(palindromeImperative([0,2,0]))
    print(palindromeImperative('abb'))
    print(palindromeRecursive([0,2,0]))
    print(palindromeRecursive('abb'))
    print(inRangeRecursive(5,10,range(1,15)))
    print(inRangeRecursive(-5,5,range(-10,10)))
    print(inRangeComprehensive(5,10,range(1,15)))
    print(inRangeComprehensive(-5,5,range(-10,10)))

if __name__ == "__main__":
    main()
