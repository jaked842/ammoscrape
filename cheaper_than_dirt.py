
def cheaper_than_dirt(ws, BeautifulSoup, requests):
    sources = {
        '6.5 Creedmoor': 'https://www.cheaperthandirt.com/6.5mm-creedmoor/ammunition/rifle-ammo/?type=caliber&brandparam=6.5mmCreedmoor&srule=price-low-to-high',
        '9mm': 'https://www.cheaperthandirt.com/ammunition/handgun-ammo/9mm-luger-or-9x19mm/?srule=cost-per-round-low-to-high',
        '223': 'https://www.cheaperthandirt.com/ammunition/rifle-ammo/.223-remington-and-5.56-nato/?srule=cost-per-round-low-to-high',
        '450 Bushmaster': 'https://www.cheaperthandirt.com/ammunition/rifle-ammo/.450-bushmaster/?srule=price-low-to-high', 
        '38-special': 'https://www.cheaperthandirt.com/ammunition/handgun-ammo/.38-special/?srule=price-low-to-high',
        '380': 'https://www.cheaperthandirt.com/ammunition/handgun-ammo/.380-acp-or-.380-auto/'
    }

    for caliber in sources :
        source = requests.get(sources[caliber]).text
        soup = BeautifulSoup(source, 'lxml')
        products_container = soup.find('div', class_='product-grid')
        products_div = products_container.find_all('div', class_='product-impression')

        for iteration, product in enumerate(products_div):
            if iteration > 4:
                break
            else:
                product_name = product.find('span', class_='d-lg-none').text
                display_cost = product.find('span', class_='value').attrs['content']

            ws.append({
                'A': 'CheaperThanDirt',
                'B': product_name,
                'C': caliber,
                'E': display_cost,
                'G': sources[caliber]
                })
