file_handle= open("textfile.txt", "r")
print(file_handle.read())

with open ("textfile.txt", "r") as file_handle, open ("textfile2.txt", "w") as file2:
    data = file_handle.read()
    file2.write(data)

with open("textfile.txt", "r") as file_handle, open("textfile.txt", "w") as file2:
    data += "\nDon't worry, be happy now"
    file2.write(data)
file_handle.close()