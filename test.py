import requests

MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_API_KEY = "https://api.themoviedb.org/3/movie/550?api_key=f87635fa8f036875b3a29619b9638fdd"
access_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmODc2MzVmYThmMDM2ODc1YjNhMjk2MTliOTYzOGZkZCIsInN1YiI6IjYzZjM3NjQ4YTI0YzUwMDA4MDBjZTAyNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.A-ngLxbze6XpO6N0szHsdTPcpijm94Qgty52ctS-fJQ"
headers = {
    "Authorization": f"Bearer {access_token}"
}
MOVIE_DB_DETAILS_URL = "https://api.themoviedb.org/3/movie"


# movie_title = "the matrix"
# response = requests.get(MOVIE_DB_SEARCH_URL, params={"api_key": MOVIE_DB_API_KEY, "query": movie_title}, headers=headers)
# data = response.json()["results"]
#
movie_api_id = 624860
response = requests.get(url=f"https://api.themoviedb.org/3/movie/{movie_api_id}?api_key={MOVIE_DB_API_KEY}&language=en-US",
                        headers=headers)
data = response.json()
print (data)