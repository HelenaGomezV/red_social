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

def test_dar_me_gusta_incrementa_contador():
    ana = Usuario("Ana", "@ana")
    publicacion = PublicacionPrueba(ana, "Hola")

    assert publicacion.me_gusta == 0

    publicacion.dar_me_gusta()

    assert publicacion.me_gusta == 1

    publicacion.dar_me_gusta()

    assert publicacion.me_gusta == 2


@pytest.mark.parametrize("texto, esperado", [
    ("Hola #Python", ["#python"]),
    ("#Python es #Genial", ["#python", "#genial"]),
    ("Hola #Python, qué tal", ["#python"]),
    ("#Python #python #PYTHON", ["#python"]),
    ])

def test_extraer_hashtags(texto, esperado):
    assert PublicacionPrueba.extraer_hashtags(texto) == esperado