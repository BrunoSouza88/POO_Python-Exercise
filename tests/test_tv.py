from src.tv import TV


def test_ligar_desligar():
    tv = TV(42)
    assert tv._TV__ligada is False
    tv.ligar_desligar()
    assert tv._TV__ligada is True
    tv.ligar_desligar()
    assert tv._TV__ligada is False


def test_modificar_canal():
    tv = TV(42)
    assert tv.get_canal() == 1
    tv.modificar_canal(42)
    assert tv.get_canal() == 42
    tv.modificar_canal(50)
    assert tv.get_canal() == 50


def test_modificar_volume():
    tv = TV(42)
    assert tv.get_volume() == 50

    tv.aumentar_volume()
    assert tv.get_volume() == 51

    tv.diminuir_volume()
    assert tv.get_volume() == 50
