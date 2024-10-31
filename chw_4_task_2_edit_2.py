# with open("G:\PROJECTS\.git\PROJECTS\PROJECTS\PROJECTS\cats_info.txt", "w") as file:
#     file.write(
#         """60b90c1c13067a15887e1ae1,Tayson,3
# 60b90c2413067a15887e1ae2,Vika,1
# 60b90c2e13067a15887e1ae3,Barsik,2
# 60b90c3b13067a15887e1ae4,Simon,12
# 60b90c4613067a15887e1ae5,Tessi,5
# """
#     )


from pathlib import Path


def get_cats_info(path):

    try:

        with open(path, "r", encoding="utf-8", errors="replace") as file:
            cats_info = []

            for line in file:
                cat_info = {"id": "", "name": "", "age": ""}
                cat_info["id"] = line.split(",")[0]
                cat_info["name"] = line.split(",")[1]
                cat_info["age"] = line.split(",")[2].strip()
                cats_info.append(cat_info)
            return cats_info
        
    except Exception as e:
        return "Enter a valid file path"
            
cats_info = get_cats_info("C:/Users/Stas/Videos/mp4.txt")
print(cats_info)



            


                
