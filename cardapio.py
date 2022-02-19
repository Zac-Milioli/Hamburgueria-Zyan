class Cardapio:

#Declaramos o atributoque será a lista de produtos de cardápio
    def __init__(self):
        self.produtos = []

#Com essa função adicionamos um produto a nossa lista de produtos
    def add_produto(self, produto):
        self.produtos.append(produto)
        return self.produtos


#Essa função checará se o nome do produto que iremos pedir consta em nossa lista de produtos de cardápio.
#Nos retornará uma informação verdadeira ou falsa

    def get_name(self, name):
        for produto in self.produtos:
            if produto.nome == name:
                return produto
        return False


#Função em que retornamos em forma de print os items de cardápio.
    def print_produtos(self):
        print("CARDÁPIO")
        for produto in self.produtos:
            print("Nome:",produto.nome,",Preço: R$", produto.preco, ",Codigo:", produto.codigo)


