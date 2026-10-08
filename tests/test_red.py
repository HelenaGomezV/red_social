from red_social.publicacion import Tweet
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

def test_publicar_anade_publicacion():
    red = RedSocial()
    ana = Usuario("Ana", "@ana")
    tweet = Tweet(ana, "Hola mundo")

    resultado = red.publicar(tweet)

    assert resultado == tweet
    assert tweet in red.publicaciones

def test_timeline_muestra_publicaciones_del_usuario_y_seguidos():
    red = RedSocial()

    ana = Usuario("Ana", "@ana")
    luis = Usuario("Luis", "@luis")
    marta = Usuario("Marta", "@marta")

    red.anadir(ana)
    red.anadir(luis)
    red.anadir(marta)

    ana.seguir(luis)

    tweet_ana = Tweet(ana, "Tweet de Ana")
    tweet_luis = Tweet(luis, "Tweet de Luis")
    tweet_marta = Tweet(marta, "Tweet de Marta")

    red.publicar(tweet_ana)
    red.publicar(tweet_luis)
    red.publicar(tweet_marta)

    timeline = red.timeline(ana)

    assert tweet_ana in timeline
    assert tweet_luis in timeline
    assert tweet_marta not in timeline

def test_tendencias_cuenta_hashtags():
    red = RedSocial()

    ana = Usuario("Ana", "@ana")
    luis = Usuario("Luis", "@luis")

    tweet1 = Tweet(ana, "Hola #Python")
    tweet2 = Tweet(luis, "Aprendiendo #Python y #Programacion")

    red.publicar(tweet1)
    red.publicar(tweet2)

    tendencias = red.tendencias()

    assert tendencias == {
        "#python": 2,
        "#programacion": 1,
    }
def test_mostrar_timeline(capsys):
    red = RedSocial()

    ana = Usuario("Ana", "@ana")
    tweet = Tweet(ana, "Hola mundo")

    red.publicar(tweet)

    red.mostrar_timeline(ana)

    captured = capsys.readouterr()

    assert "@ana: Hola mundo" in captured.out


def test_desde_json_carga_usuarios_y_seguimientos(mocker):
    contenido = """
    {
        "usuarios": [
            {"nombre": "Ana", "alias": "@ana"},
            {"nombre": "Luis", "alias": "@luis"}
        ],
        "seguimientos": [
            ["@luis", "@ana"]
        ]
    }
    """

    mocker.patch(
        "builtins.open",
        mocker.mock_open(read_data=contenido)
    )

    red = RedSocial.desde_json("datos/usuarios.json")

    assert "@ana" in red.usuarios
    assert "@luis" in red.usuarios
    assert red.usuarios["@luis"].sigue_a(red.usuarios["@ana"])

def test_len_red_social():
    red = RedSocial()

    red.registrar("Ana", "@ana")
    red.registrar("Luis", "@luis")

    assert len(red) == 2
