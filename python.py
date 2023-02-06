info_dict ={
    "name": "test",
    "age" : "age"
}
print(info_dict)

name = input("Enter your name: ")
age = input("Enter your age: ")

info_dict["name"] = name
info_dict["age"] = int(age)

print(info_dict)