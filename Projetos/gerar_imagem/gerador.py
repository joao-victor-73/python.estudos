import openai
import requests

openai.api_key = 'MINHA_CHAVE_API'


def gerar_imagem(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n = 1,
        size='1024x1024',
    )

    # Verificando se houve uma resposta válida
    if 'data' in response and len(response['data']) > 0:
        image_url = response['data'][0]['url']
        image_data = requests.get(image_url).content

        with open("generated_image.png", "wb") as f:
            f.write(image_data)

        print("imagem gerada com suscesso!")

    else:
        print('Não foi possível gerar a imagem')

pergunta = input('Digite o que você quer gerar: ')
gerar_imagem(pergunta)
