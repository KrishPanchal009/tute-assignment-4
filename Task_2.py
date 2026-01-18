text = input("Enter text to write to the file: ")

with open("output", "wt") as file:
    file.write(text+"\n")

print("Data successfully written to output.txt.")


append_text = input("\nEnter additional text to append: ")

with open("output", "at") as file:
    file.write(append_text)

print("Data successfully appended.")


print("\nFinal content of output.txt:")

with open("output", "rt") as file:
    print(file.read())
