# models/
    my_first_dbt_model.sql
    qapython.py


# models/qapython.py

import pandas as pd

def model(dbt, session):
    # Correctly reference the model
    df = dbt.ref('my_first_dbt_model').to_pandas()
    
    # Perform transformations
    df['new_column'] = df['existing_column'] * 2
    
    return df


