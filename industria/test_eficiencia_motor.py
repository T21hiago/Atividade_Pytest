from eficiencia_motor import *
import pytest
def test_calcular_eficiencia():
    assert calcular_eficiencia(900,1000) == 90
    assert calcular_eficiencia(855,1000) == 85.5
    with pytest.raises(ValueError):    
        calcular_eficiencia(1000,0)
def test_classificar_eficiencia():
    assert classificar_eficiencia(75.0) == "1E1- Baixa eficiência"
    assert classificar_eficiencia(85.0) == "IE2 - Eficiência média"
    assert classificar_eficiencia(92.0) == "IE3 - Alta eficiência"
def test_integracao():
    eficiencia = analise_motor(880,1000)
    assert eficiencia["eficiencia"] == 88
    assert eficiencia["classificacao"] == "IE2 - Eficiência média"