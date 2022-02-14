
class Cardapio:
    def __init__(self):
        self.produtos = []
        self.nomes = []


    def new_produto(self, produto):
        self.produtos.append(produto)


    def get_produto(self):
        print(20*"_")
        print("CARDÁPIO")
        for produto in self.produtos:
            print("Nome:",produto.nome,",Preço:", produto.preco, ",Codigo:", produto.codigo)
        print(20*"_")


