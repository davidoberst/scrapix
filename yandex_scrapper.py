#Playwright abre Yandex Images
#Sube tu imagen (input file)
#Espera a que cargue resultados
#Extrae: urls, thumbnails, dominios de origen

import pyfiglet
import asyncio
from playwright.async_api import async_playwright
website = "https://yandex.com/images"
print(pyfiglet.figlet_format(text="      scrapix",font='smblock'),end="")
print("by: https://github.com/davidoberst",end="")
print("\n" + "-"*35)
img = input('[+] Image path : ')
async def main():
    async with async_playwright() as p:
        # Lanza el navegador en modo headless (por defecto es True)
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        # navegar url
        await page.goto(website) # page = pagina a navegar, variable del inicio jeje
        
        # Selecciona el botón usando la clase principal que sale en la pagina al entrar en herramientas de desarrollador
        camera_button = page.locator(".HeaderDesktopActions-CbirButton")

        await boton_camara.click() #clickear boton de camara

        input_file = page.locator('input[type="file"]') #variable que localiza el input de subida de archivos

        await input_file.set_input_files(img) #subir imagen

        await browser.close()

asyncio.run(main())