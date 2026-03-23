import pandas as pd
from ofxparse import OfxParser

def extract_nubank_credit_card(file_path: str) -> pd.DataFrame:
    """
    Lê um arquivo OFX de cartão de crédito do Nubank e retorna um DataFrame.
    """
    with open(file_path, 'rb') as fileobj:
        ofx = OfxParser.parse(fileobj)
    
    transactions = ofx.account.statement.transactions
    data_fatura = ofx.account.statement.end_date
    
    data = []
    for txn in transactions:
        data.append({
            'id_transacao': txn.id,       
            'data_compra': txn.date,      
            'valor': txn.amount,          
            'descricao': txn.memo,        
            'tipo': txn.type,
            'data_fatura': data_fatura,
            'banco': 'NUBANK'
        })
        
    return pd.DataFrame(data)

def extract_bb_credit_card(file_path: str) -> pd.DataFrame:
    """
    Lê um arquivo OFX de cartão de crédito do Banco do Brasil e retorna um DataFrame.
    """
    with open(file_path, 'rb') as fileobj:
        ofx = OfxParser.parse(fileobj)
    
    transactions = ofx.account.statement.transactions
    
    try:
        data_fatura = ofx.account.statement.end_date
    except AttributeError:
        data_fatura = None
        
    data = []
    for txn in transactions:
        data.append({
            'id_transacao': txn.id,       
            'data_compra': txn.date,      
            'valor': txn.amount,          
            'descricao': txn.memo,        
            'tipo': txn.type,
            'data_fatura': data_fatura,
            'banco': 'BB'
        })
        
    return pd.DataFrame(data)