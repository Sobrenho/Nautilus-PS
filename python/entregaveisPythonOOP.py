class AUV:
    robos = []

    def __init__(self, nome, sensores, num_thursters, ano_construção, testing_sim, testing_water):
        AUV.robos.append(self)
        self.nome = nome
        self.sensores = sensores
        self.num_thursters = num_thursters
        self.ano_construção = ano_construção
        self.testing_sim = testing_sim
        self.testing_water = testing_water

    @classmethod
    def exibirTodosAUVs(cls):
        print("\n\tAno de Contrução | Nº de thrusters | Tempo de teste em simulação | Tempo de teste em água | Sensores " )
        for robo in cls.robos:
            print(f"{robo.nome+':':12}{robo.ano_construção:<8}{robo.num_thursters:15}{robo.testing_sim:20} hrs {robo.testing_water:26} hrs" + (" "*10) + ', '.join(robo.sensores))
        print("")


    def exibirAUV(self):     
        print(f"\n\t\t {self.nome}\n"
              f"Ano de Construção: {self.ano_construção}\n"
              f"Número de thursters: {self.num_thursters}\n"
              f"Tempo de teste no simulador: {self.testing_sim} hrs\n"
              f"Tempo de teste em água: {self.testing_water} hrs\n"
              f"Sensores: {self.sensores}\n")

    @classmethod
    def ranking(cls):
        def getAno(robo):
            return robo.ano_construção

        cls.robos.sort(reverse=True, key=getAno)
        print("RANKING:")
        for index, robo in enumerate(cls.robos):
            print(f"{index+1}: {robo.nome}")


    def alteraçãoTempoTeste(self):
        if int(input("Deseja alterar: \n [0] - Tempo em simulação\n [1] - Tempo em água\n")):
            tempo = int(input("Escreva a quantidade de horas adicionais de prática em água: "))
            self.testing_water += tempo
            print(f"Valor Atualizado: {self.testing_water}")
        else:
            tempo = int(input("Escreva a quantidade de horas adicionais de simulação: "))
            self.testing_sim += tempo
            print(f"Valor Atualizado: {self.testing_sim}")
        
        
auv1 = AUV('LUA', ["BAR30", "BMP180", "leakSensor", "DVL A50",  "MTi-G-AHRS", "3DM-CX5-10"], 8, 2022,250, 0)
auv2 = AUV('BRHUE', ["depthSensor", "MTi-G-AHRS"], 6, 2020, 200, 25)


#auv1.exibirAUV()

#                 LUA
#Ano de Construção: 2022
#Número de thursters: 8
#Tempo de teste no simulador: 250 hrs
#Tempo de teste em água: 0 hrs
#Sensores: ['BAR30', 'BMP180', 'leakSensor', 'DVL A50', 'MTi-G-AHRS', '3DM-CX5-10']

#auv2.exibirAUV()

#                 BRHUE
#Ano de Construção: 2020
#Número de thursters: 6
#Tempo de teste no simulador: 200 hrs   
#Tempo de teste em água: 25 hrs
#Sensores: ['depthSensor', 'MTi-G-AHRS']

#AUV.ranking()

#RANKING:
#1: LUA
#2: BRHUE

#AUV.exibirTodosAUVs()

#     Ano de Contrução | Nº de thrusters | Tempo de teste em simulação | Tempo de teste em água | Sensores
#LUA:        2022                  8                 250 hrs                          0 hrs          BAR30, BMP180, leakSensor, DVL A50, MTi-G-AHRS, 3DM-CX5-10
#BRHUE:      2020                  6                 200 hrs                         25 hrs          depthSensor, MTi-G-AHRS


#auv1.alteraçãoTempoTeste()

#Deseja alterar:
# [0] - Tempo em simulação
# [1] - Tempo em água
#0
#Escreva a quantidade de horas adicionais de simulação: 5
#Valor Atualizado: 255