reservas = []
def criar_reserva():
    nome = input("Digite o nome da reserva: ")
    data = input("Digite a data da reserva (DDMMYYYY): ")
    
    if validar_data(data):  # Valida a data
        reserva = {
            "nome": nome,
            "data": data
        }
        reservas.append(reserva)  # Adiciona a reserva à lista
        print("Reserva criada com sucesso!")
    else:
        print("Data inválida! Tente novamente.")

def listar_reservas():
    if not reservas:
        print("Nenhuma reserva encontrada.")
    else:
        for i, reserva in enumerate(reservas):
            print(f"{i + 1}. Nome: {reserva['nome']}, Data: {reserva['data']}")


def atualizar_reserva():
    listar_reservas()  # Lista as reservas
    indice = int(input("Escolha o número da reserva que deseja atualizar: ")) - 1
    
    if 0 <= indice < len(reservas):
        nome = input("Digite o novo nome da reserva: ")
        data = input("Digite a nova data da reserva (DDMMYYYY): ")
        
        if validar_data(data):
            reservas[indice]['nome'] = nome
            reservas[indice]['data'] = data
            print("Reserva atualizada com sucesso!")
        else:
            print("Data inválida! Tente novamente.")
    else:
        print("Índice inválido!")

def cancelar_reserva():
    listar_reservas()  # Lista as reservas
    indice = int(input("Escolha o número da reserva que deseja cancelar: ")) - 1
    
    if 0 <= indice < len(reservas):
        reservas.pop(indice)  # Remove a reserva da lista
        print("Reserva cancelada com sucesso!")
    else:
        print("Índice inválido!")
def validar_data(data):
    from datetime import datetime

    try:
        datetime.strptime(data, "%d%m%Y")  # Formato esperado: DDMMYYYY
        return True
    except ValueError:
        return False
