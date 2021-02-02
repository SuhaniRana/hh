def swapFileData():
    fileName1 = input("Enter first file name: ")
    fileName2 = input("Enter second file name: ")   
    data_a = open(fileName1,'r')
    data_b = open(fileName2,'r')
    data_a.write(fileName2)
    data_b.write(fileName1)


    swapFileData()

