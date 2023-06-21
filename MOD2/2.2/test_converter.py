import pytest
from converter import RomanNumericConverter, Converter


@pytest.fixture
def converter():
    roman_converter = RomanNumericConverter()
    conv = Converter(roman_converter.roman_to_decimal, roman_converter.decimal_to_roman)
    return conv


def test_roman_to_decimal(converter):
    assert converter.convert('roman', 'I') == 1
    assert converter.convert('roman', 'IV') == 4
    assert converter.convert('roman', 'IX') == 9
    assert converter.convert('roman', 'LVIII') == 58
    assert converter.convert('roman', 'MMMCMXCIX') == 3999


def test_decimal_to_roman(converter):
    assert converter.convert('decimal', 1) == 'I'
    assert converter.convert('decimal', 4) == 'IV'
    assert converter.convert('decimal', 9) == 'IX'
    assert converter.convert('decimal', 58) == 'LVIII'
    assert converter.convert('decimal', 3999) == 'MMMCMXCIX'
