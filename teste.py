import requests
from bs4 import BeautifulSoup

# URL do site alvo
url = 'https://www.clubefii.com.br/fiis/hglg11'

# Cabeçalhos para simular um navegador
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Fazendo a requisição HTTP para obter o conteúdo da página
response = requests.get(url, headers=headers)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    # Parsing do conteúdo HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # Buscando a seção que contém as informações desejadas
    info_section = soup.find('div', class_='informacoes-gerais')

    if info_section:
        # Extraindo a taxa de administração
        taxa_adm = info_section.find('span', text='Taxa de Administração').find_next_sibling('span').text.strip()

        # Extraindo a vacância física
        vacancia_fisica = info_section.find('span', text='Vacância Física').find_next_sibling('span').text.strip()

        # Exibindo os resultados
        print(f'Taxa de Administração: {taxa_adm}')
        print(f'Vacância Física: {vacancia_fisica}')
    else:
        print('Seção de informações gerais não encontrada.')
else:
    print(f'Erro ao acessar a página: {response.status_code}')
