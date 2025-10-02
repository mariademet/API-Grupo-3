import pandas as pd
import os
import sys

def barra_progresso(etapa_atual, total_etapas, descricao="", largura=50):
    progresso = int((etapa_atual / total_etapas) * largura)
    sys.stdout.write("\r[{:<{}}] {}% - {}".format("="*progresso, largura, int((etapa_atual/total_etapas*100)), descricao))
    sys.stdout.flush()
    if etapa_atual == total_etapas:
        print()

data = {'coluna_1':[1.5,2.0,1.7,2.2,1.9],
        'coluna_2':[10.0,12.0,11.5,13,11.0],
        'coluna_3':[0,1,0,1,0],
        'coluna_4':[1,0,1,1,0],
        'coluna_5':[20.5,25.5,22.0,27.0,23.0]}
df = pd.DataFrame(data)

origem = os.path.expanduser("~/Downloads/")

arquivo_1 = origem + 'ano.csv'
arquivo_2 = origem + 'mun.csv'
ncm = origem + 'NCM.csv'
pais = origem + 'pais.csv'
estados = origem + 'estados.csv'
municipios = origem + 'municipios.csv'
via = origem + 'VIA.csv'
urf = origem + 'URF.csv'
sh = origem + 'sh.csv'

finalmunicipio = pd.read_csv(arquivo_2,low_memory=False,sep=';',encoding='UTF-8')
finalncm = pd.read_csv(ncm,low_memory=False,sep=';',encoding='latin1')
finalpais = pd.read_csv(pais,low_memory=False,sep=';',encoding='latin1')
finalestados = pd.read_csv(estados,low_memory=False,sep=';',encoding='latin1')
finalmunicipios = pd.read_csv(municipios,low_memory=False,sep=';',encoding='latin1')
finalsh = pd.read_csv(sh,low_memory=False,sep=';',encoding='latin1')

finalpais = finalpais[['CO_PAIS','NO_PAIS_ING']].drop_duplicates(subset='CO_PAIS')
finalmunicipios = finalmunicipios[['CO_MUN','NO_MUN']].drop_duplicates(subset='CO_MUN')
finalsh = finalsh[['SH4','NO_SH4_ING']].drop_duplicates(subset='SH4')

exp_final = pd.concat([finalmunicipio], ignore_index=True)
exp_final = exp_final.merge(finalpais[['CO_PAIS', 'NO_PAIS_ING']],on='CO_PAIS',how='left')
exp_final = exp_final.merge(finalmunicipios[['CO_MUN', 'NO_MUN']],on='CO_MUN',how='left')
exp_final = exp_final.merge(finalsh[['SH4', 'NO_SH4_ING']],on='SH4',how='left')
exp_final.to_csv(
    origem + 'exp_finalmunicipio.csv',
    index=False,
    sep=";",
    encoding="utf-8-sig")

barra_progresso(1,1, "Concluido!")
