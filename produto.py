class Produto:

    #sobrescreve o construtor original
    def __init__(self, codigo, descricao, precoUnitario, quantEstoque):
        #__siginifica privado
        #quando deixamos os atributos privados, os dois se tornam encapsulados
        self.__codigo = codigo
        self.__descricao = descricao
        self.__precoUnitario = precoUnitario
        self.__quantEstoque = quantEstoque

    #propriedade é uma função que acessa o atributo privado (__)
    #somente leitura   property é um getter
    @property
    def codigo(self):
        return self.__codigo

    @property
    def descricao(self):
        return self.__descricao

    @property
    def precoUnitario(self):
        return self.__precoUnitario

    @property
    def quantEstoque(self):
        return self.__quantEstoque

    #setter é uma função que permite alterar o atributo da classe
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @precoUnitario.setter
    def precoUnitario(self, precoUnitario):
        self.__precoUnitario = precoUnitario

    @quantEstoque.setter
    def quantEstoque(self, quantEstoque):
        self.__quantEstoque = quantEstoque

    #sobrescreve a função builtin
    def __str__(self):
        return f'Código: {self.codigo} \tDescrição: {self.descricao} \Preço Unitário: R$ {self.precoUnitario:.2f} \tQuantidade em estoque: {self.quantEstoque}'

