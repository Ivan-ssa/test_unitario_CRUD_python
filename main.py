import re
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from tabulate import tabulate  # Importar o módulo tabulate

# Dados pré-cadastrados
salas = {
    'A': 'Salão de Festas',
    'B': 'Churrasqueira 1',
    'C': 'Churrasqueira 2',
    'D': 'Churrasqueira 3',
    'E': 'Churrasqueira 4'
}

# Apartamentos válidos e blocos
apartamentos_validos = [
    101, 102, 103, 104, 
    201, 202, 203, 204, 
    301, 302, 303, 304, 
    401, 402, 403, 404, 
    501, 502, 503, 504
]
bloco_apartamentos = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# Reservas armazenadas
reservas = []

# Função para validar email
def validar_email(email):
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(padrao, email)

# Função para validar telefone
def validar_telefone(telefone):
    return re.match(r'^\d{11}$', telefone)

# Função para verificar data válida
def validar_data(data_str):
    try:
        data = datetime.strptime(data_str, '%d%m%Y')
        if data < datetime.now():
            print("Data retroativa! Tente novamente.")
            return None
        return data
    except ValueError:
        print("Data inválida! Use o formato DDMMYYYY.")
        return None

# Função para verificar se o apartamento já tem reserva no mês
def verificar_reserva_mes(apartamento, bloco, data):
    for reserva in reservas:
        if reserva['apartamento'] == apartamento and reserva['bloco'] == bloco:
            if reserva['data'].month == data.month and reserva['data'].year == data.year:
                print("Já existe uma reserva dentro deste mês/ano para este apartamento.")
                return True
    return False

# Função para enviar notificação por email
def enviar_notificacao_email(email, mensagem):
    try:
        msg = MIMEText(mensagem)
        msg['Subject'] = 'Confirmação de Reserva'
        msg['From'] = 'seuemail@dominio.com'
        msg['To'] = email

        with smtplib.SMTP('smtp.dominio.com', 587) as server:
            server.starttls()
            server.login('seuemail@dominio.com', 'sua_senha')
            server.sendmail('seuemail@dominio.com', email, msg.as_string())
        print("Notificação enviada para o email.")
    except Exception as e:
        print(f"Erro ao enviar email: {e}")

# Função para simular notificação por WhatsApp
def enviar_notificacao_whatsapp(telefone, mensagem):
    print(f"Simulação: Enviando WhatsApp para {telefone} com a mensagem: {mensagem}")

# Função para cadastrar reserva
def cadastrar_reserva():
    nome = input("Digite seu nome: ").strip()

    # Solicitar o número do apartamento até que seja válido ou o usuário digite 'sair'
    while True:
        apartamento = input("Digite o número do apartamento: ").strip()
        if apartamento.lower() == 'sair':
            return  # Encerra o cadastro se o usuário digitar 'sair'

        try:
            apartamento = int(apartamento)
            if apartamento not in apartamentos_validos:
                print("Número de apartamento inválido! Tente novamente.")
                continue  # Continua solicitando até que o número seja válido
            break  # Sai do loop se o apartamento for válido
        except ValueError:
            print("Formato inválido! O número do apartamento deve ser numérico.")
    
    # Solicitar a letra do bloco até que seja válida ou o usuário digite 'sair'
    while True:
        bloco = input("Digite a letra do bloco: ").upper().strip()
        if bloco.lower() == 'sair':
            return  # Encerra o cadastro se o usuário digitar 'sair'

        if bloco not in bloco_apartamentos:
            print("Bloco inválido! Tente novamente.")
        else:
            break  # Sai do loop se o bloco for válido

    email = input("Digite seu email: ").strip()
    if email.lower() == 'sair':
        return
    if not validar_email(email):
        print("Email inválido!")
        return

    while True:
        telefone = input("Digite seu telefone (somente números): ").strip()
        if telefone.lower() == 'sair':
            return
        if not validar_telefone(telefone):
            print("Telefone inválido! Insira 11 dígitos.")
            continue  # Solicita novamente se o telefone for inválido
        break  # Sai do loop se o telefone for válido

    print("Escolha uma sala:")
    for key, value in salas.items():
        print(f"{key}: {value}")

    sala_escolhida = input("Digite a letra da sala desejada: ").upper().strip()
    if sala_escolhida == 'SAIR':
        return
    if sala_escolhida not in salas:
        print("Sala inválida!")
        return

    data_str = input("Digite a data da reserva (DDMMYYYY): ").strip()
    if data_str.lower() == 'sair':
        return
    data_reserva = validar_data(data_str)
    if not data_reserva:
        return

    if verificar_reserva_mes(apartamento, bloco, data_reserva):
        return

    horario_inicio = input("Digite o horário de início (HHMM): ").strip()
    if horario_inicio.lower() == 'sair':
        return

    horario_fim = input("Digite o horário de término (HHMM): ").strip()
    if horario_fim.lower() == 'sair':
        return

    # Cadastrar a reserva
    reservas.append({
        'nome': nome,
        'apartamento': apartamento,
        'bloco': bloco,
        'email': email,
        'telefone': telefone,
        'sala': salas[sala_escolhida],
        'data': data_reserva,
        'horario_inicio': horario_inicio,
        'horario_fim': horario_fim
    })

    print(f"Reserva confirmada para {salas[sala_escolhida]} no dia {data_reserva.strftime('%d/%m/%Y')}")
    print("Sala deve ser entregue limpa, caso contrário, multa será aplicada.")
    enviar_notificacao_email(email, "Sua reserva foi confirmada com sucesso!")
    enviar_notificacao_whatsapp(telefone, "Sua reserva foi confirmada com sucesso!")

# Função para listar todas as reservas
def listar_reservas():
    if not reservas:
        print("Não há reservas no momento.")
        return

    # Criar lista de reservas formatadas
    reservas_formatadas = []
    for reserva in reservas:
        reservas_formatadas.append([
            reserva['sala'],
            reserva['data'].strftime('%d/%m/%Y'),
            reserva['horario_inicio'],
            reserva['horario_fim'],
            reserva['nome'],
            reserva['apartamento'],
            reserva['bloco']
        ])

    # Imprimir a tabela com a formatação desejada e colunas alinhadas
    print(tabulate(reservas_formatadas, headers=[
        'Sala', 'Data', 'Horário Entrada', 'Horário Saída', 'Nome', 'Apartamento', 'Bloco'
    ], tablefmt='grid', stralign='center'))

# Função para cancelar uma reserva
def cancelar_reserva():
    apartamento = input("Digite o número do apartamento: ").strip()
    if apartamento.lower() == 'sair':
        return

    try:
        apartamento = int(apartamento)
    except ValueError:
        print("Número de apartamento inválido!")
        return

    bloco = input("Digite a letra do bloco: ").upper().strip()
    if bloco == 'SAIR':
        return

    for reserva in reservas:
        if reserva['apartamento'] == apartamento and reserva['bloco'] == bloco:
            print(f"Reserva encontrada: {reserva['sala']} no dia {reserva['data'].strftime('%d/%m/%Y')}")
            confirmar = input("Deseja cancelar esta reserva? (S/N): ").upper().strip()
            if confirmar == 'S':
                reservas.remove(reserva)
                print("Reserva cancelada com sucesso!")
                return
    print("Nenhuma reserva encontrada.")

# Função para iniciar o sistema
def menu():
    while True:
        print("\n--- Menu de Reservas ---")
        print("1. Cadastrar Reserva")
        print("2. Listar Reservas")
        print("3. Cancelar Reserva")
        print("4. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            cadastrar_reserva()
        elif opcao == '2':
            listar_reservas()
        elif opcao == '3':
            cancelar_reserva()
        elif opcao == '4':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
