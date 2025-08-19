from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .browser_manager import BrowserManager
from .movie_parser import MovieParser


class IMDBScraper:
    def __init__(self, browser: BrowserManager, parser: MovieParser):
        self.browser = browser
        self.parser = parser
        self.driver = browser.driver
        self.filmes = []

    def accept_cookies(self):
        try:
            button = self.browser.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Accept all')]"))
            )
            button.click()
        except Exception:
            pass

    def scrape_top_movies(self, limit: None):
        self.browser.open("https://www.imdb.com/chart/top/")
        self.accept_cookies()

        movies_elements = self.driver.find_elements(By.CSS_SELECTOR, ".ipc-metadata-list-summary-item")

        for index, items in enumerate(movies_elements[:limit], 1):
            try:
                link = items.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
                print(f"\nProcessing {index}: {link}")

                movie_data = self.parser.parse(link)
                self.filmes.append(movie_data)

                print(f"Coletado: {movie_data.get('Título')} ({movie_data.get('Ano')}) - Nota: {movie_data.get('Nota IMDb')}")
            except Exception as e:
                print(f"Error to processing movies {index}: {e}")

        return self.filmes
