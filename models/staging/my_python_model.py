# my_python_model.py

def model(dbt, session):
    # Import necessary modules
    import pandas as pd

    # This is an example of creating a simple DataFrame
    data = {
        "ID": [1, 2, 3],
        "Name": ["Alice", "Bob", "Charlie"]
    }
    df = pd.DataFrame(data)

    # Convert the DataFrame to a SQL table
    session.write_pandas(df, "my_python_model", auto_create_table=True)

    # Returning the table name
    return "my_python_model"
