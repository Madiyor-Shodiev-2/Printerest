x = "Hello my beatiful friend ''''''"
x = """Lorem ajsladskads
kasjdkasjdkajsdj kasjd \n\n\n\n
jkasdjaksjdlasjdlk'''asjd j
ka;sldjaksjdkasjdasjd jkas.\n\n\n"""
x = '''Lorem ajsladskads \n
kasjdkasjdkajsdj kasjd \n\n\n\a \\
jkasdjaksjdlasjdlk'' 'asjd j
ka;sldjaksjdkasjdasjd jkas.'''

x = "Hello World"

for i in x:
    print(i)

print(x[1])
print(len(x))
print("ello" in x)

if "Hello" in x:
    print("Nice to meet you!")

if "Bye bye" not in x:
    print("Yes, you welcome")

print("Bye bye" not in x)