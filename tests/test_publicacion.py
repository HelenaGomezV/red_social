import pytest

from red_social.publicacion import Publicacion
from red_social.usuario import Usuario


class PublicacionPrueba(Publicacion):
    def __str__(self):
        return self.texto


def test_publicacion_guarda_datos():
    ana = Usuario("Ana", "@ana")

    publicacion = PublicacionPrueba(ana, "Hola")

    assert publicacion.autor == ana
    assert publicacion.texto == "Hola"
    assert publicacion.me_gusta == 0


@pytest.mark.parametrize("texto", [
    "",
    " ",
    "a" * 281,
])
def test_texto_invalido_lanza_error(texto):
    ana = Usuario("Ana", "@ana")

    with pytest.raises(ValueError):
        PublicacionPrueba(ana, texto)