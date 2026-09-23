#Playwright abre Yandex Images
#Sube tu imagen usando el evento del botón Select File
#Espera a que cargue resultados

import pyfiglet
import asyncio
from playwright.async_api import async_playwright

website = "https://yandex.com/images"
print(pyfiglet.figlet_format(text="      scrapix", font='smblock'), end="")
print("by: https://github.com/davidoberst", end="")
print("\n" + "-"*35)
img = input('[+] Image path : ')

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(permissions=[])
        page = await context.new_page()
        
        print("[+] Loading Yandex...")
        await page.goto(website, wait_until="domcontentloaded", timeout=60000) #evitar bloqueos 
        
        # 1. Abrir modal de la cámara
        await page.locator(".HeaderDesktopActions-CbirButton").click()

        # 2. Capturar el evento del selector de archivos al presionar Select file
       
        print("[+] Sending image to Yandex...")
        async with page.expect_file_chooser() as fc_info:
            await page.locator(".CbirPanel-FileControlsButton").click()
            
        file_chooser = await fc_info.value
        await file_chooser.set_files(img)
        print("[+] Image sended.")

        # 3. Esperar a que la página procese y muestre los resultados
        print("[+] Aaiting results from Yandex...")
        await page.wait_for_selector(".CbirItem, .cbir-section, .CbirSites", timeout=30000)
        print("[+] ¡Resultados cargados con éxito!")

        print("[+] Proceso completado. Esperando 10 segundos antes de cerrar...")
        await page.wait_for_timeout(10000)

        await browser.close()

asyncio.run(main())