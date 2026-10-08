class RedSocial:
    def __init__(self):
        self.usuarios = {}
        self.publicaciones = []

    def anadir(self, usuario):
        self.usuarios[usuario.alias] = usuario