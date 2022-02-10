
class Cardapio:
    def __init__(self):
        self.produtos = []

    def set_cardapio(self, cardapio):
        self.produtos.append((cardapio))


    def new_produto(self, produto):
        self.produtos.append(produto)
        print("Item adicionado com sucesso")

    def get_pro(self):
        for produto in self.produtos:
            print("Nome:",produto.nome,",Preço:", produto.preco, ",Descrição:",produto.descricao)



