# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 17:28:13 2022

@author: Lucas
"""
#%% Parte 1 Abertura de dados
import pandas as pd

dados = pd.read_csv('dados.csv')
dados.head()
#%%combinações 
from scipy.special import comb

combinacoes = comb(60,6)
probabilidade = 1/combinacoes
print('Combinacoes = %0.1f, Probabilidade = %0.15f' %(combinacoes, probabilidade))

#%%Dist binom
from scipy.stats import binom
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binom.html
n = 10
n_de_alt_por_q = 3
p = 1/n_de_alt_por_q
q = 1-p
k = 5
prob = binom.pmf(k,n,p)
print('%0.8f' %(prob))
#%%
# Em um concurso para preencher uma vaga de cientista de dados temos 
# um total de 10 questões de múltipla escolha com 3 alternativas possíveis 
# em cada questão. Cada questão tem o mesmo valor. Suponha que um candidato
# resolva se aventurar sem ter estudado absolutamente nada. Ele resolve fazer 
# a prova de olhos vendados e chutar todas as resposta. Assumindo que a prova 
# vale 10 pontos e a nota de corte seja 5, obtenha a probabilidade deste 
# candidato acertar 5 questões e também a probabilidade deste candidato passar 
# a próxima etapa do processo seletivo.
#%%
prob =binom.pmf(5,n,p)+binom.pmf(6,n,p)+binom.pmf(7,n,p)+binom.pmf(8,n,p)+binom.pmf(9,n,p)+binom.pmf(10,n,p)
prob

binom.pmf([5,6,7,8,9,10], n, p).sum()

a= 1 - binom.cdf(4, n, p)
a
binom.sf(4, n, p)
