file=open('new.txt',"w")

lines=[" Beautiful is better than ugly.\n", "Explicit is better than implicit.\n", "Simple is better than complex.\n", "Complex is better than complicated.\n"]

file.writelines(lines)
file.close()