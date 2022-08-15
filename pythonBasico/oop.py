
#class pessoa:
#    def __init__(self,nome,sobrenome):
#        self.nome = nome
#        self.sobrenome = sobrenome

#a = pessoa('Arthur', 'Sobrinho')
   
#METODOS MAGICOS !! Pequisar.
    #Ex: __repr__(self)  retorna uma string quando o objeto é printado
    #    __add__(self, obj2)    __sub__(self, obj2)    __mult__(self, obj2)
    # __gt__(self, obj2) significa greater than, retorna valor booleano se o primeiro
    #sort() Organiza lista de forma crescente ou decrescente


#Herança
    #Subclasses recebem os atributos da superclasse
#class Cliente(pessoa):
#   def comprar(self):
#        print("Shut up and take my money")

#class Aluno(pessoa):
#    def estudar(self):
#        print("Estudando...")


#Polimorfismo
    #Subclasse e Superclasse possuirem métodos com o mesmo nome e o programa saber qual executar
    #self do método indica o correto (Olhar slide Nautilus)

#Exercício

class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome=nome
        self.idade=idade
        self.altura=altura

    def envelhecer(self):
        self.idade += 1
        print("Feliz Aniversário {}!!Você fez {} anos".format(self.nome, self.idade))
    
    def crescer(self):
        if self.idade < 21:
            self.altura = self.idade*0.05
        else: 
            self.altura = 21*0.05
        print(f"Você cresceu {round(self.altura,2)}m desde o seu nascimento.")
        


pessoa1 = Pessoa('Arthur', 21, 1.79)

pessoa1.envelhecer()
pessoa1.crescer()