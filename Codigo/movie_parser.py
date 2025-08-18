import time
from browserManager import BrowserManager
from selenium.webdriver.common.by import By

class MovieParser:
    """Responsável por extrair dados de uma página de filme no IMDb."""
    def __init__(self, browser: BrowserManager):
        self.browser = browser
        self.driver = browser.driver

    def parse(self, link: str) -> dict:
        self.driver.get(link)
        time.sleep(1)

        return {
            "Título": self.safe_get_text("//h1"),
            "Ano": self.safe_get_text("//a[contains(@href, 'releaseinfo')]"),
            "Nota IMDb": self.safe_get_text("//div[@data-testid='hero-rating-bar__aggregate-rating__score']/span").replace(",", "."),
            "Link": link,
            "Gêneros": ", ".join(self.safe_get_all("//div[@data-testid='genres']//a")),
            "Sinopse": self.safe_get_text("//span[@data-testid='plot-xl']"),
            "Elenco Principal": ", ".join(self.safe_get_all("//a[@data-testid='title-cast-item__actor']")[:3])
        }

    def safe_get_text(self, xpath: str) -> str:
        try:
            return self.browser.wait_for(By.XPATH, xpath).text
        except:
            return "N/A"

    def safe_get_all(self, xpath: str) -> list:
        try:
            return [el.text for el in self.browser.wait_for_all(By.XPATH, xpath)]
        except:
            return ["N/A"]

