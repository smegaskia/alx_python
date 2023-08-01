for i in range(99):
    print("{:02d} = 0x{:02x}".format(i, i), end=", " if i < 98 else "\n")
