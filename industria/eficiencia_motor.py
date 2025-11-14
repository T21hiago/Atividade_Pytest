def calcular_eficiencia(potencia_saida, potencia_entrada):
    #Calcula a eficiência percentual de um motor elétrico.
    if potencia_entrada <=0:
      raise ValueError("potencia de entrada deve ser maior que zero. " )
    else:
        eficiencia = (potencia_saida / potencia_entrada) * 100
        return round(eficiencia, 2)
def classificar_eficiencia(eficiencia):
    '''
    Classifica a eficiência conforme padrões simplificados (didáticos):
    - Abaixo de 80% → IE1 (Baixa eficiência)
    - Entre 80 e 89.9% → IE2 (Eficiência média)
    - 90% ou mais → IE3 (Alta eficiência)
    '''
    if eficiencia <80:
        return "1E1- Baixa eficiência"
    elif eficiencia < 90:
        return "IE2 - Eficiência média"
    else:
        return "IE3 - Alta eficiência"
    
def analise_motor( potencia_saida, potencia_entrada):
    """Funçào principal: retorna dicionário com os resultados. """
    eficiencia = calcular_eficiencia(potencia_saida, potencia_entrada)
    classificacao = classificar_eficiencia(eficiencia)
    return {
    "potencia_saida": potencia_saida,
    "potencia_entrada": potencia_entrada,
    "eficiencia": eficiencia,
    "classificacao": classificacao,
    }
print(analise_motor(880,1000))