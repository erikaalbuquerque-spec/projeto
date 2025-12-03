class Livro:
    def __init__(self, titulo_livro, autor, isbn, disponibilidade):
        self.titulo_livro = titulo_livro
        self.autor = autor
        self.isbn = isbn
        self.disponibilidade = disponibilidade

class Usuario:
    def __init__(self, nome, cod_identificacao):
        self.nome = nome
        self.cod_identificacao = cod_identificacao

class Cliente(Usuario):
    def __init__(self, nome, cod_identificacao, lista_de_livros_emprestados=None, limite_emprestimo=3):
        super().__init__(nome, cod_identificacao)
        if lista_de_livros_emprestados is None:
            lista_de_livros_emprestados = []
        self.lista_de_livros_emprestados = lista_de_livros_emprestados
        self.limite_emprestimo = limite_emprestimo

    def emprestar_livro(self, livro):
        if (self.lista_de_livros_emprestados) > self.limite_emprestimo:
            if livro.disponibilidade:
                self.lista_de_livros_emprestados.append(livro)
                livro.disponibilidade = False
                print(f"O livro '{livro.titulo_livro}' foi emprestado para {self.nome}.")
            else:
                print(f"O livro '{livro.titulo_livro}' não está disponível para empréstimo.")
        else:
            print(f"{self.nome} atingiu o limite de empréstimos ({self.limite_emprestimo} livros).")

    def devolver_livro(self, livro):
        if livro in self.lista_de_livros_emprestados:
            self.lista_de_livros_emprestados.remove(livro)
            livro.disponibilidade = True
            print(f"O livro '{livro.titulo_livro}' foi devolvido por {self.nome}.")
        else:
            print(f"{self.nome} não tem o livro '{livro.titulo_livro}' para devolver.")

class Funcionario(Usuario):
    def __init__(self, nome, cod_identificacao, cargo):
        super().__init__(nome, cod_identificacao)
        self.cargo = cargo

    def registrar_livro(self, biblioteca, livro):
        biblioteca.acervo.append(livro)
        print(f"Funcionário {self.nome} registrou o livro '{livro.titulo_livro}'.")

    def remover_livro(self, biblioteca):
        for livro in biblioteca.acervo:
            biblioteca.acervo.remove(livro)
        print(f"Funcionário {self.nome} removeu o livro {livro.titulo_livro}.")
        return
    print("Livro não encontrado no acervo.")


class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.acervo = []
        self.membros = []

    def adicionar_membro(self, usuario):
        self.membros.append(usuario)
        print(f"Membro {usuario.nome} adicionado à biblioteca.")

    def verificar_disponibilidade(self, isbn):
        for livro in self.acervo:
            if livro.isbn == isbn:
                return livro.disponivel
        return

biblioteca = Biblioteca("Biblioteca Central")


cliente = Cliente("July", "12345")
funcionario = Funcionario("liliana", "fwrayva", "Bibliotecária")

biblioteca.adicionar_membro(cliente)
biblioteca.adicionar_membro(funcionario)

livro1 = Livro("verity", "Collen Hpover", "12356")
livro2 = Livro("O Cortiço", "Aluísio Azevedo", "456")

funcionario.registrar_livro(biblioteca, livro1)
funcionario.registrar_livro(biblioteca, livro2)

cliente.emprestar_livro(livro1)
cliente.devolver_livro(livro1)

biblioteca.buscar_livro("verity")
biblioteca.buscar_livro("")