import fresh_tomatoes
import media

how_to_lose_a_guy_in_ten_days = media.Movie("How to lose a guy in 10 days", 
                                            "A story of a girl lsing a guy in 10 days",
                                            "https://i.jeded.com/i/how-to-lose-a-guy-in-10-days.17692.jpg",
                                            "https://www.youtube.com/watch?v=EFGr2_cOOTk")

the_lion_witch_and_wardrobe = media.Movie("The Lion, Witch, and Wardrobe", 
                                             "Four kids travel to the land of Narnia",
                                             "http://www.impawards.com/2005/posters/chronicles_of_narnia_the_lion_the_witch_and_the_wardrobe_xlg.jpg",
                                             "https://www.youtube.com/watch?v=lWKj41HZBzM")


pearl_harbor = media.Movie("Pearl Harbor", 
                            "The attack on Pearl Harbor",
                             "http://s3.amazonaws.com/kidzworld_photo/images/2016510/4924475e-ebea-4fec-acc0-9cb2169d66a1/pearl-harbor-poster.jpg",
                             "https://www.youtube.com/watch?v=yzK0GBEkFxc")

passengers = media.Movie("Passengers", 
                         "2 Passengers stuck in space for 90 years",
                         "http://www.impawards.com/2016/posters/passengers_xlg.jpg",
                         "https://www.youtube.com/watch?v=7BWWWQzTpNU")

intersteller = media.Movie("Intersteller", 
                         "Intersteller space travel",
                         "https://www.mauvais-genres.com/19056-thickbox_default/interstellar-french-movie-poster-15x21-2014-christopher-nolan-matthew-mcconaughey.jpg",
                         "https://www.youtube.com/watch?v=2LqzF5WauAw")

the_hobbit = media.Movie("The Hobbit", 
                         "A hobbit goes on an adventure",
                         "http://i.huffpost.com/gen/784488/thumbs/o-THE-HOBBIT-POSTER-570.jpg?7",
                         "https://www.youtube.com/watch?v=JTSoD4BBCJc")

movies = [how_to_lose_a_guy_in_ten_days, the_lion_witch_and_wardrobe, pearl_harbor, passengers, intersteller, the_hobbit]
fresh_tomatoes.open_movies_page(movies)
