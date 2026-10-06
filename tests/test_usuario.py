from red_social.usuario import Usuario


def test_alias_empieza_por_arroba():
    ana = Usuario("Ana", "ana")

    assert ana.alias == "@ana"


def test_seguir_anade_usuario():
    ana = Usuario("Ana", "@ana")
    luis = Usuario("Luis", "@luis")

    ana.seguir(luis)

    assert luis in ana.seguidos