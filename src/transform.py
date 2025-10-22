"""
Module for data transformation and cleaning
"""
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def clean_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transforma y limpia datos de ventas
    
    Realiza las siguientes transformaciones:
    - Elimina duplicados basado en 'order_id'
    - Rellena valores nulos con 0
    - Calcula columna 'total' = price * quantity
    
    Args:
        df (pd.DataFrame): DataFrame con datos raw de ventas
        
    Returns:
        pd.DataFrame: DataFrame transformado y limpio
    """
    try:
        logger.info("Iniciando limpieza y transformación de datos...")
        df = df.drop_duplicates(subset=["order_id"])
        df = df.fillna(0)
        df["total"] = df["price"] * df["quantity"]
        logger.info("Transformación completada exitosamente.")
        return df
    except Exception as e:
        logger.error(f"Error transformando datos: {str(e)}")
        raise

if __name__ == "__main__":
    from src.extract import extract_from_csv

    df_raw = extract_from_csv("data/raw/sales_data.csv")
    df_clean = clean_sales_data(df_raw)
    print(df_clean.head())

