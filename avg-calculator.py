print("created by hussainatphysics@gmail.com(hussainsha syed)")
print("welcome to avg calculator")

marks = (input("eneter each subject marks seperated by space\n").split())
for j in range(0, len(marks)):
    marks[j] = int(marks[j])
print(marks)
total = 0
for i in marks:
    total += i
print(total)
sub =0
for k in marks:
    sub+=1
print(sub)

print("the avg is", round(total/sub))


# a = sum(marks)/len(marks)
#
# print(round(a))

print()
but1 = print(input("press enter for bye"))

