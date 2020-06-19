from _functools import reduce

numbers = [0,1,2,3,4,5,6,7,8,9]
evenNumbers = list(filter(lambda n: n%2==0 , numbers))
doubles = list(map(lambda n: n*2, evenNumbers))
sum = reduce(lambda s,n: s+n ,evenNumbers)
print(evenNumbers)
print(doubles)
print(sum)