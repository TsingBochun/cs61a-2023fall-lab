# Q2: Finding Berries!
def berry_finder(t):
    """Returns True if t contains a node with the value 'berry' and 
    False otherwise.

    >>> scrat = tree('berry')
    >>> berry_finder(scrat)
    True
    >>> sproul = tree('roots', [tree('branch1', [tree('leaf'), tree('berry')]), tree('branch2')])
    >>> berry_finder(sproul)     # 第一次测试有误,实测为 FALSE
    True
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> berry_finder(numbers)
    False
    >>> t = tree(1, [tree('berry',[tree('not berry')])])
    >>> berry_finder(t)
    True
    """
    "*** YOUR CODE HERE ***"
    # 先看这个TREE是不是叶子，如果是，本身的LABEL如果是berry那么就返回TRUE，反之亦然
    #result = 0
    #if is_leaf(t) == True:
    #    if label(t) == 'berry':
        #    print(t)      #only for debug
        #    return True
    #        result += 1
    #    else:
        #    print(t)      #only for debug
        #    return False
    #        result += 0
    # 如果不是叶子，如果LABEL是berry的话，就返回TRUE，反之继续寻找：
    #else:
    #    if label(t) == 'berry':
        #    print(t)      #only for debug
        #    return True
    #        result += 1
    #    else: 
    #        for branch in branches(t):
        #        print(t)      #only for debug
                #return berry_finder(branch)
    #            result += berry_finder(branch)
    #if result > 0:
    #    return True
    #else:
    #    return False        # Q2: Finding Berries! finished
    if label(t) == 'berry':
        return True
    else:
        for branch in branches(t):
            if berry_finder(branch) == True:
                return True
    return False        # Q2 官方实现


# Q3: Replace Loki at Leaf
def replace_loki_at_leaf(t, lokis_replacement):
    """Returns a new tree where every leaf value equal to "loki" has
    been replaced with lokis_replacement.

    >>> yggdrasil = tree('odin',
    ...                  [tree('balder',
    ...                        [tree('loki'),
    ...                         tree('freya')]),
    ...                   tree('frigg',
    ...                        [tree('loki')]),
    ...                   tree('loki',
    ...                        [tree('sif'),
    ...                         tree('loki')]),
    ...                   tree('loki')])
    >>> laerad = copy_tree(yggdrasil) # copy yggdrasil for testing purposes
    >>> print_tree(replace_loki_at_leaf(yggdrasil, 'freya'))
    odin
      balder
        freya
        freya
      frigg
        freya
      loki
        sif
        freya
      freya
    >>> laerad == yggdrasil # Make sure original tree is unmodified
    True
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t) == True:
        if label(t) == 'loki':
            return tree(lokis_replacement)
        #else:
        #    return tree(t)
    else:
        #for branch in branches(t):
        #    if is_leaf(branch) == True:
        #    replace_loki_at_leaf(branch, lokis_replacement)
        #    return tree()
        bs = [replace_loki_at_leaf(b, lokis_replacement) for b in branches(t)]
        return tree(label(t), bs)        # Q3: Replace Loki at Leaf FINISHED

#### DISC05部分
#Q5: Height
def height(t):
    """Return the height of a tree.
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    >>> t = tree(3, [tree(1), tree(2, [tree(5, [tree(6)]), tree(1)])])
    >>> height(t)
    3
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t) == True:
        return 0
    #elif is_leaf(t) == False:
    #    for b in branches(t):
    #        if is_leaf(b) == True:
    #            return 1
    else:
        return 1 + max([height(b) for b in branches(t)])   #Q5(DISC05): Height finished


#Q6: Find Path
def find_path(t, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)  # returns None
    """
    #if _____________________________:
    #    return _____________________________
    #_____________________________:
    #    path = ______________________
    #    if _____________________________:
    #        return _____________________________
    #if is_leaf(t) == True and label(t) == x:
    if label(t) == x:
        return [x]
    else:
        #path = find_path(b, x) for b in branches(t)
        #if path:     # 这个代码代表PATH确实能够存在

        for b in branches(t):
            path = find_path(b, x) 
        #return list(label(t)) + path
        #if x in path:
            #return [label(t) + path]
            if path:         # 这个代码代表PATH确实能够存在
                return [label(t)] + path
        #return [path] + [label(t)]
            

# Tree ADT

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    if change_abstraction.changed:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return {'label': label, 'branches': list(branches)}
    else:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    if change_abstraction.changed:
        return tree['label']
    else:
        return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    if change_abstraction.changed:
        return tree['branches']
    else:
        return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if change_abstraction.changed:
        if type(tree) != dict or len(tree) != 2:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True
    else:
        if type(tree) != list or len(tree) < 1:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True

def is_leaf(tree):
    """Returns True if the given tree is a leaf. (i.e. It has no branches.)"""
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])

# Q4: Distance
from math import sqrt
def distance(city_a, city_b):
    """
    >>> city_a = make_city('city_a', 0, 1)
    >>> city_b = make_city('city_b', 0, 2)
    >>> distance(city_a, city_b)
    1.0
    >>> city_c = make_city('city_c', 6.5, 12)
    >>> city_d = make_city('city_d', 2.5, 15)
    >>> distance(city_c, city_d)
    5.0
    """
    "*** YOUR CODE HERE ***"
    x = get_lat(city_a) - get_lat(city_b)
    y = get_lon(city_a) - get_lon(city_b)
    distance = sqrt(x * x + y * y)
    return distance

# Q5: Closer City
def closer_city(lat, lon, city_a, city_b):
    """
    Returns the name of either city_a or city_b, whichever is closest to
    coordinate (lat, lon). If the two cities are the same distance away
    from the coordinate, consider city_b to be the closer city.

    >>> berkeley = make_city('Berkeley', 37.87, 112.26)
    >>> stanford = make_city('Stanford', 34.05, 118.25)
    >>> closer_city(38.33, 121.44, berkeley, stanford)
    'Stanford'
    >>> bucharest = make_city('Bucharest', 44.43, 26.10)
    >>> vienna = make_city('Vienna', 48.20, 16.37)
    >>> closer_city(41.29, 174.78, bucharest, vienna)
    'Bucharest'
    """
    "*** YOUR CODE HERE ***"
    #list = []
    # 创造一个CITY当做比较器
    comepare_city = make_city('compare', lat, lon)
    # 分别计算出所有CITY和这个CITY的距离，放在一个list中，最后取最小的
    #min_distance = min([distance(comepare_city, city_a), distance(comepare_city, city_b)])
    if distance(comepare_city, city_a) < distance(comepare_city, city_b):
        return get_name(city_a)
    else:
        return get_name(city_b)         # 



def check_city_abstraction():
    """
    There's nothing for you to do for this function, it's just here for the extra doctest
    >>> change_abstraction(True)
    >>> city_a = make_city('city_a', 0, 1)
    >>> city_b = make_city('city_b', 0, 2)
    >>> distance(city_a, city_b)
    1.0
    >>> city_c = make_city('city_c', 6.5, 12)
    >>> city_d = make_city('city_d', 2.5, 15)
    >>> distance(city_c, city_d)
    5.0
    >>> berkeley = make_city('Berkeley', 37.87, 112.26)
    >>> stanford = make_city('Stanford', 34.05, 118.25)
    >>> closer_city(38.33, 121.44, berkeley, stanford)
    'Stanford'
    >>> bucharest = make_city('Bucharest', 44.43, 26.10)
    >>> vienna = make_city('Vienna', 48.20, 16.37)
    >>> closer_city(41.29, 174.78, bucharest, vienna)
    'Bucharest'
    >>> change_abstraction(False)
    """

# Treat all the following code as being behind an abstraction layer,
# you shouldn't need to look at it.
def make_city(name, lat, lon):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_name(city)
    'Berkeley'
    >>> get_lat(city)
    0
    >>> get_lon(city)
    1
    """
    if change_abstraction.changed:
        return {"name" : name, "lat" : lat, "lon" : lon}
    else:
        return [name, lat, lon]

def get_name(city):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_name(city)
    'Berkeley'
    """
    if change_abstraction.changed:
        return city["name"]
    else:
        return city[0]

def get_lat(city):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_lat(city)
    0
    """
    if change_abstraction.changed:
        return city["lat"]
    else:
        return city[1]

def get_lon(city):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_lon(city)
    1
    """
    if change_abstraction.changed:
        return city["lon"]
    else:
        return city[2]

###############


def dejavu(t, n):
    """
    >>> my_tree = tree(2, [tree(3, [tree(5), tree(7)]), tree(4)])
    >>> dejavu(my_tree, 12) # 2 -> 3 -> 7
    True
    >>> dejavu(my_tree, 5) # Sums of partial paths like 2 -> 3 don ’t count
    False
    """
    "*** YOUR CODE HERE ***"


def hailstone_tree(n, h):
    """Generates a tree of hailstone numbers that will reach N, with height H.
    >>> print_tree(hailstone_tree(1, 0))
    1
    >>> print_tree(hailstone_tree(1, 4))
    1
      2
        4
          8
            16
    >>> print_tree(hailstone_tree(8, 3))
    8
      16
        32
          64
        5
          10
    """
    if _________________________________:
        return _________________________________
    branches = _________________________________
    if ___________ and ___________ and ___________:
        branches += _________________________________
    return tree(n, branches)


def change_abstraction(change):
    """
    For testing purposes.
    >>> change_abstraction(True)
    >>> change_abstraction.changed
    True
    """
    change_abstraction.changed = change

change_abstraction.changed = False

