#1
ips=["10.0.0.1", "10.0.0.2", "10.0.0.1", "192.168.1.10"]
my_set=set(ips)
print(my_set)

#2
a={"root", "admin", "test"}
a.add("hacker")
a.remove("test")
print(a)

#3
banned={21, 22, 23, 25}
a=input("Введите порт:")
if a in banned:
    print("Порт запрещен")
else:
    print("Порт разрешен")

#4
known={"mal.com", "bad.net"}
new={"bad.net", "devil.org"}
result=new.difference(known)
print(result)

#5
white_list={"alice", "bob", "root"}
black_list={"root", "admin"}
result=white_list.intersection(black_list)
print(result)

#6
a= {"CVE-1", "CVE-2"}
b= {"CVE-2", "CVE-3"}
result=a.union(b)
print(result)

#7
admin={"read", "write", "delete"}
user={"read", "download"}
result=user.symmetric_difference(admin)
print(result)

#8
all_passwords=["123", "qwerty", "test", "123", "qwerty", "admin"]
banned={"test"}
unique = set(all_passwords)
result = unique.difference(banned)
print(result)

#9
global_list = {"10.0.0.1", "10.0.0.2", "192.168.1.1"}
local_list = {"10.0.0.2", "10.0.0.3"}
result = local_list.intersection(global_list)
print(result)

#10
logs=["scan", "debug_mode", "scan", "connect", "debug_info"]
unique = set(logs)
debug_logs=set()
for i in unique:
    if "debug" in i:
        debug_logs.add(i)
result = unique.difference(debug_logs)
print(result)