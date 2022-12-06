import pandas as pd
import numpy as np


rep_table = pd.read_excel("Representantes.xlsx")
states = {
    'AC': [],
    'AL': [],
    'AP': [],
    'AM': [],
    'BA': [],
    'CE': [],
    'ES': [],
    'GO': [],
    'MA': [],
    'MT': [],
    'MS': [],
    'MG': [],
    'PA': [],
    'PB': [],
    'PR': [],
    'PE': [],
    'PI': [],
    'RJ': [],
    'RN': [],
    'RS': [],
    'RO': [],
    'RR': [],
    'SC': [],
    'SP': [],
    'SE': [],
    'TO': [],
    'DF': [],
    'EX': []
}

print(states)

for i in range(len(rep_table)):
    ele = rep_table.iloc[i].tolist()
    states[ele[3]].append(ele)
    
print(states['SP'])