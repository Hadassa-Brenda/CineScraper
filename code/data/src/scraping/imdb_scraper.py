from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .browser_manager import BrowserManager
from .movie_parser import MovieParser

class IMDBScraper:
    def __init__(self, browser: BrowserManager, parser: MovieParser):
        self.browser = browser
        self.parser = parser
        self.driver = browser.driver
        self.movies = []
        self.main_window = None

    def accept_cookies(self):
        try:
            button = self.browser.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Accept all')]"))
            )
            button.click()
            print("Cookies accepted")
        except Exception:
            print("Cookie button not found or already accepted")
            pass

    def scrape_top_movies(self, limit: None):
        self.browser.open("https://www.imdb.com/chart/top/")
        self.accept_cookies()
        
        self.main_window = self.driver.current_window_handle
        
        self.browser.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".ipc-metadata-list-summary-item"))
        )
        
        movies_elements = self.driver.find_elements(By.CSS_SELECTOR, ".ipc-metadata-list-summary-item")
        print(f"Found {len(movies_elements)} movie elements")

        for i, element in enumerate(movies_elements[:limit], 1):
            try:
                link = element.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
                print(f"\nProcessing movie {i}: {link}")

                self.driver.execute_script("window.open('');")
                self.driver.switch_to.window(self.driver.window_handles[1])
                self.driver.get(link)
                
                movie_data = self.parser.parse()
                self.movies.append(movie_data)

                print(f"Collected: {movie_data.get('Título')} ({movie_data.get('Ano')}) - Rating: {movie_data.get('Nota IMDb')}")
                
                self.driver.close()
                self.driver.switch_to.window(self.main_window)
                
            except Exception as e:
                print(f"Error processing movie {i}: {e}")
                if len(self.driver.window_handles) > 1:
                    self.driver.close()
                self.driver.switch_to.window(self.main_window)

        return self.movies