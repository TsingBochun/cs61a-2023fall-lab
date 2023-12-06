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
    i = 0
    #k = 0
    while i <= len(text) - 1:
        if int(text[i]) < int(text[i+1]):
            i += 1
        else: # int(text[i]) >= int(text[i+1])
            list.append = text[0: i]               # 将i之前的元素作为数组赋给list
        #    k += 1
    return list           # only for debug        # Q2: K Runner 暂时跳过



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
    >>> nearest_two(.1)           # 测试这里有bug,显示为0.5,其余均为正数
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
    i = 0
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
    checker = lambda x: False
    i = ____________________________
    while ____________________________:
        if not checker(i):
            checker = ____________________________
        i = ____________________________
    return ____________________________

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

