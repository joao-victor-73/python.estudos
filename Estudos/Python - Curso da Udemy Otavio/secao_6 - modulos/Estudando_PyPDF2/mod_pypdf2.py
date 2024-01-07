# PyPDF2 - Para manipular arquivos PDF
# Aulas: 327, 328, 329, 330

'''< Dentro da biblioteca, existem três API Reference importantes 
     para se trabalhar. são elas: PDFReader / PDFWriter / PDFMerger >'''

from pathlib import Path  # Para os caminhos
from PyPDF2 import PdfReader, PdfWriter, PdfMerger

'''< Criando os caminhos das pastas >'''
PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'

RELATORIO_BACEN = PASTA_ORIGINAIS / 'R20230420.pdf'

PASTA_NOVA.mkdir(exist_ok=True)

'''< -- Usando o PdfReader -- >'''
reader = PdfReader(RELATORIO_BACEN)

print(len(reader.pages))  # Vai dizer quantas páginas tem no PDF

# Colocando uma pagina dentro de uma variável:
page1 = reader.pages[0]
page2 = reader.pages[1]

'''< -- Usando o PdfWriter -- >'''
writer = PdfWriter()
# Escrevendo um PDF Novo com apenas uma das paginas do PDF_Original:
writer.add_page(page1)

with open(PASTA_NOVA / 'page1.pdf', 'wb') as arquivo:
    # Abriu o arquivo e caso ele não existisse, ele foi criado.
    writer.write(arquivo)

# Criando um arquivo PDF para cada pagina do PDF_Original:
for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    with open(PASTA_NOVA / f'page{i}.pdf', 'wb') as arquivo:
        writer.add_page(page)
        writer.write(arquivo)

'''< -- Usando o PdfMerger -- >'''
merger = PdfMerger()

files = [
    PASTA_NOVA / 'page1.pdf', # Arquivo PDF contendo uma pagina
    PASTA_NOVA / 'page0.pdf', # Arquivo PDF contendo a outra pagina
]

for file in files:
    merger.append(file)

merger.write(PASTA_NOVA / 'Arquivo_MERGER.pdf')
merger.close()

