"""
Module for data extraction from various sources
"""
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def extract_from_csv(file_path: str) -> pd.DataFrame:
    """
    Extract data from CSV file
    
    Args:
        file_path (str): Path to CSV file
        
    Returns:
        pd.DataFrame: Extracted data
    """
    try:
        logger.info(f"Extracting data from {file_path}")
        df = pd.read_csv(file_path)
        logger.info(f"Successfully extracted {len(df)} rows")
        return df
    except Exception as e:
        logger.error(f"Error extracting data: {str(e)}")
        raise

if __name__ == "__main__":
    # Example usage
    df = extract_from_csv("data/raw/sales_data.csv")
    print(df.head())
