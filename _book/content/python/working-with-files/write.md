def writeFile(file_name, callback):
    some_file = open(file_name, 'w') # w means write text in to file
    some_file.write('Gabriel Godoy\n')
    some_file.write('Front end engineer')
    some_file.close()
    callback(file_name)
