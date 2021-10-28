import os




def rename(dir):
    os.chdir(dir)
    old_names = os.listdir()
    # print(old_names)

    number = 100
    for old_name in old_names:
        #new_name = str(number) + old_name[3:]
        new_name = old_name[1:]

        #temp = old_name.split()
        #new_name = " 厨余垃圾 ".join(temp)



        print(new_name)

        os.rename(old_name, new_name)
        number += 1


if __name__ == "__main__":
    dir = r"C:\Users\Frostbite\Desktop\Garbage50\\train"
    rename(dir)