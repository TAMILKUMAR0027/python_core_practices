l1 = [1, 2, 3, 4, 5]
while True:
    print(
        "1. Append\n 2. Insert\n 3. Append alist\n  4. Modify\n 5. Delete by index\n 6. Delete by value\n 7. Sort ascending\n 8. sort descending\n 9. Display\n 10. Exit"
    )
    choice = int(input("Enter the choice: "))
    if choice == 1:
        l1.append(int(input()))
    elif choice == 2:
        l1.insert(int(input()), int(input()))
    elif choice == 3:
        l1.extend([int(input()), int(input())])
    elif choice == 4:
        l1[0] = int(input())
    elif choice == 5:
        del l1[int(input())]
    elif choice == 6:
        l1.remove(int(input()))
    elif choice == 7:
        l1.sort()
    elif choice == 8:
        l1.sort(reverse=True)
    elif choice == 9:
        print(l1)
    elif choice == 10:
        print("Thank you")
        break
    else:
        print("Enter the valid input")
