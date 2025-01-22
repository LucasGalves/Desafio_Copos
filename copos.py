# copo_1 = [400, 400]
# copo_2 = [0, 250]
# copo_3 = [0, 150]
#
# dict_copos = {1: [400, 400],
#               2: [0, 250],
#               3: [0, 150]}

# =========== Definindo os copos: =========== #
class Copo:
    def __init__(self, capacidade, conteudo=0):
        self.conteudo = conteudo
        self.capacidade = capacidade

    def get_conteudo(self):
        return self.conteudo
    
    def set_conteudo(self, novo_conteudo):
        self.conteudo = novo_conteudo

    def get_espaco_sobra(self):
        return self.capacidade - self.conteudo

    def get_capacidade(self):
        return self.capacidade

copo_1 = Copo(400, conteudo=400)
copo_2 = Copo(250)
copo_3 = Copo(150)


# =========== Funções: =========== #
def printar_conteudo():
    conteudo_1 = int(copo_1.get_conteudo())
    conteudo_2 = int(copo_2.get_conteudo())
    conteudo_3 = int(copo_3.get_conteudo())

    print("==== Estado dos copos ====")
    print(f"Copo 1: {conteudo_1}/400 ml")
    print(f"Copo 2: {conteudo_2}/250 ml")
    print(f"Copo 3: {conteudo_3}/150 ml")


def passar_conteudo(copo1: Copo, copo2: Copo):

    # Se: Não tiver nada no copo 1  |  Ser passado o mesmo copo  |  Não tiver espaço no copo 2
    if (copo1.get_conteudo() == 0) or (copo1 == copo2) or (copo2.get_espaco_sobra == 0):
        print("nada foi feito")
        return
    
    # Se for encher o copo 2 e sobrar um tanto no copo 1:
    if copo1.get_conteudo() > copo2.get_espaco_sobra():
        copo1.set_conteudo(copo1.get_conteudo() - copo2.get_espaco_sobra()) # Sobra
        copo2.set_conteudo(copo2.get_capacidade()) # Enche o copo
        # print(f"{copo1.get_conteudo()} - {copo2.get_espaco_sobra()}")

    # Se for todo o conteúdo do copo 2 para o copo 1:
    elif copo1.get_conteudo() <= copo2.get_espaco_sobra():
        copo2.set_conteudo(copo2.get_conteudo() + copo1.get_conteudo())
        copo1.set_conteudo(0)

    else:
        print("nada foi feito")
    

def condicao_vitoria(copo1: Copo, copo2: Copo) -> bool:
    flag1 = False
    flag2 = False

    if copo1.get_conteudo() == 200:
        flag1 = True

    if copo2.get_conteudo() == 200:
        flag2 = True

    return (flag1 and flag2)


# =========== O Jogo: =========== #
print("\n* Começano o jogo. Tente deixar tanto o copo 1 quanto o copo 2 com 200 ml.\n* Para sair digite 69\n")
while True:
    printar_conteudo()

    if condicao_vitoria(copo_1, copo_2):
        print("\n    ##### Parabens galvinho, você foi um imbecil esse tempo todo #####")
        break

    while True:
        try:
            escolha = int(input("Qual copo deseja retirar? [1/2/3]: "))
            if escolha == 69:
                break
            elif escolha == 1:
                c1 = copo_1
            elif escolha == 2:
                c1 = copo_2
            elif escolha == 3:
                c1 = copo_3


            escolha = int(input("Qual copo deseja colocar? [1/2/3]: "))
            if escolha == 69:
                break
            elif escolha == 1:
                c2 = copo_1
            elif escolha == 2:
                c2 = copo_2
            elif escolha == 3:
                c2 = copo_3
            
            break

        except:
            print("Desculpa, não entendi..")

    if escolha == 69:
        exit()

    passar_conteudo(c1, c2)
    print("\n")

