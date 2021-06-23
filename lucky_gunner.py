
def lucky_gunn(ws, BeautifulSoup, requests):
    sources = [
        'https://www.luckygunner.com/rifle/6.5mm-creedmoor-ammo',
        'https://www.luckygunner.com/handgun/9mm-ammo',
        'https://www.luckygunner.com/rifle/223-remington-ammo',
        'https://www.luckygunner.com/rifle/450-bushmaster-ammo',
        'https://www.luckygunner.com/rifle/30-30-ammo',
        'https://www.luckygunner.com/handgun/38-special-ammo',
        'https://www.luckygunner.com/handgun/380-auto-ammo',
        ]

    calibers = ['6.5 Creedmoor', '9mm', '223', '450 Bushmaster', '30-30', '38-special', '380']

    for it, src in enumerate(sources):
        source = requests.get(src).text
        soup = BeautifulSoup(source, 'lxml')
        products_container = soup.find(class_='products-list')
        products_li = products_container.find_all('li', class_='item')

        for iteration, product in enumerate(products_li):
            if iteration > 4:
                break
            product_name = product.find('h3', class_='product-name').span.text
            price_per_rnd = product.find('p', class_='cprc').text
            stock_qty = product.find('span', class_='stock-qty').text
            cost = product.find('span', class_='regular-price')
            special_cost = product.find('span', class_='price')
            display_cost = ''

            if special_cost:
                display_cost = special_cost.text.strip()
            else:
                display_cost = cost.text.strip() 

            ws.append(
                {
                    'A': 'Lucky Gunner',
                    'B': product_name, 
                    'C': calibers[it], 
                    'D': price_per_rnd,
                    'E': display_cost,
                    'F': stock_qty,
                    'G': src
                })


        #print(product_name, price_per_rnd, stock_qty, cost)



    