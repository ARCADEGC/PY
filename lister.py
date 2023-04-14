import os
import time
import csv

def number_of_arguments(arguments):
     return len(arguments)

run = 1
ls = []
with open("lister.csv", "r") as csvfile:
        datas = csv.reader(csvfile, delimiter = ",")
        print(datas)
        for data in datas:
            ls.append(str(data[0]))

os.system('cls')
print("\n\t Use \"done\" to delete an element or \"exit\" to close the program.")
print("\n\t To delete the last element fastly or safely, you can use the number 0 or add 1.")

while run == 1:

    article = input("\n\n\t Set article: ")
    ls.append(article)
    print("\n")

    if ls[-1] == "exit":
        exit()
    
    done = 0
    if ls[-1] == "done":

        try:
            done = int(input("\t What is done: ")) - 1
            ls.pop(done)
            ls.pop(-1)  

        except ValueError:
            print("\n\n\t Value must be a number!")
            ls.pop(-1)
            time.sleep(1)
            
        except IndexError:
            print("\n\n\t Value must be in range!")
            ls.pop(-1)
            time.sleep(1)  
      

    os.system('cls')
    i = 0
    while i < number_of_arguments(ls):

        with open("lister.csv", "w", newline = "") as csvfile:
            writer = csv.writer(csvfile, delimiter = ",")
            set_row = 0
            while set_row <= i:
                writer.writerow([ls[set_row]])
                set_row += 1

        print("\t", str(i + 1) + ".", ls[int(i)])
        i += 1