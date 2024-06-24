import random
import webbrowser

greetings = ["Welcome! What kind of music are you into?, pop, rock, hip hop, electronic, classical, lofi", "What kind of music like to hear?  pop, rock, hip hop, electronic, classical, lofi" ]
farewells = ["Bye for now!", "See you later!", "Have a great day!"]
music_genres = ["pop", "rock", "hip hop", "electronic", "classical", "lofi" ]

popular_songs = {  # Dictionary for predefined playlists (optional)
    "pop": ["https://www.youtube.com/playlist?list=PLMC9KNkIncKvYin_USF1qoJQnIyMAfRxl"],
    "rock": ["https://www.youtube.com/playlist?list=PLyORnIW1xT6wFALM5dZlkFhOULbToFok3"],
    "hip hop":["https://www.youtube.com/playlist?list=PLJtpjlkBVF4wneUJqC9SZPhBiEBQmmEsi"],
    "electronic":["https://www.youtube.com/playlist?list=PL7wr9BYcCCyNb0IhqqebdLEMkklMSOttA"],
    "classical":["https://www.youtube.com/playlist?list=PL6iA3a5UwHSc2XxuV_X-QkP42LLStcUt6"],
    "lofi":["https://www.youtube.com/playlist?list=PLy5uJRaX9m1i8-w2lNNDRndd_RhElX3EQ"]
    # Add more genres and songs
}


def greet():
    """Greets the user with a random greeting message."""
    print(random.choice(greetings))


def farewell():
    """Bids farewell to the user with a random farewell message."""
    print(random.choice(farewells))


def recommend_music(genre):
    
    
    if "music" in genre:  # Check if user specified a song/artist
        search_query = genre.strip()
    else:
        if genre.lower() in music_genres:  # Check for predefined genre
            if popular_songs:  # Use predefined playlist if available
                song_url = random.choice(popular_songs[genre])
                webbrowser.open(song_url)
                print(f"Here's some {genre.capitalize()} music for you to enjoy!")
            else:  # Fallback to YouTube search
                search_query = f"{genre} music"
        else:
            raise ValueError(f"Sorry, I don't have recommendations for {genre.capitalize()} yet. "
                              f"Tell me if there are other genres you'd like to explore!")

    webbrowser.open(f"https://www.youtube.com?search_query={search_query}")
    print(f"Here are some results for '{search_query}' on YouTube!")


def main():
    """Main conversation loop for the chatbot."""
    greet()
    while True:
        user_input = input("You: ").lower().strip()
        if user_input in ("bye", "exit", "quit"):
            farewell()
            break
        else:
            try:
                recommend_music(user_input)
            except ValueError as e:
                print(e)


if __name__ == "__main__":
    main()
