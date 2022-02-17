#MANUAL DO USUÁRIO
Olá, este é um manual básico direcionado ao usuário deste sistema básico.

Todas as ações devem ser feitas diretamente dentro da área delimitada e nomeada como "ÁREA DO USUÁRIO",
para conservar a integridade dos objetos e funções, pois esses estão perfeitamente funcionais.
O programa também pode ser executado via console.


FORMAS DE USO:

° Para adicionar um produto ao cardápio:

    Na ÁREA DO USUÁRIO, crie um objeto utilizando o seguinte formato

        objeto_produto = p('nome', 'descrição', valor)

    Notando sempre que o valor deve ser um inteiro, nada de strings!
    Caso a descrição seja grande demais, crie uma variável e atribua a descrição à ela, então no instanciamento do
    objeto basta colocá-la como parâmetro.

    Após instanciar o objeto, ele deve ser adicionado à lista de produtos para funcionar corretamente. Para isso, utilize
    a função

        c.add_produto(objeto_produto)


° Para exibir o cardápio:

    Dentro da ÁREA DO USUÁRIO, após criar e adicionar seus próprios produtos ao cardápio, digite o seguinte comando:

        exibir_cardapio()


° Para adicionar um cliente:

    Deve ser instanciado um objeto Cliente, então utilize o seguinte formato:

        objeto_cliente = Cliente('nome', código_numérico, 'número_da_mesa')


° Para adicionar pedidos ao cliente:

    Utilize o seguinte comando:

        objeto_cliente.add_pedido(objeto_produto)


° Para exibir a comanda atual do cliente:

    get_comanda(objeto_cliente)


**Os outros comandos (getters e setters) são reservados aos desenvolvedores, mas seu acesso é fácil, bastando usar
o nome do atributo que busca alterar (colocando a alteração) ou exibir (utilizando print() junto à função).
