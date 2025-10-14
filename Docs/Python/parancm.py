import pandas as pd
import os
import sys

def barra_progresso(etapa_atual, total_etapas, descricao="", largura=50):
    progresso = int((etapa_atual / total_etapas) * largura)
    sys.stdout.write("\r[{:<{}}] {}% - {}".format("="*progresso, largura, int((etapa_atual/total_etapas*100)), descricao))
    sys.stdout.flush()
    if etapa_atual == total_etapas:
        print()

origem = os.path.expanduser("~/Downloads/Python/")

arquivo_1 = origem + 'EXP.csv'
arquivo_2 = origem + 'IMP.csv'
ncm = origem + 'NCM.csv'
pais = origem + 'pais.csv'
estados = origem + 'estados.csv'
municipios = origem + 'municipios.csv'
via = origem + 'VIA.csv'
urf = origem + 'URF.csv'

finalexp = pd.read_csv(arquivo_1,low_memory=False,sep=';',encoding='UTF-8')
finalimp = pd.read_csv(arquivo_2,low_memory=False,sep=';',encoding='UTF-8')

finalncm = pd.read_csv(ncm,low_memory=False,sep=';',encoding='latin1')
finalpais = pd.read_csv(pais,low_memory=False,sep=';',encoding='latin1')
finalestados = pd.read_csv(estados,low_memory=False,sep=';',encoding='latin1')
finalmunicipios = pd.read_csv(municipios,low_memory=False,sep=';',encoding='latin1')
finalvia = pd.read_csv(via,low_memory=False,sep=';',encoding='latin1')
finalurf = pd.read_csv(urf,low_memory=False,sep=';',encoding='latin1')

exp_finalexp = pd.concat([finalexp], ignore_index=True)
exp_finalimp = pd.concat([finalimp], ignore_index=True)

def processar(df):
    df = df.merge(finalpais[['CO_PAIS', 'NO_PAIS_ING']], on='CO_PAIS', how='left')
    df = df.merge(finalncm[['CO_NCM', 'NO_NCM_ING']], on='CO_NCM', how='left')
    df = df.merge(finalurf[['CO_URF', 'NO_URF']], on='CO_URF', how='left')
    df = df.merge(finalvia[['CO_VIA', 'NO_VIA']], on='CO_VIA', how='left')

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
        "MEIOS PROPRIOS": "OWN MEANS"
    }

    df['NO_VIA'] = df['NO_VIA'].str.strip().str.upper()
    df["NO_VIA"] = df["NO_VIA"].map(traducao_via)
    return df

exp_finalexp = processar(exp_finalexp)
exp_finalimp = processar(exp_finalimp)

exp_finalexp.to_csv(
    origem + 'exp_finalexp.csv', 
    index=False, 
    sep=';', 
    encoding='utf-8-sig')

exp_finalimp.to_csv(
    origem + 'exp_finalimp.csv', 
    index=False, 
    sep=';', 
    encoding='utf-8-sig')

barra_progresso(1,1, "Concluido!")
