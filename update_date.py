#!/usr/bin/env python3
"""
Script para atualizar a data no README.md automaticamente.
Atualiza a data entre as tags <!--DATE--> com a data atual.
"""

import re
from datetime import datetime

# Caminho do arquivo README
README_PATH = 'README.md'

# Formato de data brasileiro (dd/mm/yyyy)
DATE_FORMAT = '%d/%m/%Y'

def update_readme_date():
    """Atualiza a data no README.md com a data atual."""
    # Obter data atual no formato brasileiro
    current_date = datetime.now().strftime(DATE_FORMAT)
    
    # Ler o conteúdo do README
    with open(README_PATH, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Atualizar a data entre as tags <!--DATE-->
    pattern = r'<!--DATE-->.*?<!--DATE-->'
    replacement = f'<!--DATE-->{current_date}<!--DATE-->'
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # Escrever o conteúdo atualizado de volta ao arquivo
    with open(README_PATH, 'w', encoding='utf-8') as file:
        file.write(new_content)
    
    print(f'✅ README atualizado com sucesso! Data: {current_date}')

if __name__ == '__main__':
    update_readme_date()
