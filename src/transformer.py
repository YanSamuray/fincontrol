import pandas as pd

def clean_credit_card_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Recebe o DataFrame bruto do cartão de crédito e aplica as regras da Camada Silver.
    """
    # Cria uma cópia para evitar avisos do Pandas ao modificar o DataFrame original
    df_clean = df.copy()
    
    # 1. Padroniza a data (converte para datetime e remove o fuso horário)
    df_clean['data_compra'] = pd.to_datetime(df_clean['data_compra']).dt.tz_localize(None)
    
    # 2. Garante que o valor é um float
    df_clean['valor'] = df_clean['valor'].astype(float)
    
    # 3. Limpa a descrição (remove espaços extras e deixa tudo em maiúsculo para facilitar filtros depois)
    df_clean['descricao'] = df_clean['descricao'].astype(str).str.strip().str.upper()
    
    # 4. Ordena os dados cronologicamente
    df_clean = df_clean.sort_values(by='data_compra').reset_index(drop=True)
    
    return df_clean