classmates = ['Michael', 'Bob', 'Tracy']
print(len(classmates))
classmates.append('jesse')
classmates.insert(1, "lisa")

classmates2 = ('Michael', 'Bob', 'Tracy')


for classmate in classmates:
    print(classmate)

dictionary = {"jesse":12, "lisa":21}
for key, value in dictionary.items():
    print(key)
    print(value)