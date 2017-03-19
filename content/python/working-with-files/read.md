import write


def readFile(file_to_read):
    file = open(file_to_read, 'r')
    content = file.read()
    print(content)
    file.close()


write.writeFile('sample.txt', readFile)
