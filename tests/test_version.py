from snakypy.dotctrl import __info__


def test_version():
    assert __info__["version"] == "2.0.0rc2"
