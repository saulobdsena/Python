
from identificador_estado import IdentificadorEstado
from estacionamento import calcular_valor

def main():
    print("=== Sistema de Estacionamento ===")
    placa = input("Digite a placa do veículo (ex: ABC1D23): ").strip().upper()
    entrada = input("Digite o horário de entrada (HH:MM): ").strip()
    saida = input("Digite o horário de saída (HH:MM): ").strip()

    identificador = IdentificadorEstado()
    estado = identificador.identificar(placa)
    valor = calcular_valor(entrada, saida)

    print("\n--- Resultado ---")
    print(f"Placa: {placa}")
    print(f"Estado de origem: {estado}")
    print(f"Valor a pagar: R$ {valor:.2f}")

if __name__ == "__main__":
    main()
