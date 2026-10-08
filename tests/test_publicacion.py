import pytest

from red_social.publicacion import Publicacion, Tweet, Respuesta, Retweet


class PublicacionPrueba(Publicacion):
    def __str__(self):
        return self.texto


def test_publicacion_guarda_datos(ana):
    publicacion = PublicacionPrueba(ana, "Hola")

    assert publicacion.autor == ana
    assert publicacion.texto == "Hola"
    assert publicacion.me_gusta == 0


@pytest.mark.parametrize("texto", [
    "",
    " ",
    "a" * 281,
])
def test_texto_invalido_lanza_error(ana, texto):
    with pytest.raises(ValueError):
        PublicacionPrueba(ana, texto)


def test_dar_me_gusta_incrementa_contador(ana):
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


def test_tweet_str(ana):
    tweet = Tweet(ana, "Hola mundo")

    assert str(tweet) == "@ana: Hola mundo"


def test_respuesta_str(ana, luis, tweet):
    respuesta = Respuesta(luis, "¡Hola Ana!", tweet)

    assert respuesta.original == tweet
    assert str(respuesta) == "@luis ↩ @ana: ¡Hola Ana!"


def test_retweet_comparte_el_texto_del_original(ana, luis, tweet):
    retweet = Retweet(luis, tweet)

    assert retweet.original == tweet
    assert retweet.texto == tweet.texto
    assert retweet.hashtags == tweet.hashtags