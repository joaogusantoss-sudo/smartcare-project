import csv
from datetime import datetime, date, timedelta
from pathlib import Path
ARQUIVO_CSV = Path(__file__).resolve().parent.parent / "n8n" / "equipamentos.csv"
def cadastrar_equipamento():
    print("\n======= CADASTRO SMARTCARE =======")
    equipamento = input("Nome do equipamento: ").strip()
    data_texto = input(
        "Data da última manutenção (DD/MM/AAAA): "
    ).strip()
    intervalo = int(
        input("Intervalo entre manutenções em dias: ")
    )
    datetime.strptime(data_texto, "%d/%m/%Y")
    if not equipamento or intervalo <= 0:
        raise ValueError("Informe um nome e um intervalo válido.")
    arquivo_existe = ARQUIVO_CSV.exists()
if arquivo_existe and ARQUIVO_CSV.stat().st_size > 0:
    with open(ARQUIVO_CSV, "rb") as arquivo:
        arquivo.seek(-1, 2)
        ultimo_byte = arquivo.read(1)
    if ultimo_byte not in (b"\n", b"\r"):
        with open(ARQUIVO_CSV, "a", encoding="utf-8") as arquivo:
            arquivo.write("\n")
    with open(ARQUIVO_CSV, "a", newline="", encoding="utf-8") as arquivo:
        campos = [
            "equipamento",
            "data_ultima_manutencao",
            "intervalo_dias"
        ]
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        if not arquivo_existe or ARQUIVO_CSV.stat().st_size == 0:
            escritor.writeheader()
        escritor.writerow({
            "equipamento": equipamento,
            "data_ultima_manutencao": data_texto,
            "intervalo_dias": intervalo
        })
    print("\nEquipamento cadastrado com sucesso!")
def calcular_manutencao(data_texto, intervalo):
    ultima_manutencao = datetime.strptime(
        data_texto, "%d/%m/%Y"
    ).date()
    proxima_manutencao = (
        ultima_manutencao + timedelta(days=intervalo)
    )
    hoje = date.today()
    dias_restantes = (proxima_manutencao - hoje).days
    if dias_restantes < 0:
        status = "Atrasada"
    elif dias_restantes <= 7:
        status = "Próxima do vencimento"
    else:
        status = "Em dia"
    return proxima_manutencao, dias_restantes, status
def main():
    while True:
        print("\n========== SMARTCARE ==========")
        print("1 - Cadastrar equipamento")
        print("2 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            try:
                cadastrar_equipamento()
            except ValueError:
                print("Erro: verifique a data e os valores informados.")
        elif opcao == "2":
            print("Encerrando o SmartCare...")
            break
        else:
            print("Opção inválida. Tente novamente.")
if __name__ == "__main__":
    main()