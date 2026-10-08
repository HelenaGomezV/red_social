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


def test_a_dict():
    ana = Usuario("Ana", "@ana")

    assert ana.a_dict() == {
        "nombre": "Ana",
        "alias": "@ana"
    }

def test_desde_dict():
    datos = {
        "nombre": "Ana",
        "alias": "@ana"
    }

    ana = Usuario.desde_dict(datos)

    assert ana.nombre == "Ana"
    assert ana.alias == "@ana"
    assert ana.seguidos == []

def test_str_usuario():
    ana = Usuario("Ana", "@ana")

    assert str(ana) == "Ana (@ana)"


def test_usuarios_son_iguales_si_tienen_mismo_alias():
    ana1 = Usuario("Ana", "@ana")
    ana2 = Usuario("Otra Ana", "@ana")
    luis = Usuario("Luis", "@luis")

    assert ana1 == ana2
    assert ana1 != luis


def test_alias_que_ya_tiene_arroba_no_cambia():
    ana = Usuario("Ana", "@ana")

    assert ana.alias == "@ana"