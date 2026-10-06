class Usuario:
    def __init__(self, nombre, alias):
        self.nombre = nombre
        
        if not alias.startswith("@"):
            alias = "@" + alias

        self.alias = alias
        self.seguidos = []