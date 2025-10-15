import pandas as pd
import os
import sys

def barra_progresso(etapa_atual, total_etapas, descricao="", largura=50):
    progresso = int((etapa_atual / total_etapas) * largura)
    sys.stdout.write("\r[{:<{}}] {}% - {}".format("="*progresso, largura, int((etapa_atual/total_etapas*100)), descricao))
    sys.stdout.flush()
    if etapa_atual == total_etapas:
        print()

origem = os.path.expanduser("~/Downloads/Python/arquivos/")
codigos = os.path.expanduser("~/Downloads/Python/codigos/")
destino = os.path.expanduser("~/Downloads/Python/")

arquivo_1 = origem + 'EXP_2023_MUN.csv'  
arquivo_2 = origem + 'EXP_2024_MUN.csv'  
arquivo_3 = origem + 'EXP_2025_MUN.csv'   
arquivo_4 = origem + 'IMP_2023_MUN.csv'
arquivo_5 = origem + 'IMP_2024_MUN.csv'
arquivo_6 = origem + 'IMP_2025_MUN.csv'
pais = codigos + 'pais.csv'
municipios = codigos + 'municipios.csv'
sh = codigos + 'sh.csv'

finalexp2023 = pd.read_csv(arquivo_1,low_memory=False,sep=';',encoding='UTF-8')
finalexp2024 = pd.read_csv(arquivo_2,low_memory=False,sep=';',encoding='UTF-8')
finalexp2025 = pd.read_csv(arquivo_3,low_memory=False,sep=';',encoding='UTF-8')
finalimp2023 = pd.read_csv(arquivo_4,low_memory=False,sep=';',encoding='UTF-8')
finalimp2024 = pd.read_csv(arquivo_5,low_memory=False,sep=';',encoding='UTF-8')
finalimp2025 = pd.read_csv(arquivo_6,low_memory=False,sep=';',encoding='UTF-8')

finalpais = pd.read_csv(pais,low_memory=False,sep=';',encoding='latin1')
finalmunicipios = pd.read_csv(municipios,low_memory=False,sep=';',encoding='latin1')
finalsh = pd.read_csv(sh,low_memory=False,sep=';',encoding='latin1')

finalpais = finalpais[['CO_PAIS','NO_PAIS_ING']].drop_duplicates(subset='CO_PAIS')
finalmunicipios = finalmunicipios[['CO_MUN','NO_MUN']].drop_duplicates(subset='CO_MUN')
finalsh = finalsh[['SH4','NO_SH4_ING']].drop_duplicates(subset='SH4')

exp_finalexp = pd.concat([finalexp2023, finalexp2024, finalexp2025], ignore_index=True)
exp_finalimp = pd.concat([finalimp2023, finalimp2024, finalimp2025], ignore_index=True)

def processar(df):
    df = df.merge(finalpais[['CO_PAIS', 'NO_PAIS_ING']],on='CO_PAIS',how='left')
    df = df.merge(finalmunicipios[['CO_MUN', 'NO_MUN']],on='CO_MUN',how='left')
    df = df.merge(finalsh[['SH4', 'NO_SH4_ING']],on='SH4',how='left')
    return df

exp_finalexp = processar(exp_finalexp)
exp_finalimp = processar(exp_finalimp)

exp_finalexp.to_csv(
    destino + 'exp_munexp.csv',
    index=False,
    sep=";",
    encoding="utf-8-sig")

exp_finalimp.to_csv(
    destino + 'exp_munimp.csv',
    index=False,
    sep=";",
    encoding="utf-8-sig")
barra_progresso(1,1, "Concluido!")
