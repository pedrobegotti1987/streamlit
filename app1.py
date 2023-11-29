import pandas as pd
from datetime import datetime, timedelta

def calcular_cronograma_simplificado(valor_emprestimo, taxa_anual, num_meses):
    # Converter taxa anual para mensal
    taxa_mensal = (1 + taxa_anual)**(1/12) - 1

    # Calcular prestação mensal usando Tabela Price
    pmt = valor_emprestimo * (taxa_mensal / (1 - (1 + taxa_mensal)**(-num_meses)))

    # Criar cronograma de pagamento
    cronograma = []
    saldo_devedor = valor_emprestimo
    data_pagamento = datetime.today()
    for mes in range(1, num_meses + 1):
        juros_mes = saldo_devedor * taxa_mensal
        amortizacao = pmt - juros_mes
        saldo_devedor -= amortizacao
        cronograma.append([data_pagamento.strftime("%Y-%m-%d"), round(pmt, 2), round(juros_mes, 2), round(amortizacao, 2), round(saldo_devedor, 2)])
        data_pagamento += timedelta(days=30)  # Aproximando para cada mês ter 30 dias

    return pd.DataFrame(cronograma, columns=["Data", "Parcela", "Juros", "Amortização", "Saldo Devedor"])

# Exemplo de uso da função simplificada
valor_emprestimo = 300000  # R$ 300.000,00
taxa_anual = 0.14  # 14%
num_meses = 36  # 36 meses

cronograma_pagamento = calcular_cronograma_simplificado(valor_emprestimo, taxa_anual, num_meses)
cronograma_pagamento.head()
