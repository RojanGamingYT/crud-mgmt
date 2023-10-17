import os,sqlite3

answer = int(input("Enter Module (1: Create, 2: Read, 3: Update, 4: Delete):"))

def create():
    with open('data.txt', 'w') as f:
        data = input("Enter Your Data:")
        f.write(f"{data}\n")
        print("Create Successful")

def read():
    with open('data.txt', 'r') as f:
        content = f.read()
        print(content)

def update():
    with open('data.txt', 'a') as f:
        data = input("Enter Your Data:")
        f.write(f"{data}\n")
        print("Update Successful")

def delete():
    with open('data.txt', 'w') as f:
        f.write(" ")
        print("Delete Successful")

def main():
    if answer == 1:
        create()
    elif answer == 2:
        read()
    elif answer == 3:
        update()
    elif answer == 4:
        delete()
    else:
        print("Invalid option")

main()