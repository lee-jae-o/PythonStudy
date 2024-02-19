import requests

def search_movie(api_key, movie_title):
    base_url = "http://www.omdbapi.com/"
    params = {"apikey": api_key, "t": movie_title}

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200 and data["Response"] == "True":
        print("Title:", data["Title"])
        print("Year:", data["Year"])
        print("Genre:", data["Genre"])
        print("Plot:", data["Plot"])
    else:
        print("Movie not found or there was an error.")

def main():
    omdb_api_key = "5a3f73e9"
    movie_title = input("Enter the movie title: ")

    search_movie(omdb_api_key, movie_title)

if __name__ == "__main__":
    main()