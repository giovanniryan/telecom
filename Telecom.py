#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd

# p1. importar base de dados pro python
tabela = pd.read_csv(r"C:\Users\giova\OneDrive\Área de Trabalho\Aula 2 - Telecom\telecom_users.csv")

# visualizar base de dados


# entender as informações disponíveis 
# descobrir problemas da base de dados
tabela = tabela.drop("Unnamed: 0", axis=1) #drop retira uma coluna ou linha (axis=0 retira uma linha e =1 retira uma coluna)
display(tabela)


# In[9]:


# p3. tratamento de dados
# analisar se o python le as info no formato correto #object = texto / float64 = float /int = inteiro
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")


print(tabela.info()) 
# conferir se existe alguma coluna completamente vazia (NaN)

# how = all ou any (com todas informacoes vazias ou pelo menos uma informacao eh vazia)
tabela = tabela.dropna(how="all", axis=1)

# verificar a info em alguma linha vazia
tabela = tabela.dropna(how="any", axis=0)


# In[31]:


# p4. analise global - analise inicial
# quantos clientes cancelaram e quantos clientes mativeram a assinatura
print(tabela["Churn"].value_counts())
# % dos clientes
print(tabela["Churn"].value_counts(normalize= True))


# In[42]:


# p5. analise detalhada
import plotly.express as px

# criar o grafico

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="Churn")
    # exibir o grafico
    grafico.show()


# <h2> Conclusoes </h2>

# In[ ]:


- Clientes cancelam nos primeiros meses
    - Problemas na entrada
    - Problemas na retenção de clientes

- Pessoas com familias na mesma operadora tem menos chance de cancelar 

- Quantos mais serviços ele tem, menor a chance de cancelar 

- Algum problema no serviço de fibra
    - A taxa de cancelamento na fibra está maior

- Contrato mensal tem muita taxa de cancelamento
    - Descontos para plano anual ou 3 meses
    
- Boleto taxa alta
    - Desconto nas outras formas de pagamento

