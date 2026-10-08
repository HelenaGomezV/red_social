from red_social.red import RedSocial
from red_social.usuario import Usuario



def test_red_social_empieza_vacia():
    red = RedSocial()

    assert red.usuarios == {}
    assert red.publicaciones == []

def test_anadir_usuario():
    red = RedSocial()
    ana = Usuario("Ana", "@ana")

    red.anadir(ana)

    assert red.usuarios["@ana"] == ana

def test_registrar_usuario():
    red = RedSocial()

    ana = red.registrar("Ana", "@ana")

    assert ana.nombre == "Ana"
    assert ana.alias == "@ana"
    assert red.usuarios["@ana"] == ana