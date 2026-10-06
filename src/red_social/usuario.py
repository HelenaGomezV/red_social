class Usuario:
    def __init__(self, nombre, alias):
        self.nombre = nombre

        if not alias.startswith("@"):
            alias = "@" + alias

        self.alias = alias
        self.seguidos = []

    def seguir(self, otro):
        if otro is self:
            raise ValueError("No puedes seguirte a ti mismo")

        if otro in self.seguidos:
            raise ValueError("Ya sigues a este usuario")
        
        self.seguidos.append(otro)