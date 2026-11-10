from datetime import datetime, date, timedelta
def calcular_manutencao(data_texto, intervalo):
    ultima_manutencao = datetime.strptime(
        data_texto, "%d/%m/%Y"
    ).date()
    proxima_manutencao = ultima_manutencao + timedelta(days=intervalo)
    hoje = date.today()
    dias_restantes = (proxima_manutencao - hoje).days
    if dias_restantes <0:
        status = ("Atrasada")
    elif dias_restantes <= 7:
        status = ("Próxima do vencimento")
    else:
        status = ("Em dia")
    return proxima_manutencao, dias_restantes, status
equipamento = input ("Nome do Equipamento :")
data_texto = input ("Data da ultima manutenção (DD/MM/AAAA): ")
intervalo = int(input("Intervalo de manutenção em dias: "))
proxima, dias, status, = calcular_manutencao(data_texto, intervalo)
print ("\n-------SMARTCARE--------")
print ("Equipamento: ", equipamento)
print ("Proxima manutenção:", proxima.strftime("%d/%m/%Y"))
print ("Dias restantes: ", dias)
print ("Status", status)