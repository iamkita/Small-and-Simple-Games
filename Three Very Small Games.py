####Fav scientist quiz####
print("What is your name?")
name= input()
print("Hello, " + name)
print("Who's your favorite scientist?")
fav_scientist= input()
print("Give us another name.")
fav_scientist_second= input()
print(fav_scientist, "and",  fav_scientist_second, "are your favorite scientists.")
print("Thanks for playing")

####Are you an adult?####
print ("What is your age?")
age=int(input())
if age > 65:
    print("So, you are a senior citizen")
elif age > 17:
    print("You are an adult!!!")
else:
    print("You are not an adult!!!")

####What are you searching for?####
things= ["dress", "tab", "book", "mobile", "laptop", "ghost", "pen"]
print("What are you searching for?")
ans=input()
for thing in things:
      if thing == ans:
        print("We found " + ans)
        break 
else:
    print("Not found")
