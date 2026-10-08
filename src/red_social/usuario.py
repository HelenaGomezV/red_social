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

    def sigue_a(self, otro):
        return otro in self.seguidos

    @property
    def numero_seguidos(self):
        return len(self.seguidos)

    def a_dict(self):
        return {
            "nombre": self.nombre,
            "alias": self.alias
        }

    @classmethod
    def desde_dict(cls, datos):
        return cls(datos["nombre"], datos["alias"])
    
    def __str__(self):
        return f"{self.nombre} ({self.alias})"

    def __eq__(self, otro):
        if not isinstance(otro, Usuario):
            return False

        return self.alias == otro.alias

