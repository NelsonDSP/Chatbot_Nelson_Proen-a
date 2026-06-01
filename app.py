import os
from datetime import datetime

def obter_resposta(texto: str) -> str:
    comando: str = texto.lower()

#    if comando in ('olá', 'boa tarde', 'bom dia'):
#        return 'Olá tudo bem!'
#    if comando == 'como estás':
#        return 'Estou bem, obrigado!'
#    if comando == 'como te chamas?':
#        return 'O meu nome é: Bot :)'
#    if comando == 'tempo':
#        return 'Está um dia de sol!'
#    if comando in ('bye', 'adeus', 'tchau'):
#        return 'Gostei de falar contigo! Até breve...'
#    if 'horas' in comando:
#        return f'São: {datetime.now():%H:%M} horas'
#    if 'data' in comando:
#        return f'Hoje é dia: {datetime.now():%d-%m-%Y}'

#   return f'Desculpa, não entendi a questão! {texto}'

    respostas = {
        ('olá', 'boa tarde', 'bom dia'): 'Olá tudo bem!',
        'como estás': 'Estou bem, obrigado!',
        ('bye', 'adeus', 'tchau', 'xau', 'q'): 'Gostei de falar contigo! Até breve...',
        ('horas', 'que horas são'): f'São: {datetime.now():%H:%M} horas',
        ('data', 'dia'): f'Hoje é dia: {datetime.now():%d-%m-%Y}',
        ('como te chamas?', 'qual é o teu nome?'): 'O meu nome é: Bot :)'
        ('tempo', 'como está o tempo?'): 'Não tenho acesso à informação do tempo, mas espero que esteja um ótimo dia!'
        ('Quem és tu?', 'sobre ti'): 'Sou um chatbot criado para responder às tuas perguntas e ajudar-te com o que precisares!'
    }

    for chave, resposta in respostas.items():
        if isinstance(chave, tuple):
            if comando in chave:
                return resposta
        elif chave in comando:
            return resposta

    return f'Desculpa, não entendi a questão! {texto}'


def chat() -> None:
    print('Bem-vindo ao ChatBot!')
    print('\nEscreva "bye" para sair do chat')
    name: str = input('\nBot: Como te chamas? ')
    print(f'Bot: Olá, {name}!\n \n Como te posso ajudar?')

    while True:
        user_input: str = input('Tu: ')
        resposta: str = obter_resposta(user_input)
        print(f'Bot: {resposta}')

        if user_input.lower() in ('bye', 'adeus', 'tchau'):
            break

    print('Chat acabou')
    print()


def main() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    chat()


if __name__ == '__main__':
    main()