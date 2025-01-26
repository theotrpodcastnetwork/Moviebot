import requests
from bs4 import BeautifulSoup
import random

# Disclaimer
print("Note: This bot is for educational purposes only. Always respect website terms of service.")

# Mood to Genre Mapping
MOOD_GENRE = {
    'happy': ['comedy', 'musical'],
    'sad': ['drama', 'romance'],
    'adventurous': ['adventure', 'action'],
    'scared': ['horror', 'thriller'],
    'nostalgic': ['family', 'animation']
}

def get_genre(mood):
    return random.choice(MOOD_GENRE.get(mood.lower(), ['drama']))

def scrape_flixtor(search_query):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    try:
        # WARNING: This URL might need adjustment based on Flixtor's actual structure
        url = f"https://flixtor.to/search/{search_query}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # WARNING: These selectors are hypothetical - inspect Flixtor's actual HTML
        movies = []
        for item in soup.select('.movie-item'):  # Update selector
            title = item.select_one('.title').text.strip()  # Update selector
            year = item.select_one('.year').text.strip()  # Update selector
            link = item.find('a')['href']
            movies.append({'title': title, 'year': year, 'link': link})
        
        return movies[:5]  # Return top 5 results
    except Exception as e:
        print(f"Error fetching data: {e}")
        return []

def movie_bot():
    print("🎬 Movie Mood Bot 🍿\n")
    mood = input("How are you feeling today? (happy/sad/adventurous/scared/nostalgic): ")
    
    genre = get_genre(mood)
    print(f"\n🧠 I think {genre} movies might match your {mood} mood!")
    
    movies = scrape_flixtor(genre)
    
    if movies:
        print(f"\n🎥 Here are some {genre} movies from Flixtor.to:")
        for idx, movie in enumerate(movies, 1):
            print(f"{idx}. {movie['title']} ({movie['year']})")
            print(f"   🔗 {movie['link']}\n")
    else:
        print("\n😢 Couldn't find any movies right now. Try another mood!")

if __name__ == "__main__":
    movie_bot()