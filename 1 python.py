numbers = input("Input 3 integer separated by commas: ") 
lv = numbers.split(",")
ts = tuple(lv)
# print(len(lv))
# print(ts)
remove_RI=set(ts)
if len(lv)>3:
    print("Enter 3 number only")
elif len(remove_RI)==len(lv):
    print(0)
else:
    print(4-len(remove_RI))