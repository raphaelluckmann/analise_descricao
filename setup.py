import sys
from cx_Freeze import setup, Executable


# "scipy", "numpy","nltk", "pandas", "os",  "sklearn",

packages = [ "analise_descricao.analise_produtos" ]
# Definir o que deve ser incluído na pasta final
arquivos = [
      (r'analise_descricao\Modelo\Base_Analise.xlsx', 'analise_descricao/Modelo/Base_Analise.xlsx'),
    (r'analise_descricao\nltk_data', 'nltk_data')
            

]
# Saida de arquivos
base = None
if sys.platform =='win32':
    base='Win32GUI'

configuracao = Executable(
            script='analise_descricao\interface-tq.py',
            base=base
            
        )

        # Configurar o executável
setup(
            name='Analisador',
            version='2.0',
            description='Este programa analisa por  AI qualquer descrição',
            author='Raphael Luckmann',
            options={'build_exe':{
                'packages': packages,
                'include_files': arquivos,

                
                'include_msvcr': True
                
            }},
            
            executables=[configuracao]
        )


