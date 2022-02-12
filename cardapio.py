
class Cardapio:
    def __init__(self):
        self.produtos = []


    def new_produto(self, produto):
        self.produtos.append(produto)
        print("Item foi adicionado com sucesso")

    def get_pro(self):
        for produto in self.produtos:
            print("Nome:",produto.nome,",Preço:", produto.preco, ",Descrição:",produto.codigo)