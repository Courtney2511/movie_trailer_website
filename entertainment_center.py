import media
import fresh_tomatoes

# create 6 movie objects
bad_moms = media.Movie("Bad Moms",
                       "These moms like to party",
                       "https://upload.wikimedia.org/wikipedia/en/7/70/Bad_Moms_poster.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=P0FNjPsANGk")

wedding_crashers = media.Movie("Wedding Crashers",
                               "A hilarious tale of two guys that crash"
                               "weddings for fun",
                               "https://upload.wikimedia.org/wikipedia/en/3/3e/Wedding_crashers_poster.jpg",  # NOQA
                               "https://www.youtube.com/watch?v=ZeUSo8voIXM")

old_school = media.Movie("Old School",
                         "A group of old guys start a fraternity",
                         "https://upload.wikimedia.org/wikipedia/en/2/21/Old_s_poster.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=VqtymOtKr48")

blue_valentine = media.Movie("Blue Valentine",
                             "A tragic tale of the dissolution of love and"
                             " marriage",
                             "https://upload.wikimedia.org/wikipedia/en/0/04/Blue_Valentine_film.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=3oiY7W7nDeE")

days_of_summer = media.Movie("500 Days of Summer",
                             "an entertaining look at unrequited love",
                             "https://upload.wikimedia.org/wikipedia/en/d/d1/Five_hundred_days_of_summer.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=PsD0NpFSADM")

gone_with_the_wind = media.Movie(
                    "Gone With The Wind",
                    "An epic tale of the old south and Civil War",
                    "https://upload.wikimedia.org/wikipedia/commons/2/27/Poster_-_Gone_With_the_Wind_01.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=8mM8iNarcRc")


# Store all the movies in an array
movies = [bad_moms, wedding_crashers, old_school, blue_valentine,
          days_of_summer, gone_with_the_wind]

# Display movies and trailers in the browswer
fresh_tomatoes.open_movies_page(movies)
