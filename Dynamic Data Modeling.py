import pandas as pd

flat_file_path = "ADD PATH"
df = pd.read_csv(flat_file_path)


new_sentence_table = ['Column_1','Sentence','Column_2','Column_3']

new_subTheme_table= ['Column_4', 'Theme']

new_sku_table= ['Column_6', 'Column_7', 'SKU']



Sentence_table=df[new_sentence_table].drop_duplicates(subset=['Sentence','Column_2','Column_3'])

Subtheme_table=df[new_subTheme_table].drop_duplicates(subset=['Column_5'])

SKU_table=df[new_sku_table].drop_duplicates(subset=['Column_7','SKU'])


def add_surrogate_key(df, key_name):
    df[key_name] = range(1, len(df) + 1)
    return df

required_columns_sentence =['Sentence_Key','Sentence']
required_columns_theme =['Column_5','Theme_Key']
required_columns_sku =['SKU','SKU_Key']


Sentence_table = add_surrogate_key(Sentence_table, 'Sentence_Key')
Subtheme_table = add_surrogate_key(Subtheme_table, 'Theme_Key')
SKU_table = add_surrogate_key(SKU_table, 'SKU_Key')

merged_fact_table = pd.merge(df,Sentence_table[required_columns_sentence], on='Sentence', how='left')

merged_fact_table = pd.merge(merged_fact_table,Subtheme_table[required_columns_theme], on='Column_5', how='left')

merged_fact_table = pd.merge(merged_fact_table,SKU_table[required_columns_sku], on='SKU', how='left')

columns_to_remove=['Column_1','Sentence','Column_5','Column_4','Column_2','Column_3','Column_6','Column_7','SKU']

merged_fact_table=merged_fact_table.drop(columns=columns_to_remove)
merged_fact_table=merged_fact_table.drop_duplicates()



Sentence_table.to_csv("ADD PATH", index=False)
Subtheme_table.to_csv("ADD PATH", index=False)
SKU_table.to_csv("ADD PATH", index=False)
merged_fact_table.to_csv("ADD PATH", index=False)


