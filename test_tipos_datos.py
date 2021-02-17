from utils_test import eval_test
import pytest

import tipos_de_datos

d = {
    'var2': 15,
    'apellido': ' alvarez',
    'len_apellido': 8,
    'apellido2': 'alvarez',
    'apellido_es_mayuscula': False,
    'apellido3': 'ALVAREZ',
    'a_in_apellido': 2,
    'apellido_end_ez': True,
    'apellidos_tuple': ('PRIETO  ', ' GUERRERO', 'cortes  ', 'santos ', 'medina  ', ' nuñez ', '   MARIN', 'ortiz ', '    DELGADO ', '  MORALES', 'SUAREZ  ', 'serrano    ', ' gil  ', 'VAZQUEZ'),
    'apellidos_list2': [' pascual', 'AGUILAR  ', '  reyes  ', 'NIETO  ', ' caballero  ', 'CARRASCO ', ' FUENTES ', 'diez', 'vega  ', ' CAMPOS  ', '  FLORES', '  CABRERA ', ' PEÑA  ', '   marquez', '  herrera  ', ' ferrer  ', 'VAZQUEZ', ' gil  ', 'serrano    ', 'SUAREZ  ', '    DELGADO ', 'ortiz ', '   MARIN', ' nuñez ', 'medina  ', 'cortes  ', ' GUERRERO', 'PRIETO  '],
    'apellidos_set1': {' caballero  ', 'diez', 'vega  ', 'AGUILAR  ', ' pascual', ' FUENTES ', '  FLORES', ' PEÑA  ', '   marquez', '  herrera  ', '  reyes  ', '  CABRERA ', 'CARRASCO ', 'NIETO  '},
    'apellidos_set2': {' caballero  ', 'diez', 'vega  ', 'AGUILAR  ', ' pascual', 'HIDALGO', ' FUENTES ', 'montero ', ' herrero  ', ' LORENZO', '  reyes  ', 'CARRASCO ', '  ibañez ', 'santana', 'NIETO  '},
    'apellidos_set3': {' caballero  ', 'diez', 'vega  ', 'CARRASCO ', ' FUENTES ', 'NIETO  ', '  reyes  ', 'AGUILAR  ', ' pascual'},
    'apellidos_set4': {' caballero  ', 'diez', ' pascual', 'HIDALGO', ' FUENTES ', '  FLORES', ' PEÑA  ', 'montero ', '   marquez', '  herrera  ', '  reyes  ', '  CABRERA ', ' LORENZO', '  ibañez ', 'NIETO  ', 'vega  ', ' herrero  ', 'CARRASCO ', 'santana', 'AGUILAR  '},
    'apellidos_set5': {'HIDALGO', '  FLORES', ' PEÑA  ', 'montero ', '   marquez', '  herrera  ', ' LORENZO', '  CABRERA ', '  ibañez ', ' herrero  ', 'santana'},
    'var3': True,
    'apellidos_dict': {'  GARCIA': None, '        rodriguez  ': None, 'FERNANDEZ ': None, 'LOPEZ': None, 'key1': 12},
    'apellido_gonzalez': 34,
    'apellido_none': None
}

@pytest.mark.parametrize("var", list(d.keys()))
def test_eval(var):
    eval_test(d, var, tipos_de_datos)