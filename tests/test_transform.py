import pytest
import pandas as pd
from src.transform import clean_sales_data

def test_remove_duplicates():
    """Test que duplicados son removidos correctamente"""
    df = pd.DataFrame({
        'order_id': [1, 1, 2],
        'product': ['A', 'A', 'B'],
        'quantity': [2, 2, 3],
        'price': [10, 10, 20]
    })
    result = clean_sales_data(df)
    assert len(result) == 2
    assert result['order_id'].is_unique

def test_handle_missing_values():
    """Test que valores nulos son manejados correctamente"""
    df = pd.DataFrame({
        'order_id': [1, 2],
        'product': ['A', 'B'],
        'quantity': [1, None],
        'price': [10, 20]
    })
    result = clean_sales_data(df)
    assert result['quantity'].isna().sum() == 0
    assert 'total' in result.columns

