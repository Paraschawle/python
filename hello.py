# it is use for comment 
name = input("what's your name ? ")
#print("hello, " + name  ) this is a one step for only one line to print

#print("hello, ", name ,end=""  ) this is second thing for print


# Remove whitespace frm str
# name= name.strip()

# capatilize user name 
#name= name.title()
# doing capatalize and strip both we  can add them on first line after name input to reduce the size or line of code
name= name.strip().title()
print(f"hello, {name}")
