# -*- coding: utf-8 -*-

import webbrowser

"""
    Modulo responsável por tratar e encapsular a classe Movie.
"""
class Movie():
    """
        Classe utiliziada para criar objetos com as informações de um filme.

        Atributtes:
            title (str): Titulo do filme.
            poster_image_url (str): Url que contém a imagem do poster do filme.
            trailer_youtube_url (str): Url do trailer do filme no youtube.
            director (str): Nome do diretor do filme.
            release_date (str): Data de lançamento do filme.
            runtime (str): Tempo de duração do filme.
    """

    def __init__(self, title, poster_image_url,
                 trailer_youtube_url, director,
                 release_date, runtime):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.director = director
        self.release_date = release_date
        self.runtime = runtime

    def show_trailer(self):
        """Função responsável por exibir o trailer do filme."""
        webbrowser.open(self.trailer_youtube_url)
