# coding: utf-8
import subscription

# this read the settings of add on
settings = subscription.Settings()
# settings.movie_folder = to save the movies
# settings.show_folder = to save the tv shows

# define the browser to open URL
browser = subscription.Browser()
# browser.open(url)
# url to open
# return true if it is 200 status
# browser.status : status and error
# browser.content : content html
# browser.login(url, payload, verification expression): open a page and do the login, return true if can login
# url login page
# payload dictionary {'username': username, 'pass', password, ..} all the variable from the FORM
# verification expression, string to check it couldn't login, like incorrect username and password.


# subscribing TV shows
listing = ['Game of thrones', 'The Simpsons']  # example from list tv shows
ID = [] # empty for tv shows
subscription.integration(listing, ID,'SHOW', settings.show_folder)

# subscribing Movies without IMDB_ID
listing = ['Frozen (2013)', 'Guardians of the Galaxy (2014)']  # example from list movies, it is better to have the year
ID = [] # IMDB_ID, if it is empty the function will figure it out
subscription.integration(listing, ID,'MOVIE', settings.movie_folder)

# subscribing Movies with IMDB_ID
listing = ['Edge of tomorrow', 'Gone girl']  # example from list movies, the year isn't necessary
ID = ['tt1631867', 'tt2267998'] # IMDB_ID, if it is empty the function will figure it out
subscription.integration(listing, ID,'MOVIE', settings.movie_folder)
