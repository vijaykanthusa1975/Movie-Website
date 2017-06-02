import fresh_tomatoes
import media
def main():
    """Main function to pass Title, Poster Image, Youtube URL to fresh_tomatoes.py
    Args:
        None
    Returns:
        None
    Raises:
        No Exception"""

    Alien_Covenant=media.Movie("Alien:Covenant","https://upload.wikimedia.org/wikipedia/en/3/33/Alien_Covenant_Teaser_Poster.jpg","https://www.youtube.com/watch?v=svnAD0TApb8")

    Guardians_of_the_Galaxy_Vol_2=media.Movie("Guardians of the Galaxy Vol. 2","https://upload.wikimedia.org/wikipedia/en/9/95/GotG_Vol2_poster.jpg","https://www.youtube.com/watch?v=dW1BIid8Osg")

    Wonder_Woman=media.Movie("Wonder Woman","https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg","https://www.youtube.com/watch?v=INLzqh7rZ-U")

    Snatched=media.Movie("Snatched","https://upload.wikimedia.org/wikipedia/en/c/ce/Snatched2017poster.jpg","https://www.youtube.com/watch?v=PsBWnst8f7w")

    King_Arthur_Legend_of_the_Sword=media.Movie("King Arthur Legend of the Sword","https://upload.wikimedia.org/wikipedia/en/a/a4/King_Arthur_LotS_poster.jpg","https://www.youtube.com/watch?v=jIM4-HLtUM0")

    Diary_of_a_Wimpy_Kid_The_Long_Haul=media.Movie("Diary of a Wimpy Kid: The Long Haul","https://upload.wikimedia.org/wikipedia/en/c/cd/Long_Haul_Poster.jpg","https://www.youtube.com/watch?v=3aNjdFjDzoI")

    The_Fate_of_the_Furious=media.Movie("The Fate of the Furious","https://upload.wikimedia.org/wikipedia/en/2/2d/The_Fate_of_The_Furious_Theatrical_Poster.jpg","https://www.youtube.com/watch?v=JwMKRevYa_M")

    The_Boss_Baby=media.Movie("The Boss Baby","https://upload.wikimedia.org/wikipedia/en/0/0e/The_Boss_Baby_poster.jpg","https://www.youtube.com/watch?v=Ud8j5GaqH3c")

    Beauty_and_the_Beast=media.Movie("Beauty and the Beast","https://upload.wikimedia.org/wikipedia/en/d/d6/Beauty_and_the_Beast_2017_poster.jpg","https://www.youtube.com/watch?v=e3Nl_TCQXuw")

    The_Circle=media.Movie("The Circle","https://upload.wikimedia.org/wikipedia/en/8/80/The_Circle_%282017_film%29.png","https://www.youtube.com/watch?v=QUlr8Am4zQ0")

    Gifted=media.Movie("Gifted","https://upload.wikimedia.org/wikipedia/en/f/fe/Gifted_film_poster.jpg","https://www.youtube.com/watch?v=x7CAjpdRaXU")

    Get_out=media.Movie("Get Out","https://upload.wikimedia.org/wikipedia/en/e/eb/Teaser_poster_for_2017_film_Get_Out.png","https://www.youtube.com/watch?v=sRfnevzM9kQ")

    movies=[Alien_Covenant,The_Circle,Gifted,Get_out,Wonder_Woman,Snatched,Guardians_of_the_Galaxy_Vol_2,King_Arthur_Legend_of_the_Sword,Diary_of_a_Wimpy_Kid_The_Long_Haul,The_Fate_of_the_Furious,The_Boss_Baby,Beauty_and_the_Beast]

    fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    main()
