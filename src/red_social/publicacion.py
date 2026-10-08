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
