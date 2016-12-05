import fresh_tomatoes
import media as m

toy_story = m.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)
avatar = m.Movie("Avatar",
                 "A Marine on an alien planet",
                 "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                 "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)

always_sunny = m.Movie("It's Always Sunny in Philidelphia",
                       "Some friends own a bar",
                       "http://www.shopthetv.com/imgcache/product/resized/000/781/920/catl/its-always-sunny-in-philadelphia-season-10-giclee-print-452_305.jpg?k=ee5efe92&pid=781920&s=catl&sn=shoptv",
                       "https://www.youtube.com/watch?v=vVmAjkmZpJY")

#avatar.show_trailer()
#always_sunny.show_trailer()

#always_sunny.show_poster()
the_last_airbender = m.Movie("The Last Airbender",
                             "The Last Airbender must defeat the Firelord",
                             "https://images-na.ssl-images-amazon.com/images/I/51usRZ5aNIL._SY344_BO1,204,203,200_.jpg",
                             "https://www.youtube.com/watch?v=dMnDkFktGF4")

banshee = m.Movie("Banshee",
                  "A man poses as a Sherriff",
                  "http://www.impawards.com/tv/posters/banshee_cinemax.jpg",
                  "https://www.youtube.com/watch?v=-fvSG8KmWTY")

dr_horrible = m.Movie("Dr. Horrible's Sing-Along Blog",
                      "A mad scientist attempts to woo a woman",
                      "https://images-na.ssl-images-amazon.com/images/I/512IePeoDvL.jpg",
                      "https://www.youtube.com/watch?v=0nn0zSbn7gc")
movies = [toy_story, avatar, always_sunny, the_last_airbender, banshee, dr_horrible]
#fresh_tomatoes.open_movies_page(movies)
#print(m.Movie.VALID_RATINGS)
print(m.Movie.__module__)

                             
                 
