from morse import decode
import pytest


@pytest.mark.parametrize(
    "source_morse,result", [
        ('... --- ...', 'SOS'),
        ('.', 2),
        ('SOS', 'S'),
    ], )
def test_decode(source_morse, result):
    assert decode(source_morse) == result


if __name__ == '__main__':
    print('hi')
