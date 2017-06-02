"""Defines the Movie class that contains the details of a movie."""
import webbrowser

class Movie(object):
    """This class provides storage of movie related information."""

    def __init__(self,movie_title,poster_image,trailer_youtube):
        """Initialises Movie class instance variables.
        Args:
            title: A string variable to store the title of the movie.
            poster_image_url: A string variable to store the URL of the movie poster.
            trailer_youtube_url: A string variable to store the URL of the movie trailer.
        Returns:
                None
        Raises:
                No Exception
        """
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    def show_trailer(self):
        """Function Plays the movie trailer in web browser."""
        webbrowser.open(self.trailer_youtube_url)
