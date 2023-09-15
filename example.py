from vacancy import consultar_vaga

RA_ESTUDANTE = ""
DIG_RA = ""
UF_RA = ""
DATA_DE_NASCIMENTO = "00/00/0000" 


def salvar(resultado: dict, nome_arquivo: str) -> None:
    """
    Salva um arquivo TXT em base nos resultados adquiridos
    """
    with open(f'{nome_arquivo}.txt', 'w') as file:
        for key, value in resultado.items():
            file.write(f"{key}: {value}\n")

def main():
    resultado = consultar_vaga(
        ra=RA_ESTUDANTE,
        digRa=DIG_RA,
        ufRa=UF_RA,
        dtNasc=DATA_DE_NASCIMENTO
    )

    salvar(resultado, "resultados")
    print("Consulta feita! Abra o arquivo \"resultados.txt\".")

if __name__ == "__main__":
    main()
