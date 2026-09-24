import asyncio
from playwright.async_api import async_playwright

website = "https://images.google.com/"
img = input('img : ')

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(permissions=[])
        page = await context.new_page()
        
        print("[+] Loading Google Images...")
        await page.goto(website, wait_until="domcontentloaded", timeout=60000)
        
        await page.locator(".hWdRGb").click() # localizador de icono de camara
        await page.wait_for_timeout(2000)
       
        print('[+] Uploading image...')
        
        # Corregida la indentación (debe estar dentro de main y del contexto del navegador)
        async with page.expect_file_chooser() as fc_info:
            await page.locator(".DV7the").click()
            
        file_chooser = await fc_info.value
        await file_chooser.set_files(img)
        
        await page.wait_for_timeout(10000)

asyncio.run(main())