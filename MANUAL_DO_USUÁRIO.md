# MANUAL DO USUÁRIO

Olá, este é um manual básico direcionado ao usuário deste sistema.

Todas as ações devem ser feitas diretamente dentro da área delimitada e nomeada como "ÁREA DO USUÁRIO",
para conservar a integridade dos objetos e funções, pois esses estão perfeitamente funcionais.
O programa também pode ser executado via console.


# Formas de uso:

* Para ADICIONAR UM PRODUTO ao cardápio:

    Na Área do Usuário, crie um objeto utilizando o seguinte formato

        objeto_produto = p('nome', 'descrição', valor)

    Notando sempre que o valor deve ser um inteiro, nada de strings!
    Caso a descrição seja grande demais, crie uma variável e atribua a descrição à ela, então no instanciamento do
    objeto basta colocá-la como parâmetro.

    Após instanciar o objeto, ele deve ser adicionado à lista de produtos para funcionar corretamente. Para isso, utilize
    a função

        c.add_produto(objeto_produto)


* Para EXIBIR CARDÁPIO:

    Dentro da ÁREA DO USUÁRIO, após criar e adicionar seus próprios produtos ao cardápio, digite o seguinte comando:

        exibir_cardapio()


* Para ADICIONAR UM CLIENTE:

    Deve ser instanciado um objeto Cliente, então utilize o seguinte formato:

        objeto_cliente = Cliente('nome', código_numérico, 'número_da_mesa')


* Para ADICIONAR PEDIDOS AO CLIENTE:

    Utilize o seguinte comando:

        objeto_cliente.add_pedido(objeto_produto)

* Para DELETAR PEDIDOS de um cliente:
    Utilize o seguinte comando:
        
        objeto_cliente.delete_pedido(objeto_produto)

* Para EXIBIR A COMANDA atual do cliente:

      get_comanda(objeto_cliente)


> Os outros comandos (getters e setters) são reservados aos desenvolvedores, mas seu acesso é fácil, bastando usar
o nome do atributo que busca alterar (colocando a alteração) ou exibir (utilizando print() junto à função).
