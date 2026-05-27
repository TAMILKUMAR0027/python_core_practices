try:
    f = open("test.txt", "w")
    try:
        f.write("Hello")
    finally:
        print("File closed")
        f.close
except IOError:
    print("can't open")
else:
    print("There is no error")
finally:
    print("The progeam is finished]")
