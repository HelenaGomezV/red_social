from red_social.usuario import Usuario
import json

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

    @classmethod
    def desde_json(cls, ruta):
        with open(ruta, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        red = cls()

        for datos_usuario in datos["usuarios"]:
            usuario = Usuario.desde_dict(datos_usuario)
            red.anadir(usuario)

        for alias_seguidor, alias_seguido in datos["seguimientos"]:
            red.usuarios[alias_seguidor].seguir(
                red.usuarios[alias_seguido]
            )

        return red

    def __len__(self):
        return len(self.usuarios)

    def __iter__(self):
        return iter(sorted(self.usuarios.values(), key=lambda usuario: usuario.alias))
    
    def __contains__(self, alias):
        return alias in self.usuarios

    def __getitem__(self, alias):
        return self.usuarios[alias]