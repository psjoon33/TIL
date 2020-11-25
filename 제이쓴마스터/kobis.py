class URLMaker:

    url = 'https://api.themoviedb.org/3/movie/top_rated'
    # url = 'https://api.themoviedb.org/3/genre/movie/list'
    key = 'c94ff0a895a99423430945754296e797'

    def __init__(self, key):
        self.key = key

    def get_url(self):
        return f'{self.url}?api_key={self.key}&language=ko-KR'