import os
import pandas as pd
import zipfile
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

dict_zip ={ 2018: 'dados_PROCON/zips/reclamacoes-fundamentadas-2018-em-zip.zip',
            2017: 'dados_PROCON/zips/cnrf2017.zip',
            2019: 'dados_PROCON/zips/crf2019-dados-abertos.zip',
            2012: 'dados_PROCON/zips/reclamacoes-fundamentadas-sindec-2012.zip',
            2013: 'dados_PROCON/zips/reclamacoes-fundamentadas-sindec-2013-1.zip',
            2014: 'dados_PROCON/zips/reclamacoes-fundamentadas-sindec-2014.zip',
            2015: 'dados_PROCON/zips/reclamacoes-fundamentadas-sindec-2015.zip',
            2016: 'dados_PROCON/zips/cnrf2017.zip',
            2009: 'dados_PROCON/zips/reclamacoes-fundamentadas-sindec-2009.zip',
            2010: 'dados_PROCON/zips/reclamacoes-fundamentadas-sindec-2010.zip',
            2011: 'dados_PROCON/zips/reclamacoes-fundamentadas-sindec-2011.zip'}

list_zip =['dados_PROCON/zips/reclamacoes-fundamentadas-2018-em-zip.zip',
           'dados_PROCON/zips/cnrf2017.zip',
           'dados_PROCON/zips/crf2019-dados-abertos.zip',
           'dados_PROCON/zips/reclamacoes-fundamentadas-sindec-2012.zip',
           'dados_PROCON/zips/reclamacoes-fundamentadas-sindec-2013-1.zip',
           'dados_PROCON/zips/reclamacoes-fundamentadas-sindec-2014.zip',
           'dados_PROCON/zips/reclamacoes-fundamentadas-sindec-2015.zip',
           'dados_PROCON/zips/cnrf2017.zip',
           'dados_PROCON/zips/reclamacoes-fundamentadas-sindec-2009.zip',
           'dados_PROCON/zips/reclamacoes-fundamentadas-sindec-2010.zip',
           'dados_PROCON/zips/reclamacoes-fundamentadas-sindec-2011.zip']

try: 
  os.path('dados_PROCON/cnrf2017')
except:
  for caminho in list_zip:
    caminho_certo = 'dados_PROCON/' + caminho[:-4]
    with zipfile.ZipFile(caminho, 'r') as zip_ref:
      zip_ref.extractall(caminho_certo)


