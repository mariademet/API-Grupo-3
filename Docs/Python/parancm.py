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

origem = os.path.expanduser("~/Downloads/Python")

arquivo_1 = origem + 'ano.csv'
ncm = origem + 'NCM.csv'
pais = origem + 'pais.csv'
estados = origem + 'estados.csv'
municipios = origem + 'municipios.csv'
via = origem + 'VIA.csv'
urf = origem + 'URF.csv'


finalncm2024 = pd.read_csv(arquivo_1,low_memory=False,sep=';',encoding='UTF-8')
finalncm = pd.read_csv(ncm,low_memory=False,sep=';',encoding='latin1')
finalpais = pd.read_csv(pais,low_memory=False,sep=';',encoding='latin1')
finalestados = pd.read_csv(estados,low_memory=False,sep=';',encoding='latin1')
finalmunicipios = pd.read_csv(municipios,low_memory=False,sep=';',encoding='latin1')
finalvia = pd.read_csv(via,low_memory=False,sep=';',encoding='latin1')
finalurf = pd.read_csv(urf,low_memory=False,sep=';',encoding='latin1')

exp_final = pd.concat([finalncm2024], ignore_index=True)
exp_final = exp_final.merge(finalpais[['CO_PAIS', 'NO_PAIS_ING']],on='CO_PAIS',how='left')
exp_final = exp_final.merge(finalncm[['CO_NCM', 'NO_NCM_ING']],on='CO_NCM',how='left')
exp_final = exp_final.merge(finalurf[['CO_URF', 'NO_URF']],on='CO_URF',how='left')
exp_final = exp_final.merge(finalvia[['CO_VIA', 'NO_VIA']],on='CO_VIA',how='left')

traducao_via = {
    "ENTRADA/SAIDA FICTA": "FICTITIOUS ENTRY/EXIT",
        "VIA DESCONHECIDA": "UNKNOWN MEANS",
        "POR REBOQUE": "BY TOW/TRAILER",
        "COURIER": "COURIER",
        "VICINAL FRONTEIRICO": "LOCAL BORDER ROUTE",
        "DUTOS": "PIPES / DUCTS",
        "EM MAOS": "BY HAND",
        "VIA NAO DECLARADA": "UNDECLARED MEANS",
        "MARITIMA": "MARITIME",
        "FLUVIAL": "RIVER",
        "LACUSTRE": "LAKE / INLAND WATERWAY",
        "AEREA": "AIR",
        "POSTAL": "POSTAL",
        "FERROVIARIA": "RAIL",  
        "RODOVIARIA": "ROAD",
        "CONDUTO/REDE DE TRANSMISSAO": "CONDUIT / TRANSMISSION NETWORK",
        "MEIOS PROPRIOS": "OWN MEANS"}
exp_final['NO_VIA'] = exp_final['NO_VIA'].str.strip().str.upper()
exp_final["NO_VIA"] = exp_final["NO_VIA"].map(traducao_via)
exp_final.to_csv(
    origem + 'exp_finalNCM.csv',
    index=False,
    sep=";",
    encoding="utf-8-sig")

barra_progresso(1,1, "Concluido!")

