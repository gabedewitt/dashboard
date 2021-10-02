from enum import unique
from pkg_resources import run_script
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
columns_names = ['DataArquivamento', 'DataAbertura', 'Regiao', 'UF', 'strRazaoSocial',
       'strNomeFantasia', 'Tipo', 'NumeroCNPJ', 'DescCNAEPrincipal',
       'Atendida', 'DescricaoAssunto', 'DescricaoProblema', 'SexoConsumidor',
       'FaixaEtariaConsumidor', 'CEPConsumidor', 'Ano', 'Mês', 'Dia',
       'Dia da Semana', 'Tempo de Atendimento']

st.set_page_config("wide", 
                   initial_sidebar_state="collapsed",
                    page_icon= '📊')

@st.cache
def create_df():
    dict_arq ={ 2018: 'dados_PROCON/reclamacoes-fundamentadas-2018-em-zip/CNRF2018.csv',
                2017: 'dados_PROCON/cnrf2017/CNRF_2017.csv',
                2019: 'dados_PROCON/crf2019-dados-abertos/CRF2019 Dados Abertos.csv',
                2012: 'dados_PROCON/reclamacoes-fundamentadas-sindec-2012/reclamacoes-fundamentadas-sindec-2012.csv',
                2013: 'dados_PROCON/reclamacoes-fundamentadas-sindec-2013-1/reclamacoes-fundamentadas-sindec-2013.csv',
                2014: 'dados_PROCON/reclamacoes-fundamentadas-sindec-2014/reclamacoes-fundamentadas-sindec-2014.csv',
                2015: 'dados_PROCON/reclamacoes-fundamentadas-sindec-2015/reclamacoes-fundamentadas-sindec-2015.csv',
                2016: 'dados_PROCON/reclamacoes-fundamentadas-sindec-2016v2/reclamacoes-fundamentadas-sindec-2016_v2.csv'}
    dict_problematicos ={2009: 'dados_PROCON/reclamacoes-fundamentadas-sindec-2009/reclamacoes-fundamentadas-sindec-2009.csv',
                        2010: 'dados_PROCON/reclamacoes-fundamentadas-sindec-2010/reclamacoes-fundamentadas-sindec-2010.csv',
                        2011: 'dados_PROCON/reclamacoes-fundamentadas-sindec-2011/reclamacoes-fundamentadas-sindec-2011.csv',
                        }  

    pd.options.display.float_format = '{:.0f}'.format

    nomes_atrib = ['AnoCalendario', 'DataArquivamento', 'DataAbertura', 'CodigoRegiao',
        'Regiao', 'UF', 'strRazaoSocial', 'strNomeFantasia', 'Tipo',
        'NumeroCNPJ', 'RadicalCNPJ', 'RazaoSocialRFB', 'NomeFantasiaRFB',
        'CNAEPrincipal', 'DescCNAEPrincipal', 'Atendida', 'CodigoAssunto',
        'DescricaoAssunto', 'CodigoProblema', 'DescricaoProblema',
        'SexoConsumidor', 'FaixaEtariaConsumidor', 'CEPConsumidor']

    df_names = []

    for year in dict_problematicos.keys(): 
        caminho = str(dict_problematicos.get(year))
        name = "df_"+str(year)
        locals()[name] = pd.read_csv(caminho, sep=';', error_bad_lines=False, encoding = 'latin')
        locals()[name].columns = nomes_atrib
        df_names.append(locals()[name])

    for year in dict_arq.keys(): 
        caminho = str(dict_arq.get(year))
        name = "df_"+str(year)
        locals()[name] = pd.read_csv(caminho, sep=';', error_bad_lines=False, encoding = "utf-8", warn_bad_lines= False)
        locals()[name].columns = nomes_atrib
        df_names.append(locals()[name])

    df_all = pd.concat(df_names)
    df_all.drop(['AnoCalendario','CodigoRegiao','RadicalCNPJ','NomeFantasiaRFB','RazaoSocialRFB','CNAEPrincipal','CodigoAssunto','CodigoProblema'],inplace= True, axis = 1)
    df_all['DataArquivamento'] = pd.to_datetime(df_all['DataArquivamento'], format='%Y-%m-%d %H:%M:%S.%f') #%Y-%m-%d %H:%M:%S
    df_all['DataAbertura'] =  pd.to_datetime(df_all['DataAbertura'], format='%Y-%m-%d %H:%M:%S.%f') #%Y-%m-%d %H:%M:%S
    df_all['Ano'] = pd.DatetimeIndex(df_all['DataArquivamento']).year
    df_all['Mês'] = pd.DatetimeIndex(df_all['DataArquivamento']).month
    df_all['Dia'] = pd.DatetimeIndex(df_all['DataArquivamento']).day
    df_all['Dia da Semana'] = pd.DatetimeIndex(df_all['DataArquivamento']).weekday
    df_all['CEPConsumidor'] = df_all['CEPConsumidor'].astype(str)
    df_all['Tempo de Atendimento'] = df_all['DataArquivamento'] - df_all['DataAbertura']
    return df_all
 

df_org = create_df()

pd.set_option('precision', 0)
with st.sidebar: 
    year = st.selectbox('Selecione o ano', df_org.Ano.dropna().sort_values().unique())
    st.write("O ano  destacado é " + str(year))
    setor = st.selectbox('Selecione o setor', df_org.DescCNAEPrincipal.dropna().sort_values().unique())
    st.write("O setor destacado é " + str(setor))


st.bar_chart(df_org.Ano.value_counts(), )

df = df_org.loc[df_org['Ano'] == year]

df1 = df.DescCNAEPrincipal.value_counts().head(10)
fig1 = px.bar(df1, orientation= 'h', color = df1.index)
fig1.update_yaxes(showticklabels=False)
fig1.update_layout(showlegend=False)
st.plotly_chart(fig1, use_container_width=True)
st.dataframe(df1.index)
col1, col2 = st.columns(2)

df = df.loc[df['DescCNAEPrincipal'] == setor]
df2 = df.SexoConsumidor.value_counts()
fig2 = px.pie(df2, values = df2.values, color = df2.index, hole=.3)
col1.plotly_chart(fig2, use_container_width=True)
col1.dataframe(df2)

df3 = df.Atendida.value_counts()
fig3 = px.pie(df3, values = df3.values, color = df3.index, hole=.3)
col2.plotly_chart(fig3, use_container_width=True)
col2.dataframe(df3)

df4 = df.FaixaEtariaConsumidor.value_counts()
fig4 = px.bar(df4, orientation= 'v', color = df4.index)
st.plotly_chart(fig4, use_container_width=True)
