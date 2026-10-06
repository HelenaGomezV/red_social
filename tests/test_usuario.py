from red_social.usuario import Usuario


def test_alias_empieza_por_arroba():
    ana = Usuario("Ana", "ana")

    assert ana.alias == "@ana"