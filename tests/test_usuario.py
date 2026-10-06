import pytest
from red_social.usuario import Usuario


def test_alias_empieza_por_arroba():
    ana = Usuario("Ana", "ana")

    assert ana.alias == "@ana"


def test_seguir_anade_usuario():
    ana = Usuario("Ana", "@ana")
    luis = Usuario("Luis", "@luis")

    ana.seguir(luis)

    assert luis in ana.seguidos

def test_seguirse_a_si_mismo_lanza_error():
    ana = Usuario("Ana", "@ana")

    with pytest.raises(ValueError):
        ana.seguir(ana)

def test_seguir_dos_veces_lanza_error():
    ana = Usuario("Ana", "@ana")
    luis = Usuario("Luis", "@luis")

    ana.seguir(luis)

    with pytest.raises(ValueError):
        ana.seguir(luis)


def test_sigue_a():
    ana = Usuario("Ana", "@ana")
    luis = Usuario("Luis", "@luis")

    assert ana.sigue_a(luis) is False

    ana.seguir(luis)

    assert ana.sigue_a(luis) is True
    assert luis.sigue_a(ana) is False


def test_numero_seguidos():
    ana = Usuario("Ana", "@ana")
    luis = Usuario("Luis", "@luis")

    assert ana.numero_seguidos == 0

    ana.seguir(luis)

    assert ana.numero_seguidos == 1