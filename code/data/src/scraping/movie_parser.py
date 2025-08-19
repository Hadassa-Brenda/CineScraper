import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .browser_manager import BrowserManager 

class MovieParser:
    def __init__(self, browser: BrowserManager):
        self.browser = browser
        self.driver = browser.driver

    def parse(self) -> dict:
        time.sleep(2)
        
        return {
            "Título": self.safe_get_text("//h1"),
            "Ano": self.safe_get_text("//a[contains(@href, 'releaseinfo')]"),
            "Nota IMDb": self.safe_get_rating(),
            "Link": self.driver.current_url,
            "Gêneros": self.safe_get_genres(),
            "Sinopse": self.safe_get_text("//span[@data-testid='plot-xl']"),
            "Elenco Principal": self.safe_get_cast()
        }

    def safe_get_text(self, xpath: str) -> str:
        try:
            element = self.browser.wait.until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            return element.text.strip() if element.text else "N/A"
        except:
            return "N/A"

    def safe_get_rating(self) -> str:
        try:
            rating_text = self.safe_get_text("//div[@data-testid='hero-rating-bar__aggregate-rating__score']/span")
            return rating_text.replace(",", ".") if rating_text != "N/A" else "N/A"
        except:
            return "N/A"

    def safe_get_genres(self) -> str:
        try:
            genres_elements = self.driver.find_elements(By.XPATH, "//div[@data-testid='genres']//a")
            genres = [genre.text for genre in genres_elements if genre.text]
            return ", ".join(genres) if genres else "N/A"
        except:
            return "N/A"

    def safe_get_cast(self) -> str:
        try:
            cast_elements = self.driver.find_elements(By.XPATH, "//a[@data-testid='title-cast-item__actor']")[:3]
            cast = [actor.text for actor in cast_elements if actor.text]
            return ", ".join(cast) if cast else "N/A"
        except:
            return "N/A"