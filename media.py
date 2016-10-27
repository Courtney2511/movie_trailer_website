import webbrowser


class Movie():
    """ This class provides a way to store movie related information

        Attributes:
            movie_title (str): movie title
            movie_storyline (str): one line synopsis of movie
            poster_image_url (str): link to poster picture on wikipedia
            trailer_youtube (str): link to movie trailer on youTube """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
