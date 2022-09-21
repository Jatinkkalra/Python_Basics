
print("#️⃣#️⃣ File Handling \n")

print("#️⃣ Printing other file data using r (read) method")
file_read_Text_Data = open("File Handling - Text Data", "r")

print(file_read_Text_Data.read())
print()

print("#️⃣ Writing new data in other file using w (write) method \n"
      "| Also creating a new file directly")
file_write_new = open("File Handling - New File", "w")
print(file_write_new.write("This a new file\n"))
print()

print("#️⃣ Appending new data in other file using a (append) method")
file_append_new = open("File Handling - New File", "a")
print(file_append_new.write("next line \n"))
print()

print("#️⃣ Printing data using loop")
for data in file_read_Text_Data:
    print(data)
print()

print("#️⃣ Printing data using loop in a new file")
for data in file_read_Text_Data:
    file_write_new.write(data)
print()
