# with open("G:\PROJECTS\.git\PROJECTS\PROJECTS\PROJECTS\salary_developers.txt", "w") as fh:
#     fh.write(
#         '''Alex Korp,3000
# Nikita Borisenko,2000
# Sitarama Raju,1000
# '''
#     )

from pathlib import Path
def total_salary(path):

        with open(path, "r", encoding="utf-8", errors="strict") as file:
            if not file:
                return "No file avialable"
            else:
                salary = list()
                for line in file:
                    salary.append(float(line.split(",")[1]))
                return (sum(salary), sum(salary)//len(salary))
    
total, average = total_salary("salary_developers.txt")
  
print((f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}"))