import pandas as pd

data = pd.read_csv("top_movies_imdb.csv")
df = pd.DataFrame(data)

df.rename(columns={
    'Título': 'Title',
    'Ano': 'Year',
    'Nota IMDb': 'IMDb Rating',  
    'Gêneros': 'Genres',        
    'Sinopse': 'Synopsis',  
    'Elenco Principal': 'Main Cast'  
}, inplace=True)

df_sorted = df.sort_values(by=['Title', 'Year'], ascending=[True, False],  key=lambda x: x.str.lower() if x.name == 'Title' else x).reset_index(drop=True)

df_processed = df.replace('N/A', '-').fillna('-')

output_filename = "processed_data.xlsx"

df_processed.to_excel(output_filename, index=False)

print(f"File saved as '{output_filename}'!")