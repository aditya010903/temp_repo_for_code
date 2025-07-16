# Strings 
a = "Hello"
print(a)


# Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


#Characters
a = "Hello, World!"
print(a[1])  #returns the character at index 1 whis is 'e'. String indexing starts at 0.


#looping through a string
for x in "banana":
  print(x)


#String length
a = "Hello, World!"
print(len(a))


#Check String
txt = "The best things in life are free!"
print("free" in txt)


#Slicing
b = "Hello, World!"
print(b[2:5])   #slicing from index 2 to 5  (5 not included) . Result is 'llo'

print(b[:5])    #slicing from the start to index 5 (5 not included). Result is 'Hello'

print(b[2:])    #slicing from index 2 to the end. Result is 'llo, World!'
