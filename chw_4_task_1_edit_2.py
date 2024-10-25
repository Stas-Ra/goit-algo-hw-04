# with open("G:\PROJECTS\.git\PROJECTS\PROJECTS\PROJECTS\salary_developers.txt", "w") as fh:
#     fh.write(
#         '''Alex Korp,3000
# Nikita Borisenko,2000
# Sitarama Raju,1000
# '''
#     )

from pathlib import Path

path = Path("G:/PROJECTS/.git/PROJECTS/PROJECTS/PROJECTS/salary_developers.txt") 


def total_salary(path):
       
    if path.exists():
        with open(path, "r", encoding="utf-8", errors="strict") as file:    

            salary = list()
            for line in file:
                salary.append(float(line.split(",")[1]))
            total, average = sum(salary), sum(salary)//len(salary)
            result = (total, average)
            print((f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}"))
            return result
        
    else:
        print("File not avialable") 
            
total_salary(path)
    


  