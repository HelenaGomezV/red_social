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