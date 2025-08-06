stu_list = []
stu_submit_list = []

for i in range(1, 31):
    stu_list.append(i)
    
for j in range(28):
    student_num = int(input())
    stu_submit_list.append(student_num)
stu_nosubmit_list = []

for num in stu_list:
    if num not in stu_submit_list:
        stu_nosubmit_list.append(num)
stu_nosubmit_list.sort()
print(stu_nosubmit_list[0])
print(stu_nosubmit_list[1])