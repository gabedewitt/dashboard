import pandas as pd


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
  print('OK {}'.format(name))

for year in dict_arq.keys(): 
  caminho = str(dict_arq.get(year))
  name = "df_"+str(year)
  locals()[name] = pd.read_csv(caminho, sep=';', error_bad_lines=False, encoding = "utf-8", warn_bad_lines= False)
  locals()[name].columns = nomes_atrib
  df_names.append(locals()[name])
  print('OK {}'.format(name))

df_all = pd.concat(df_names)

df_all.to_csv('dados_PROCON/dados_consolidados.csv')

