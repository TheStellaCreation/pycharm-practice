employee_file= open("employee", "r")
for employee in employee_file .readlines():
    print (employee)
#print (employee_file.readlines()[1])
#when use emoloyee_file.readline
#it only shows one line
employee_file .close()


