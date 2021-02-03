import requests

class the_movie_db:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3"
        self.api_key = "e8a9d5f82d78ca210c8076d648685c12"

    def get_populars(self):
        response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()

    def get_search_results(self, keyword):
        response = requests.get(f"{self.api_url}/search/keyword?api_key={self.api_key}&query={keyword}&page=1")
        return response.json()

movie_api = the_movie_db()

while True:
    choose = input("1 - Popüler filmler\n2 - Film ara\n3 - Çıkış\nSeçiminiz :")

    if choose == "3":
        break
    else:
        if choose == "1":
            movies = movie_api.get_populars()
            for movie in movies["results"]:
                print(movie["title"])
        elif choose == "2":
            keyword = input("Aramak istediğiniz filmle ilgili kelime giriniz :")
            movies = movie_api.get_search_results(keyword)
            for movie in movies["results"]:
                print(movie["name"])
         