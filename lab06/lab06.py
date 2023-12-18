HW_SOURCE_FILE=__file__

# Q2: Insert Items
def insert_items(s, before, after):
    """Insert after into s after each occurrence of before and then return s.
    # Important: No new lists should be created or returned.   # 不可以创造新的列表
    >>> test_s = [1, 5, 8, 5, 2, 3]
    >>> new_s = insert_items(test_s, 5, 7)
    >>> new_s
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> test_s
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> new_s is test_s
    True
    >>> double_s = [1, 2, 1, 2, 3, 3]
    >>> double_s = insert_items(double_s, 3, 4)    
    >>> double_s
    [1, 2, 1, 2, 3, 4, 3, 4]                       # 测试未通过，测试结果为[1, 2, 1, 2, 3, 4, 3]
    >>> large_s = [1, 4, 8]
    >>> large_s2 = insert_items(large_s, 4, 4)
    >>> large_s2
    [1, 4, 4, 8]                                   # 测试未通过，测试结果为[1, 4, 4, 4, 8]
    >>> large_s3 = insert_items(large_s2, 4, 6)
    >>> large_s3
    [1, 4, 6, 4, 6, 8]                           # 测试未通过, 测试结果为[1, 4, 6, 4, 6, 4, 8]
    >>> large_s3 is large_s
    True
    """
    "*** YOUR CODE HERE ***"
    #for i in range(len(s)):
    #    if s[i] == before:
    #        if i == len(s) - 1:     # 假如测试是最后一个元素
    ##            s.append(after)
    #            return s
    #        s.insert(i+1, after)
    #        print("i: ", i)          # only for debug
    #        print("length of s: ", len(s))     # only for debug
    #for element in s:
    #    if element == before:
    #        s.insert(s.index(element) + 1, after) 
    i = 0
    while i < len(s):
        if s[i] == before:
            s.insert(i+1, after)
            i += 1       # 当完成这个操作之后，后面的元素不做条件判断，这样就不会进入无限循环
        i += 1
    return s           # Q2: Insert Items FINISHED



# Q4: Count Occurrences
def count_occurrences(t, n, x):
    """Return the number of times that x is equal to one of the
    first n elements of iterator t.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> count_occurrences(s, 10, 9)
    3
    >>> s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> count_occurrences(s2, 3, 10)
    2
    >>> s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> count_occurrences(s, 1, 3)  # Only iterate over 3
    1
    >>> count_occurrences(s, 3, 2)  # Only iterate over 2, 2, 2
    3
    >>> list(s)                     # Ensure that the iterator has advanced the right amount
    [1, 2, 1, 4, 4, 5, 5, 5]
    >>> s2 = iter([4, 1, 6, 6, 7, 7, 6, 6, 2, 2, 2, 5])
    >>> count_occurrences(s2, 6, 6)
    2
    """
    "*** YOUR CODE HERE ***"
    count = 0
    i = 0
    while i < n:
    #    if next(t) == x:     #
        tmp = next(t)
        if x == tmp:
    #    for x in t:
    #        if 
            count += 1
        i += 1
    return count         # Q4: Count Occurrences FINISHED

# Q5: Repeated 
def repeated(t, k):
    """Return the first value in iterator t that appears k times in a row,
    calling next on t as few times as possible.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s, 2)
    9
    >>> s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s2, 3)
    8
    >>> s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> repeated(s, 3)
    2
    >>> repeated(s, 3)
    5
    >>> s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
    >>> repeated(s2, 3)
    2
    """
    assert k > 1
    "*** YOUR CODE HERE ***"
    #list = [next(t)]      # 初始化一个表用来存数据
    count = 0
    list = []
    list.append(next(t))
    tmp = 0
    while True:
    #while i < k - 1:
        tmp = next(t)
        if tmp == list[-1]:
            i += 1
            if i == k - 1:
                return list[-1]
        else:
            list.append(tmp)
            i = 0

            

        
    

    




def partial_reverse(s, start):
    """Reverse part of a list in-place, starting with start up to the end of
    the list.

    >>> a = [1, 2, 3, 4, 5, 6, 7]
    >>> partial_reverse(a, 2)
    >>> a
    [1, 2, 7, 6, 5, 4, 3]
    >>> partial_reverse(a, 5)
    >>> a
    [1, 2, 7, 6, 5, 3, 4]
    """
    "*** YOUR CODE HERE ***"

