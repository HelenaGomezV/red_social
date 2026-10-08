from red_social.publicacion import Tweet
from red_social.usuario import Usuario

class RedSocial:
    def __init__(self):
        self.usuarios = {}
        self.publicaciones = []

    def anadir(self, usuario):
        self.usuarios[usuario.alias] = usuario

    def registrar(self, nombre, alias):
        usuario = Usuario(nombre, alias)
        self.anadir(usuario)
        return usuario

    def publicar(self, publicacion):
        self.publicaciones.append(publicacion)
        return publicacion

    def timeline(self, usuario):
        usuarios_timeline = [usuario] + usuario.seguidos

        return [
            publicacion
            for publicacion in self.publicaciones
            if publicacion.autor in usuarios_timeline
    ]

    def tendencias(self):
        tendencias = {}

        for publicacion in self.publicaciones:
            for hashtag in publicacion.hashtags:
                tendencias[hashtag] = tendencias.get(hashtag, 0) + 1

        return tendencias

    def mostrar_timeline(self, usuario):
        for publicacion in self.timeline(usuario):
            print(publicacion)