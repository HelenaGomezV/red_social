from red_social.publicacion import Tweet
from red_social.red import RedSocial
from red_social.usuario import Usuario


def test_red_social_empieza_vacia(red):
    assert red.usuarios == {}
    assert red.publicaciones == []


def test_anadir_usuario(red, ana):
    resultado = red.anadir(ana)

    assert resultado == ana
    assert red.usuarios["@ana"] == ana


def test_registrar_usuario(red):
    ana = red.registrar("Ana", "@ana")

    assert ana.nombre == "Ana"
    assert ana.alias == "@ana"
    assert red.usuarios["@ana"] == ana


def test_publicar_anade_publicacion(red, tweet):
    resultado = red.publicar(tweet)

    assert resultado == tweet
    assert tweet in red.publicaciones


def test_timeline_solo_tiene_publicaciones_de_los_seguidos(red, ana, luis):
    ana.seguir(luis)

    tweet_luis_1 = Tweet(luis, "Primer tweet de Luis")
    tweet_luis_2 = Tweet(luis, "Segundo tweet de Luis")
    tweet_ana = Tweet(ana, "Tweet de Ana")

    red.anadir(ana)
    red.anadir(luis)

    red.publicar(tweet_luis_1)
    red.publicar(tweet_luis_2)
    red.publicar(tweet_ana)

    timeline = red.timeline(ana)

    assert timeline == [tweet_luis_2, tweet_luis_1]


def test_tendencias_cuenta_hashtags(red, ana, luis):
    tweet1 = Tweet(ana, "Hola #Python")
    tweet2 = Tweet(luis, "Aprendiendo #Python y #Programacion")

    red.publicar(tweet1)
    red.publicar(tweet2)

    tendencias = red.tendencias()

    assert tendencias == [
        ("#python", 2),
        ("#programacion", 1),
    ]


def test_mostrar_timeline(red, ana, tweet, capsys):
    luis = Usuario("Luis", "@luis")

    red.anadir(ana)
    red.anadir(luis)
    luis.seguir(ana)
    red.publicar(tweet)

    red.mostrar_timeline(luis)

    captured = capsys.readouterr()

    assert "Timeline de Luis (@luis):" in captured.out
    assert "@ana: Hola mundo  ♥ 0" in captured.out


def test_mostrar_timeline_acepta_alias(red, ana, tweet, capsys):
    luis = Usuario("Luis", "@luis")

    red.anadir(ana)
    red.anadir(luis)
    luis.seguir(ana)
    red.publicar(tweet)

    red.mostrar_timeline("@luis")

    captured = capsys.readouterr()

    assert "Timeline de Luis (@luis):" in captured.out
    assert "@ana: Hola mundo  ♥ 0" in captured.out


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


def test_len_red_social(red):
    red.registrar("Ana", "@ana")
    red.registrar("Luis", "@luis")

    assert len(red) == 2


def test_iter_usuarios_ordenados_por_alias(red):
    red.registrar("Luis", "@luis")
    red.registrar("Ana", "@ana")
    red.registrar("Marta", "@marta")

    usuarios = list(red)

    assert [usuario.alias for usuario in usuarios] == [
        "@ana",
        "@luis",
        "@marta",
    ]


def test_contains_comprueba_si_alias_existe(red):
    red.registrar("Ana", "@ana")

    assert "@ana" in red
    assert "@luis" not in red


def test_getitem_devuelve_usuario(red, ana):
    red.anadir(ana)

    assert red["@ana"] == ana


