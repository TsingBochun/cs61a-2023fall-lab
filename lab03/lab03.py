from operator import add, mul

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1


def ordered_digits(x):
    """Return True if the (base 10) digits of X>0 are in non-decreasing   # 从左往右读取digit,判断是否为非降序,如果是就返回真,不是就返回假
    order, and False otherwise.

    >>> ordered_digits(5)
    True
    >>> ordered_digits(11)
    True
    >>> ordered_digits(127)
    True
    >>> ordered_digits(1357)
    True
    >>> ordered_digits(21)
    False
    >>> result = ordered_digits(1375) # Return, don't print
    >>> result
    False

    """
    "*** YOUR CODE HERE ***"
    text = str(x)
    i = 0
    while i < len(text) - 1:                  # i 取到倒数第二个即可
        if int(text[i]) <= int(text[i+1]):
            i += 1
        else:
            return False
    return True                       # Q1: Ordered: Digitsordered_digits() finished 


def get_k_run_starter(n, k):
    """Returns the 0th digit of the kth increasing run within n.
    >>> get_k_run_starter(123444345, 0) # example from description
    3
    >>> get_k_run_starter(123444345, 1)
    4
    >>> get_k_run_starter(123444345, 2)
    4
    >>> get_k_run_starter(123444345, 3)
    1
    >>> get_k_run_starter(123412341234, 1)
    1
    >>> get_k_run_starter(1234234534564567, 0)
    4
    >>> get_k_run_starter(1234234534564567, 1)
    3
    >>> get_k_run_starter(1234234534564567, 2)
    2
    """
    #i = 0                                            # 不使用给定的写法
    #final = None
    #while ____________________________:
    #    while ____________________________:
    #        ____________________________
    #    final = ____________________________
    #    i = ____________________________
    #    n = ____________________________
    #return final
    list = []                                       # 初始化一个list空表单
    text = str(n)
    i = 0         # 用来显示当前元素的位置
    l = 0         # 从来表示起始元素的位置
    #while i < len(text) - 1:
    #    if int(text[i]) < int(text[i+1]):
    #        i += 1
    #    else: # int(text[i]) >= int(text[i+1])
    ##        list.append(text[l: i+1])               # 将i之前的元素作为数组赋给list,包括i，所以结尾是i+1
    #        l = i + 1                            # 测试将结束位置的下一个位置标记为k
    #        i = l
        #    k += 1
        #    break        # onlu for debug
    ###上述全部注释掉，改用for循环来实现
    for i in range(len(text) - 1):                # 因为最后一个元素没有包括进去，所以实质上i是到了倒数第二个
        if int(text[i]) < int(text[i+1]):  
            i += 1
            if i == len(text) - 1:            # 相当于此时i指向最后一个元素
                list.append(text[l: i+1])     # 将此时的最后一组由小到大组放进去 
        else: # int(text[i]) >= int(text[i+1])
            list.append(text[l: i+1])
            l = i + 1
            i = l                    
     #return list           # only for debug        # Q2: K Runner 生成list完成
    index = len(list) - 1 - k             # 将k进行转换
    return int(list[index][0])            # Q2: K Runner get_k_run_starter() finish



def nearest_two(x):
    """Return the power of two that is nearest to x.

    >>> nearest_two(8)    # 2 * 2 * 2 is 8
    8.0
    >>> nearest_two(11.5) # 11.5 is closer to 8 than 16
    8.0
    >>> nearest_two(14)   # 14 is closer to 16 than 8
    16.0
    >>> nearest_two(2015)
    2048.0
    >>> nearest_two(.1)           # 测试这里有bug,显示为0.5,其余均为正数  Q3: Nearest Power of Two 整型测试通过
    0.125
    >>> nearest_two(0.75) # Tie between 1/2 and 1
    1.0
    >>> nearest_two(1.5)  # Tie between 1 and 2
    2.0

    """
    power_of_two = 1.0
    "*** YOUR CODE HERE ***"
    def power2(n):               # 先自己写一个2的幂函数
        return float(2 ** n)
    #if x < 1:
    #    while(power2(i) <= x):   
    i = 0
    if x < 1:          # 当X是小数的时候需要单独考虑       # Q3: Nearest Power of Two nearest_two all finished
        while(power2(i) >= x):
            if power2(i) == x:
                power_of_two = power2(i)
            i -= 1
        if x - power2(i) <=  power2(i+1) - x:
            power_of_two = power2(i)
        else:
            power_of_two = power2(i+1)
        

    while(power2(i) <= x):    # 遍历所有2的幂小于等于x, 找到小于等于x的2的幂的最大值的指数i
        if power2(i) == x:     # 如果存在2的幂等于x
            power_of_two = power2(i)
        i += 1    # 当2的i次幂大于x的时候退出循环，这个时候的i是2的i次幂比x刚刚大的那个i
    if power2(i) - x <= x - power2(i-1):
        power_of_two = power2(i)
    else:
        power_of_two = power2(i-1)
    
    return power_of_two


def make_repeater(func, n):
    """Returns the function that computes the nth application of func.

    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> make_repeater(square, 0)(5) # Yes, it makes sense to apply the function zero times!
    5
    """
    "*** YOUR CODE HERE ***"
    #def myfunction(n):                      # Q4: Make Repeater 暂时跳过
    if n <= 0:
        return lambda x: x              # 如果调用零次只显示参数
    list = []                          # 初始化一个list用来存放函数
    for i in range(n):
        if i == 0:
            #tempf = func
            list.append(func)
            i += 1
        else:
            list.append(composer(func, list[i - 1]))
            i += 1
    return list[i-1]                 # Q4: Make Repeater：make_repeater（） finish
    # myfunction = tempf

    #    return result                        
    #return myfunction
    
    

def composer(func1, func2):
    """Returns a function f, such that f(x) = func1(func2(x))."""
    def f(x):
        return func1(func2(x))
    return f

def apply_twice(func):
    """Returns a function that applies func twice.

    func -- a function that takes one argument

    >>> apply_twice(square)(2)
    16
    """
    "*** YOUR CODE HERE ***"
    #def myfunction(x):
    #    result = func(func(x))
    #    return result
    #return myfunction            # Q5: Apply Twice apply_twice 完成，不使用make_repeater版本
    #def myfunction(x):
    #    result = make_repeater(func, 2)
    #    return result
    return make_repeater(func, 2)     # Q5: Apply Twice apply_twice 完成，使用make_repeater版本


def div_by_primes_under(n):
    """
    >>> div_by_primes_under(10)(11)
    False
    >>> div_by_primes_under(10)(121)
    False
    >>> div_by_primes_under(10)(12)
    True
    >>> div_by_primes_under(5)(1)
    False
    """
#    checker = lambda x: False
#    i = ____________________________
#    while ____________________________:
#        if not checker(i):
#            checker = ____________________________
#        i = ____________________________
#    return ____________________________
    # 首先找到n以下所有的质数，包括n，按顺序装在一个list中
    list = []
    def is_prime(x):      # 自己写一个判断质数的函数，如果是质数，返回真，反之亦然
        if x == 0 or x == 1 or x < 0:
            return False
        i = 2             # 直接让i从2开始
        while i < x:
            if x % i == 0:
                return False
            i += 1
        return True
    # 先找到n以下的所有质数，包括n
    for i in range(0, n+1):
        if is_prime(i) == True:
            list.append(i)
    # return list                # Q6: It's Always a Good Prime 完成功能找到N以下所有质数并存储在list
    # 最后实现 n 能否被 n以下所有质数 中任意一个整除
    def myfunction(x):
        k = 0
        for k in range(len(list)):
            if x % list[k] == 0:
                return True
            #else:
            #    k += 1
            k += 1
        return False
    return myfunction       # Q6: It's Always a Good Prime 完成所有功能

        


def div_by_primes_under_no_lambda(n):
    """
    >>> div_by_primes_under_no_lambda(10)(11)
    False
    >>> div_by_primes_under_no_lambda(10)(121)
    False
    >>> div_by_primes_under_no_lambda(10)(12)
    True
    >>> div_by_primes_under_no_lambda(5)(1)
    False
    """
    def checker(x):
        return False
    i = ____________________________
    while ____________________________:
        if not checker(i):
            def outer(____________________________):
                def inner(____________________________):
                    return ____________________________
                return ____________________________
            checker = ____________________________
        i = ____________________________
    return ____________________________

