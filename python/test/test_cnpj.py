from app.valida_cnpj import validate_cnpj

def test_cnpj_valido():
    assert validate_cnpj("78.245.685/0001-23") == "78245685000123"

def test_cnpj_invalido():
    assert validate_cnpj("78.245.685/0001-00") == False

def test_exemplo_que_funciona():
    exemplo('11222333000181', '11222333000181')

def test_exemplo_que_nao_funciona():
    exemplo('11222333000100', False)

def test_exemplo_que_nao_funciona_com_texto():
    exemplo('abcdefghijklmn', False)

def exemplo(entrada, saida):
    assert validate_cnpj(entrada) == saida