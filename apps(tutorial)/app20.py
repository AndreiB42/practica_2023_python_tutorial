# numbers = [5,2,1,5,7,4]
# numbers.append(20)
# numbers.insert(0, 10)
# numbers.remove(5)
# numbers.clear()
# numbers.pop()
# print(numbers.index(5))
# print(50 in numbers) #boolean
# print(numbers.count(5))
# numbers.sort()
# numbers.reverse()
# print(numbers)
# numbers2= numbers.copy()
# numbers.append(10)
# print(numbers)

numbers = [2,2,4,6,3,4,6,1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

