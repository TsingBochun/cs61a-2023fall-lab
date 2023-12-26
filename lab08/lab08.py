# Q2: Duplicate Link
def duplicate_link(link, val):
    """Mutates `link` such that if there is a linked list
    node that has a first equal to value, that node will
    be duplicated. Note that you should be mutating the
    original link list.

    >>> x = Link(5, Link(4, Link(3)))
    >>> duplicate_link(x, 5)
    >>> x
    Link(5, Link(5, Link(4, Link(3))))
    >>> y = Link(2, Link(4, Link(6, Link(8))))
    >>> duplicate_link(y, 10)
    >>> y
    Link(2, Link(4, Link(6, Link(8))))
    >>> z = Link(1, Link(2, (Link(2, Link(3)))))
    >>> duplicate_link(z, 2) # ensures that back to back links with val are both duplicated
    >>> z
    Link(1, Link(2, Link(2, Link(2, Link(2, Link(3))))))
    """
    "*** YOUR CODE HERE ***"
    if link is Link.empty:
        return
    if link.first == val:
        link.rest = Link(val, link.rest)
    else:
        duplicate_link(link.rest, val)
        duplicate_link(link.rest.rest, val)       # Q2: Duplicate Link FINISHED
    

# Q3: Convert Link
def convert_link(link):
    """Takes a linked list and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> convert_link(link)
    [1, 2, 3, 4]
    >>> convert_link(Link.empty)
    []
    """
    "*** YOUR CODE HERE ***"
    list = []
    if link is Link.empty:
        return []
    #list = [link.first] + convert_link(link.rest)
    #return list                                       # Q3: Convert Link RECURSIVE finished
    remain = link
    while True:
        list.append(remain.first)
        remain = remain.rest
        if remain is Link.empty:
            break
    return list                                     # Q3: Convert Link ITERAGBLE finished

    

# Q4: Multiply Links
def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3))
    >>> b = Link(5, Link(4))
    >>> p1 = multiply_lnks([a, b])
    >>> p1
    Link(10, Link(12))

    >>> c = Link(2, Link(3, Link(5)))
    >>> d = Link(6, Link(4, Link(2)))
    >>> e = Link(4, Link(1, Link(0, Link(2))))
    >>> p2 = multiply_lnks([c, d, e])
    >>> p2
    Link(48, Link(12, Link(0)))
    """
    #product = 1
    #for _________ in ________________:
    #    if __________________________________________:
    #        _________________________________
    #    ___________________
    #lst_of_lnks_rests = [_________ for _________ in ________________]
    #return _________________________________________________
    #if lst_of_lnks[0].rest is Link.empty:
    #    if lst_of_lnks[1].rest is Link.empty:
    #        return Link(lst_of_lnks[0].first * lst_of_lnks[1].first)
    #return Link(lst_of_lnks[0].first * lst_of_lnks[1].first, multiply_lnks([x.rest for x in lst_of_lnks]))
    product = 1
    for lnk in lst_of_lnks:
        if lnk is Link.empty:
            return Link.empty    # 当这个链表本身是空链表的时候直接返回它，不进行后面的运算，最后再利用空元祖乘以任何数值得到空元组，所以最后再和前面的元素进行LINK（），依然是作为尾巴存在
            #return              
        product *= lnk.first
    lst_of_lnks_rests = [lnk.rest for lnk in lst_of_lnks]
    return Link(product, multiply_lnks(lst_of_lnks_rests))      # Q4: Multiply Links 学习答案，没有百分百看懂
                                                        # 一个空元组乘以任何数字都是空元组


class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

