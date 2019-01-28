# -*- coding: utf-8 -*-

import fresh_tomatoes
from media import Movie


# criação das instancias dos filmes
avangers_infinity_war = Movie("Avengers: Infinity War",
                              "https://upload.wikimedia.org/wikipedia/en/4/"
                              "4d/Avengers_Infinity_War_poster.jpg",
                              "https://www.youtube.com/watch?v=6ZfuNTqbHE8",
                              "Anthony Russo, Joe Russo",
                              "26 Apr 2018 (Brazil)",
                              "149 min")

logan = Movie("Logan",
              "https://upload.wikimedia.org/wikipedia/pt/"
              "2/2d/Filme_Logan_2017.jpg",
              "https://www.youtube.com/watch?v=KPND6SgkN7Q",
              "James Mangold",
              "2 Mar 2017 (Brazil)",
              "137 min")

star_wars_v = Movie("Star Wars: Episode V",
                    "https://upload.wikimedia.org/wikipedia/pt/thumb/5/5c"
                    "/The_Empire_Strikes_Back.jpg/"
                    "250px-The_Empire_Strikes_Back.jpg",
                    "https://www.youtube.com/watch?v=JNwNXF9Y6kY",
                    "Irvin Kershner",
                    "21 Jul 1980 (Brazil)",
                    "124 min")

the_godfather = Movie("The Godfather",
                      "https://m.media-amazon.com/images/M"
                      "/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZT"
                      "k3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg",
                      "https://www.youtube.com/watch?v=lLThoR1S0QQ",
                      "Francis Ford Coppola",
                      "10 Sep 1972 (Brazil)",
                      "175 min")

lord_of_the_ring_1 = Movie("The Lord of the Rings",
                           "https://m.media-amazon.com/images/M/"
                           "MV5BN2EyZjM3NzUtNWUzMi00MTgxLWI0NTctMzY4M2VlOTdjZ"
                           "WRiXkEyXkFqcGdeQXVyNDUzOTQ5MjY"
                           "@._V1_SY999_CR0,0,673,999_AL_.jpg",
                           "https://youtu.be/IUerKBZHnBs",
                           "Peter Jackson",
                           "1 Jan 2002 (Brazil)",
                           "178 min")

# lista que contém alguns de meus filmes favoritos
# que serão renderizados no navegador
movie_list = [avangers_infinity_war,
              logan,
              star_wars_v,
              the_godfather,
              lord_of_the_ring_1]

# função que abre uma página web com a lista de filmes
fresh_tomatoes.open_movies_page(movie_list)
