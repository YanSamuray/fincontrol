import pandas as pd
from ofxparse import OfxParser

def extract_nubank_credit_card(file_path: str) -> pd.DataFrame:
    """
    Lê um arquivo OFX de cartão de crédito do Nubank e retorna um DataFrame.
    """
    with open(file_path, 'rb') as fileobj:
        ofx = OfxParser.parse(fileobj)
    
    # Capturando as transações e a data de fechamento/vencimento da fatura atual
    transactions = ofx.account.statement.transactions
    
    # NOVA LINHA: Pegamos a data final do extrato (que o Nubank usa como referência da fatura)
    data_fatura = ofx.account.statement.end_date
    
    data = []
    
    for txn in transactions:
        data.append({
            'id_transacao': txn.id,       
            'data_compra': txn.date,      
            'valor': txn.amount,          
            'descricao': txn.memo,        
            'tipo': txn.type,
            'data_fatura': data_fatura    # NOVA COLUNA: Carimba a qual fatura essa compra pertence
        })
        
    df = pd.DataFrame(data)
    
    return df