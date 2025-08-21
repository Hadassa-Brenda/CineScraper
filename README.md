# CineScraper

## Projeto
**Análise dos Top 250 Filmes do IMDb**

## Descrição
Este projeto realiza uma análise dos Top 250 filmes do IMDb, explorando informações como:  

- Notas  
- Gêneros  
- Sinopse 
- Outras métricas relevantes  

O projeto inclui:  

- Scripts em Python para coleta de dados do IMDb  
- Processamento e limpeza dos dados para análise  
- xlsx final pronto para importação no Power BI, permitindo a criação de dashboards interativos  

## Arquitetura do projeto
Estrutura modular do projeto:

```text
src/
├─ processing/           # Scripts para processamento e limpeza de dados
│  └─ cleaning_data.py
├─ scraping/             # Scripts para raspagem de dados do IMDb
│  ├─ browser_manager.py
│  ├─ imdb_scraper.py
│  └─ movie_parser.py
├─ utils/                # Funções utilitárias usadas em todo o projeto
├─ main.py               # Script principal que orquestra o processo
└─ .gitignore
```
## Ferramentas e bibliotecas utilizadas
- **Python** – linguagem principal do projeto  
- **Selenium** – automação de navegação e coleta de dados do IMDb  
- **Pandas** – manipulação e análise de dados  
- **CSV** – formato final para exportação de dados e importação no Power BI  

## Dashboard Interativo

O dashboard do CineScraper foi criado no Power BI.  

**Baixar arquivo PBIX:**  
[Download do Dashboard](https://app.powerbi.com/onedrive/open?pbi_source=ODSPViewer&driveId=b!K5ZHvIC9UkyFxm4xkHuT_D29WDYGKc9ItkPAf2trjMoveWp_mzeBSKQ_SxgSGA82&itemId=01E7CKJR46Z4HJQIEGIRA2WAWLF64EPOJ4)

**Imagem Estática:**
<img width="1123" height="593" alt="image" src="https://github.com/user-attachments/assets/4f2948af-de4b-4c32-91a6-0cdfb6df741d" />

