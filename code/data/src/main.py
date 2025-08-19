from utils.data_exporter import DataExporter
from scraping.browser_manager import BrowserManager
from scraping.imdb_scraper import IMDBScraper
from scraping.movie_parser import MovieParser

def main():
    browser = BrowserManager(wait_time=20)

    try:
        parser = MovieParser(browser)
        
        scraper = IMDBScraper(browser, parser)
        
        filmes = scraper.scrape_top_movies(limit=10)
        
        DataExporter.to_csv(filmes, filename="top_movies_imdb.csv")
    finally:
        browser.quit()

if __name__ == "__main__":
    main()