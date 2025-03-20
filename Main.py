"""
Objetivo: Receber a temperatura da carne e informar o ponto da carne conforme a temperatura.
"""

def definir_ponto_carne(temperatura: float) -> str:
    """Retorna o ponto da carne com base na temperatura informada."""
    if temperatura >= 71:
        return "Bem passada"
    elif temperatura >= 65:
        return "Ao ponto para bem passada"
    elif temperatura >= 60:
        return "Ao ponto"
    elif temperatura >= 54:
        return "Ao ponto para mal passada"
    elif temperatura >= 48:
        return "Selada"
    else:
        return "Crua"

def main():
    """Função principal para entrada e saída de dados."""
    try:
        temperatura = float(input("Qual a temperatura da carne (°C)? ").strip())
        
        if temperatura < 0:
            print("A temperatura não pode ser negativa. Insira um valor válido.")
            return
        
        ponto = definir_ponto_carne(temperatura)
        print(f"A carne está: {ponto}")
    except ValueError:
        print("Por favor, insira um valor numérico válido.")

if __name__ == "__main__":
    main()
