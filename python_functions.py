def sum_to(n):
    num_range = range(n+1)
    sum = 0
    for num in num_range:
        sum += num 
    print(sum)

sum_to(6)  # returns 21
sum_to(10) # returns 55


def largest(nums):
    largest_num = 0
    for num in nums:
        if num > largest_num:
            largest_num = num
    print(largest_num)


largest([1, 2, 3, 4, 0])  # returns 4
largest([10, 4, 2, 231, 91, 54])  # returns 231

def occurrences(str1, str2):
    count = str1.count(str2)
    print(count)
    


occurrences('fleep floop', 'e')   # returns 2
occurrences('fleep floop', 'p')   # returns 2
occurrences('fleep floop', 'ee')  # returns 1
occurrences('fleep floop', 'fe')  # returns 0

def product(*args):
    total = 1
    for n in args:
      total = n * total        
    print(total)

product(-1, 4) # returns -4
product(2, 5, 5) # returns 50
product(4, 0.5, 5) # returns 10.0