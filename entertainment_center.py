# -*- coding: utf-8 -*-

import fresh_tomatoes
from media import Movie


# criação das instancias dos filmes

# o comentário #noqa faz com que o pep-8
# ignore a linha em que ele foi inserido
avangers_infinity_war = Movie("Avengers: Infinity War",
                              "https://bit.ly/2KjSEUq",
                              "https://www.youtube.com/watch?v=6ZfuNTqbHE8",  # noqa
                              "Anthony Russo, Joe Russo",
                              "26 Apr 2018 (Brazil)",
                              "149 min")

logan = Movie("Logan",
              "https://bit.ly/2t2f5op",
              "https://www.youtube.com/watch?v=KPND6SgkN7Q",   # noqa
              "James Mangold",
              "2 Mar 2017 (Brazil)",
              "137 min")

star_wars_v = Movie("Star Wars: Episode V",
                    "https://bit.ly/2TjmdcV",
                    "https://www.youtube.com/watch?v=JNwNXF9Y6kY",   # noqa
                    "Irvin Kershner",
                    "21 Jul 1980 (Brazil)",
                    "124 min")

the_godfather = Movie("The Godfather",
                      "https://bit.ly/2FSEAmu",
                      "https://www.youtube.com/watch?v=lLThoR1S0QQ",  # noqa
                      "Francis Ford Coppola",
                      "10 Sep 1972 (Brazil)",
                      "175 min")

lord_of_the_ring_1 = Movie("The Lord of the Rings",
                           "https://bit.ly/2zKhRDI",
                           "https://youtu.be/IUerKBZHnBs",  # noqa
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
