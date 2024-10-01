#importação de valores, já com valores adaptados para python
sp = float(67836.43)
mg = float(29229.88)
rj = float(36678.66)
es = float(27165.48)
outros = float(19849.53)

#Soma total de regiões
soma_total_regioes = sp + mg + rj + es + outros

#calculo de percentual de cada região com base na soma total
percentual_Sp = (sp / soma_total_regioes * 100)
percentual_mg = (mg / soma_total_regioes * 100)
percentual_rj = (rj / soma_total_regioes * 100)
percentual_es = (es / soma_total_regioes * 100)
percentual_outros = (outros / soma_total_regioes * 100)

#print de resultados
print(f"Resultados de percentual:\n")
print(f"O percentual de SP: {percentual_Sp:.2f}%\n")
print(f"O percentual de MG: {percentual_mg:.2f}%\n")
print(f"O percentual de RJ: {percentual_rj:.2f}%\n")
print(f"O percentual de ES: {percentual_es:.2f}%\n")
print(f"O percentual de Outros: {percentual_outros:.2f}%\n")


