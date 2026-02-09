'''
Olhe primeiro o arquivo __init__.py depois olhe o arquivo routes.py (onde ficam as funções)
'''
from ProjetoSiteFlask import app

if __name__ == '__main__':  # o código só roda se estiver utilizando esse arquivo.
    app.run(debug=True) # o Debug permite atualizar o site de forma automática, sem precisar pausar e sair do código.


 