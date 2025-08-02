dict_ = {"key1": "value1", "key2": "value2"}
print(dict_)
print(type(dict_))
print(dict_["key1"])
print(dict_["key2"])

dict_ = {"key1": 12, "key2": [1,2,3], "key3": "Mehrdad", "key4": True}
print(dict_)
print(dict_["key2"])


dict_ = dict(key1 = 12, key2 = [1,2,3], key3 = "Mehrdad", key4 = True)
print(dict_)
print(dict_["key2"])
dict_["key1"] = "254"
print(dict_)