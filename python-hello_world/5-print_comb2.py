#where {i:02d} means 2digit. 'end' means end with ','
for i in range(100):
    print(f"{i:02d}", end=", " if i < 99 else "\n")
