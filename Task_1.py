
try:
    with open("sample","rt") as f:
        line1=f.readline()
        line2=f.readline()
    print(f"this is the first line: {line1}")
    print(f"this is the second line: {line2}")
    f.close()

except FileNotFoundError:
    print("file not found")