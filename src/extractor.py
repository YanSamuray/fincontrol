import pandas as pd
from ofxparse import OfxParser

def extract_nubank_credit_card(file_path: str) -> pd.DataFrame:
    """
    Lê um arquivo OFX de cartão de crédito do Nubank e retorna um DataFrame.
    """
    # 1. Abrimos o arquivo em modo binário ('rb') para evitar problemas de codificação (encoding)
    with open(file_path, 'rb') as fileobj:
        ofx = OfxParser.parse(fileobj)
    
    # 2. Navegamos até a lista de transações
    transactions = ofx.account.statement.transactions
    
    # 3. Criamos uma lista vazia para guardar os dados extraídos
    data = []
    
    # 4. Loop para extrair as informações de cada compra
    for txn in transactions:
        data.append({
            'id_transacao': txn.id,       # Importante para evitar duplicidades no futuro
            'data_compra': txn.date,      # Quando a compra foi feita
            'valor': txn.amount,          # O valor (atenção aos sinais positivo/negativo)
            'descricao': txn.memo,        # O nome do estabelecimento (ex: "UBER", "MERCADO")
            'tipo': txn.type              # Débito ou Crédito
        })
        
    # 5. Transformamos a lista em um DataFrame do Pandas e retornamos
    df = pd.DataFrame(data)
    
    return df