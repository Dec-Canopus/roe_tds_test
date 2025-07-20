import asyncio
from playwright.async_api import async_playwright

async def scrape_and_sum():
    total = 0

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        for seed in range(62, 72):  # Scraping from seed 62 to seed 71
            url = f"https://sanand0.github.io/tdsdata/js_table/?seed={seed}"
            await page.goto(url)
            await page.wait_for_selector("table")

            # Extracting the text from the table and parsing the numbers
            table_text = await page.inner_text("table")
            numbers = [int(x) for x in table_text.replace('\n', '\t').split('\t') if x.strip().isdigit()]

            seed_sum = sum(numbers)
            print(f"Seed {seed}: sum = {seed_sum}")
            total += seed_sum

        await browser.close()
        print(f"\nTotal sum across seeds 62–71: {total}")

# 🟢 Run the async function directly in Colab
if __name__ == "__main__":
    asyncio.run(scrape_and_sum())
