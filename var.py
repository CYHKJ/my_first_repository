""" my_var = 10
print(my_var)

my_list = [1, 2, 3]
print(*my_list)
print(my_list) """

""" my_int = 10
print(my_int)

my_float = 3.14
print(my_float)

my_complex = 3+4j
print(my_complex)

my_character = 'A'
print(my_character)
my_char = "@"
print(my_char)

my_string = 'Hello, World!'
print(my_string)
str_name = "python"
print(str_name)

my_bool = True
bFlag = False
print(my_bool)
print(bFlag)

my_list = [1, 2, 'three', True]
print(my_list)
lsElement = [3.14, "b", 'two', False]
print(lsElement) """

""" my_list = [10, 3, 8, 9, 42, "hello"]
print(my_list)
print(*my_list) """

""" my_list = [10, 3, 8, 9, 42, "hello"] """
""" print(my_list[3])

my_list[3] = "t"
print(*my_list)
 """

""" print(my_list[3] - my_list[2]) """

""" slice_ls = my_list[2:5]
print(slice_ls)
 """
""" my_list = [10, 3, 8, 9, 42, "hello", [5, 4, 2, "world"]]
print(my_list)
print(my_list[6][1])
print(my_list[5][2]) """

""" my_list = [10, 3, 8, 9, 42, "hello"] """
""" print(my_list)
my_list.insert(2,4)
print(my_list)
 """
""" print(my_list.index(3)) """

""" my_list.append(22)
print(my_list) """

""" print(my_list.count(5)) """

""" print(my_list.pop())
print(my_list)

my_list.sort()
print(my_list) """

""" print(my_list)
my_list.sort()
print(my_list) """
""" list = ['python', 'hello', 'apple']
print(list)
list.sort()
print(list) """

""" my_list = [10, 3, 8, 9, 42, "hello"]
print(my_list)
my_list.reverse()
print(my_list) """

""" my_list = [10, 3, 8, 9, 42,8, "hello"]
""" """ list_tmp = [5, 7, "world"] """
"""
print(my_list, list_tmp)
my_list.extend(list_tmp)
print(my_list)
list_tmp.clear()
print(list_tmp) """
""" my_list.remove(3)
print(my_list) """

""" print(my_list)
del my_list[5]
print(my_list) """

""" my_tuple = (1, 2, 'three', True)
tpItem = (3.14, "b", 'two', False)
print(my_tuple)
print(tpItem)
 """
""" my_tup = (4, 2, 6, 1, "py", "w") """
""" print(my_tup.__len__())
print(my_tup)
 """
""" print(my_tup[2])
print(my_tup[2] + my_tup[0])
print(*my_tup) """

""" print(my_tup[2:]) """

""" my_tup = (4, 2, 6, 1, "py", "w", ("h", 8, 7, 3))
print(my_tup)

print(my_tup[6][0]) """

""" my_tup = (4, 2, 6, 1, "py", "w")    """ 
""" print(my_tup.index(2,0,3)) """

""" y_dict = {'key1': 'value1', 'key2': 'value2'}
dicData = {"name" : "python", "number" : 23564897}
print(my_dict)
print(dicData) """

""" my_dict = {'key1': 'value1', 'key2': 'value2'}
my_item = my_dict.items()
print(my_item) """

""" idx = ("key1", "key2", "key3")
dicts = dict.fromkeys(idx, "0")
print(dicts)
 """
""" my_dict = {'key1': 'value1', 'key2': 'value2'}
dicData = {"name" : "python", "number" : 23564897}

print(my_dict["key1"]) """

""" my_dict = {'key1': 'value1', 'key2': 'value2'}
my_str = my_dict.get("key2")
print(my_str) """
    
""" my_dict = {'key1': 'value1', 'key2': 'value2'}
print(my_dict.pop("key1"))
print(my_dict) """

""" my_dict = {'key1': 'value1', 'key2': 'value2'}
dicts = my_dict.copy()
print(dicts)
print(my_dict) """

""" my_dict = {'key1': 'value1', 'key2': 'value2'}
dicData = {"name" : "python", "number" : 23564897}

my_dict["key3"] = "va;ue3"

print(my_dict) """

""" my_dict = {'key1': 'value1', 'key2': 'value2'}
my_dict.setdefault("key3")
print(my_dict)
 """

""" my_dict = {'key1': 'value1', 'key2': 'value2'}
my_dict.update({"key1" : "v4"})
print(my_dict) """

""" my_dict = {'key1': 'value1', 'key2': 'value2'}
del my_dict["key2"]
print(my_dict) """

""" my_dict = {'key1': 'value1', 'key2': 'value2'}
print("key2" in my_dict)
print("key3" in my_dict) """

""" my_dict = {'key1': 'value1', 'key2': 'value2'}
my_list = list(my_dict.keys())
print(my_list) """

""" my_dict = {'key1': 'value1', 'key2': 'value2'}
my_list = list(my_dict.values())
print(my_list) """

""" my_dict = {'key1': 'value1', 'key2': 'value2'}
my_set = set(my_dict.keys())
print(my_set) """

my_dict = {'key1': 'value1', 'key2': 'value2'}
my_dict.clear()
print(my_dict)