# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 23:55:50 2022

@author: fabio
"""


#%% Importação de bibliotecas e configuração de diretório

import matplotlib.pyplot as plt
import numpy as np
import os
import scipy.io as sc
import statistics as st
import scipy.stats as ss
import scipy.fft as fft

# Direcionamento do diretório das imagens
#os.chdir(r'E:\Arquivos\ENGENHARIA MÉDICA - PRES\Atividade Prática 2')
from extraicarac import extraicarac


#%% Leitura e extração inicial de dados

A1 = sc.loadmat('Dados')

# O sinal possui 1179 trechos de 30 segundos cada
sinal = A1['SINAL']

# Os estagios são classificados como 0 = Vigília; 1~4 = Estágio 1~4; 5 = REM
estagios = A1['ESTAGIOS']


#%% Atividade 1 - A

# Leitura e entendimento da função extraicarac da biblioteca extraicarac

# Input sin - Matriz de sinais/trechos
# (Linhas - Sinais/Trechos, Colunas - Domínio do tempo dividido conforme frequência de amostragem do sinal)
# Input freq - Frequência de amostragem dos sinais em Hz
# Input bandas - Dicionário de nomes de bandas (keys) e intervalos das bandas de frequência (valores - arrays)
# Exemplo: bandas={'delta 1':[0.5,2.5],'delta 2':[2.5,4],'teta 1':[4,6],'teta 2':[6,8], 'alfa':[8,12],'beta':[12,20],'gama':[10,45]}


def extraicarac_comentada(sin, freq, bandas):
    (S, X) = np.shape(sin) # S é o número de sinais/trechos e X é o tamanho dos sinais no tempo
    nc = 15 # número de características
    car = np.zeros((S, nc)) # Matriz de características - Cada sinal/trecho é associado a um array de nc características
    nomesc = [None]*nc # Array de nome das nc características
    
    # Início do loop de análise dos sinais
    for s in range(S):
        
        # Cálculo da média - car[s, 0]
        car[s, 0] = np.mean(sin[s, :])
        nomesc[0] = 'Média'
    
        # Variância - car[s, 1]
        var0 = np.var(sin[s, :], ddof = 1) # ddof define o dividor -> N - ddof (default = 0)
        car[s, 1] = var0
        nomesc[1] = 'Variância'
    
        # Mobilidade - car[s, 2]
        x1 = np.diff(sin[s, :]) # vetor de diferenças de 1ª ordem do sinal a[n+1] - a[n], a[n+2] - a[n]...
        var1 = np.var(x1, ddof = 1) # variância associada ao vetor de diferenças entre os elementos do sinal
        mob = var1/var0
        car[s, 2] = mob
        nomesc[2] = 'Mobilidade'
    
        # Complexidade Estatística - car[s, 3]
        x2 = np.diff(x1)
        var2 = np.var(x2, ddof = 1)
        ce = (var2/var1 - var1/var0)**(1/2)
        car[s, 3] = ce
        nomesc[3] = 'Complexidade Estatística'
    
        # Cálculo do Espectro
        yf = np.abs(fft.fft(sin[s, :] - car[s, 0]))**2 # Pegando o módulo do sinal menos a média e elevando ao quadrado
        yf = yf/np.size(yf) # Normalização do espectro
        yf = yf[0:X//2] # Divisão do espectro em 2
        xf = np.linspace(0.0, 1.0/(2.0/freq), X//2) # Eixo de frequências do espectro
        Yf = yf/np.sum(yf) # Normalização do espectro (Agiliza em outros cálculos)
    
        # Frequência Central do Espectro - car[s, 4]
        car[s, 4] = np.sum(xf*Yf)
        nomesc[4] = 'Frequência Central'
        
        # Potência na Frequência Central - car[s, 5]
        ifc = np.abs(xf - car[s, 4]) == np.min(np.abs(xf - car[s,4])) # Índice da frequência central
        car[s, 5] = yf[ifc]
        nomesc[5] = 'Potência Freq Central'
        
        # Largura de banda no Espectro - car[s, 6]
        car[s, 6] = np.sqrt(np.sum(((xf - car[s, 4])**2)*Yf))
        nomesc[6] = 'Largura de Banda'
        
        # Frequência de margem do Espectro - car[s, 7]
        sw = np.cumsum(Yf) # Soma cumulativa
        f = np.max(np.where(sw <= 0.9)[0]) # Busca pelo índice onde
        car[s, 7] = xf[f]
        nomesc[7] = 'Frequência de Margem'
        
        # Potência Espectrais normalizadas nas bandas - car[s, 8 até 14]
        for ib, b in enumerate(bandas):
            car[s, 8 + ib] = sum(Yf[((xf >= bandas[b][0]) & (xf <= bandas[b][1]))])
            nomesc[8 + ib] = b
    
    return (car, nomesc)

# Função Adenauer        
teste = extraicarac(sinal, 100, bandas={'delta 1':[0.5,2.5],'delta 2':[2.5,4],'teta 1':[4,6],'teta 2':[6,8], 'alfa':[8,12],'beta':[12,20],'gama':[20,45]})
# Função Adenauer comentada
teste2 = extraicarac_comentada(sinal, 100, bandas={'delta 1':[0.5,2.5],'delta 2':[2.5,4],'teta 1':[4,6],'teta 2':[6,8], 'alfa':[8,12],'beta':[12,20],'gama':[20,45]})


#%% Atividade 1 - B

'''
Usar a função para calcular as características de cada um dos trechos do EEG do exame de polisonografia.
Gerar histogramas destas características para inspecioná-las individualmente
'''

carac = extraicarac(sinal, 100, bandas={'delta 1':[0.5,2.5],'delta 2':[2.5,4],'teta 1':[4,6],'teta 2':[6,8], 'alfa':[8,12],'beta':[12,20],'gama':[20,45]})
nomes_estag = ['vigília', 'estágio 1', 'estágio 2', 'estágio 3', 'estágio 4', 'REM']
# Estágios: 0 (0-479); 1 (480-535); 2 (536-942); 3 (943-977); 4 (978-1076); 5 (1077-1178)

# Histogramas das características nos estágios de sono

for i in range (len(carac[1])):
    fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3, constrained_layout = True)
    ax1.hist(carac[0][0:479, i])
    ax1.set_title(carac[1][i] + ' ' + nomes_estag[0])
    ax2.hist(carac[0][480:535, i])
    ax2.set_title(carac[1][i] + ' ' + nomes_estag[1])
    ax3.hist(carac[0][536:942, i])
    ax3.set_title(carac[1][i] + ' ' + nomes_estag[2])
    ax4.hist(carac[0][943:977, i])
    ax4.set_title(carac[1][i] + ' ' + nomes_estag[3])
    ax5.hist(carac[0][978:1076, i])
    ax5.set_title(carac[1][i] + ' ' + nomes_estag[4])
    ax6.hist(carac[0][1077:1178, i])
    ax6.set_title(carac[1][i] + ' ' + nomes_estag[5])
    
    plt.show()


#%% Atividade 1 - C
'''
Construir os espaços de características em 2D, mostrando classes com cores diferentes
'''

plt.xlabel(carac[1][2])
plt.ylabel(carac[1][3])
plt.scatter(carac[0][0:479,2], carac[0][0:479,3], c = 'red', label = nomes_estag[0], marker = 'o')
plt.scatter(carac[0][480:535,2], carac[0][480:535,3], c = 'blue', label = nomes_estag[1])
plt.scatter(carac[0][536:942,2], carac[0][536:942,3], c = 'green', label = nomes_estag[2])
plt.scatter(carac[0][943:977,2], carac[0][943:977,3], c = 'yellow', label = nomes_estag[3])
plt.scatter(carac[0][978:1076,2], carac[0][978:1076,3], c = 'black', label = nomes_estag[4])
plt.scatter(carac[0][1077:1178,2], carac[0][1077:1178,3], c = 'orange', label = nomes_estag[5])
plt.legend()



#%% Atividade 1 - D
'''
Inspecionar as classes em espaços de características em 3D. Em particular, observar os valores
para os estágios correspondentes à vigília, ao sono REM e ao sono não REM, estudando combinações
de características como a mobilidade, complexidade estatística, potência nas bandas de baixa
frequência, frequência central e a frequência de margem.
'''

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(projection='3d')
ax.scatter(carac[0][0:479,2], carac[0][0:479,4], carac[0][0:479,8], color = 'blue')
ax.scatter(carac[0][978:1076,2], carac[0][978:1076,4], carac[0][978:1076,8], color = 'red')
ax.scatter(carac[0][1077:1178,2], carac[0][1077:1178,4], carac[0][1077:1178,8], color = 'green')
ax.set_xlabel(carac[1][2])
ax.set_ylabel(carac[1][4])
ax.set_zlabel(carac[1][8])
plt.show()


