
def freedom_munition(ws, BeautifulSoup, requests):

    sources = {
        '6.5 Creedmoor': 'https://www.freedommunitions.com/ammunition/rifle.html?hmt_caliber=5768', 
        '9mm':'https://www.freedommunitions.com/ammunition/pistol/9mm.html',
        '223':'https://www.freedommunitions.com/ammunition/rifle/223-remington.html',
        '450 Bushmaster':'https://www.freedommunitions.com/ammunition/rifle/223-remington.html',
        '38-special':'https://www.freedommunitions.com/ammunition/pistol/38-special.html',
        '380': 'https://www.freedommunitions.com/ammunition/pistol/380-auto.html'
    }

    for caliber in sources:
        source = requests.get(sources[caliber]).text
        soup = BeautifulSoup(source, 'lxml')
        products_container = soup.find('div', class_='products-grid')
        products_li = products_container.find_all('li', class_='product-item')

        for iteration, product in enumerate(products_li):
            if iteration > 4:
                break
            else: 
                product_name = product.find('strong', class_='product-item-name').a.text
                display_cost = product.find('span', class_='price').text
            
            ws.append(
                {
                    'A': 'Freedom Munitions',
                    'B': product_name,
                    'C': caliber,
                    'E': display_cost,
                    'G': sources[caliber]
                })
