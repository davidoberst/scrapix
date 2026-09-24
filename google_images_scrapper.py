
import asyncio
from playwright.async_api import async_playwright


website = "https://images.google.com/"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(permissions=[])
        page = await context.new_page()
        
        print("[+] Loading Google Images...")
        await page.goto(website, wait_until="domcontentloaded", timeout=60000) #evitar bloqueos 
        await page.locator(".hWdRGb").click()
        await page.wait_for_timeout(10000)

        await browser.close()

asyncio.run(main())
        