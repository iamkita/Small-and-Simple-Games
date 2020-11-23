print("Hey you, yes you. Give us your favorite songs.")
print("Hit enter after each song. 'q' to quit 'r' to remove.")
favs= []
while True:
    data= input()
    if str.lower(data)== "q":
        break 
    elif str.lower(data)== "r":
        print("Removing:", favs.pop())
    else:
        favs.append(data)
    print(favs)
for song in favs:
    print("You said: ", song)
