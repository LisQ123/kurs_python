pw = input("gimme password: ")
alphanum = pw.isalnum()
condition_only_upper = (alphanum and not pw.islower())
if len(pw) < 8:
    print("too short")
if not alphanum:
    print("yr pw should be alphanumeric")
if pw.isalpha():
    print("yr pw should contain digits too")
if pw.isdigit():
    print("yr pw should contain letters too")
if condition_only_upper:
    print("yr pw should contain at least 1 upper")
print("the end")