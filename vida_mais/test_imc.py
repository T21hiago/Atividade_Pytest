from imc import *
import pytest

def test_imc():
    assert calcular_imc(70,1.75) == 22.86

def test_calculo_imc_arredonda():
    assert calcular_imc(68, 1.75) == round(68 / (1.75**2), 2)

def test_casas():
   assert calcular_imc(80, 1.80) == round(80 / (1.80 ** 2), 2)
   with pytest.raises(ValueError):    
        calcular_imc(70,0)
    #assert calcular_imc(70,0) == "A altura deve ser maior que zero!!"

def test_imc_baixo_peso():
    assert classificar_imc(17.9) == "Abaixo do peso"

def test_imc_peso_normal():
    assert classificar_imc(22.9) == "Peso normal"

def test_imc_sobrepeso():
    assert classificar_imc(27.3) == "Sobrepeso"

def test_imc_obesidade1():
    assert classificar_imc(33.1) == "Obesidade grau I"

def test_imc_obesidade2():
    assert classificar_imc(37.0) == "Obesidade grau II"

def test_imc_obesidade3():
    assert classificar_imc(45.0) == "Obesidade grau III"




