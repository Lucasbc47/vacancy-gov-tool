import requests

from typing import Dict
from bs4 import BeautifulSoup

def get_last_item(html: str) -> str:
    """
    Busca ultimo item do HTML. A ultima escola no caso 
    """
    soup = BeautifulSoup(html, 'html.parser')
    ultimo_item = soup.find('table').find_all('tr')[-1].get_text()
    return ultimo_item

def consultar_vaga(ra: str, digRa: int, ufRa: str, dtNasc: str) -> Dict[str, str]:
    """
    Faz um POST ao SED pra consultar vaga
    """
    url: str = "https://sed.educacao.sp.gov.br/ConsultaPublica/Pesquisar"

    payload: dict = {
        "ra": ra,
        "digRa": digRa,
        "ufRa": ufRa,
        "dtNasc": dtNasc
    }
    response: requests.Response = requests.post(url=url, data=payload)
    res = get_last_item(response.text)
    lista_filtrada = list(filter(lambda x: x.strip(), res.splitlines()))
    itens = ["Nome", "Data de Nascimento", "Ano", "Nível", "Série", "RA", "Escola", "Endereço", "Telefone" ]
    resultados = dict(zip(itens, lista_filtrada))
    return resultados
