# -*- coding: utf-8 -*-

import webbrowser

"""
    Classe responsável por encapsular as informações de um filme
"""
class Movie():

    def __init__(self, title, poster_image_url,
                 trailer_youtube_url, director,
                 release_date, runtime):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.director = director
        self.release_date = release_date
        self.runtime = runtime

    # função responsável por exibir o trailer do filme
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
