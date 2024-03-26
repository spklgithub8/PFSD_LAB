try:
    klu1=open("file.txt","r+")
    try:
        klu1.write("xyzthis is s17 of crt class")
    finally:
        klu1.close()
except IOError:
    print("File not found")
else:
    print("file opened successfully")
    klu1.close()