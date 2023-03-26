def favorite_book(title):
    print(f"One of my favorite books is {title}.")

favorite_book("Rich dad Poor Dad")

def make_shirt(size, message):
    print(f"A {size} shirt will be printed with the message: {message}")

make_shirt("medium", "Hello, World!")
make_shirt(size="small", message="Hello Hassan!")

def make_shirt1(message="I love Python", size="large"):
    print(f"A {size} shirt will be printed with the message: {message}")

make_shirt1() 
make_shirt1(size="medium") 
make_shirt1(message="Hello, World!", size="small") 

def make_album(artist, title, num_tracks=None):
    album = {"artist": artist, "title": title}
    if num_tracks:
        album["num_tracks"] = num_tracks
    return album

# Example usage:
album1 = make_album("Taylor Swift", "Folklore")
album2 = make_album("Ed Sheeran", "÷ (Divide)", 12)
album3 = make_album("Ariana Grande", "Positions", 14)

print(album1)
print(album2)
print(album3)


