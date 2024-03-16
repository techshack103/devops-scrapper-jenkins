# from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright, Playwright
from bs4 import BeautifulSoup

async def get_dynamic_soup(url: str) -> BeautifulSoup:
    async with async_playwright() as playwright:
        chromium = playwright.chromium
        browser = await chromium.launch()
        page = await browser.new_page()
        await page.goto(url)
        await page.wait_for_load_state("networkidle")
        content = await page.content()
        await browser.close()
        return BeautifulSoup(content, "html.parser")

async def scrape_dev_to_search_results(search_query: str, limit: int = 30) -> list:
    url = f"https://dev.to/search?q={search_query}"
    soup = await get_dynamic_soup(url)

    article_list_element = soup.find("div", "articles-list")
    article_substories_element = article_list_element.find("div", "substories search-results-loaded")
    article_substories_list = article_substories_element.find_all("article")

    results = []
    for i,article in enumerate(article_substories_list,start=1):
        if i >= limit:
            break
        data = {}
        data["article_title"] = article.find("a").text.strip()
        article_link_text = article.find("a")["href"]
        data["article_dev_to_link"] = "https://dev.to" + article_link_text
        results.append(data)

    return results


