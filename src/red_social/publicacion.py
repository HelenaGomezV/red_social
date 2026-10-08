from abc import ABC, abstractmethod
from red_social.usuario import Usuario


LIMITE_CARACTERES = 280

class Publicacion(ABC):
    def __init__(self, autor, texto):
        if not texto.strip():
            raise ValueError("El texto no puede estar vacío")

        if len(texto) > LIMITE_CARACTERES:
            raise ValueError("El texto supera los 280 caracteres")

        self.autor = autor
        self.texto = texto
        self.me_gusta = 0

    def dar_me_gusta(self):
        self.me_gusta += 1

    @property
    def hashtags(self):
        return self.extraer_hashtags(self.texto)

    @staticmethod
    def extraer_hashtags(texto):
        hashtags = []

        for palabra in texto.split():
            if palabra.startswith("#") and len(palabra) > 1:
                hashtag = palabra.lower().rstrip(",.;:!?¡¿")

                if hashtag not in hashtags:
                    hashtags.append(hashtag)

        return hashtags

class Tweet(Publicacion):
    def __str__(self):
        return f"{self.autor.alias}: {self.texto}"
