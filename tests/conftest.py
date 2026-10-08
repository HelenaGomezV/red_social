import pytest

from red_social.usuario import Usuario
from red_social.publicacion import Tweet
from red_social.red import RedSocial


@pytest.fixture
def ana():
    return Usuario("Ana", "@ana")


@pytest.fixture
def luis():
    return Usuario("Luis", "@luis")


@pytest.fixture
def tweet(ana):
    return Tweet(ana, "Hola mundo")


@pytest.fixture
def red():
    return RedSocial()