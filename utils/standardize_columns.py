def standardize_column_names(df):
    """
    Standardizes the column names of a pandas DataFrame by:
    - Converting column names to lowercase.
    - Replacing spaces with underscores.

    Parameters:
        df (pd.DataFrame): The input DataFrame whose column names are to be standardized.

    Returns:
        pd.DataFrame: A new DataFrame with standardized column names.
    
    Example:
        >>> df = pd.DataFrame(columns=["First Name", "Last Name", "Age"])
        >>> df_standardized = standardize_column_names(df)
        >>> df_standardized.columns
        Index(['first_name', 'last_name', 'age'], dtype='object')
    """
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    return df