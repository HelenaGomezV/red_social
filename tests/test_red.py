from red_social.red import RedSocial


def test_red_social_empieza_vacia():
    red = RedSocial()

    assert red.usuarios == {}
    assert red.publicaciones == []