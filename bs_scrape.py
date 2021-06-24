from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook
import lucky_gunner, freedom_munitions, cheaper_than_dirt
import os

wb = Workbook()
ws = wb.active
ws.title = 'data'
fieldnames = ['Company', 'Product', 'Caliber', 'Price-Per-Round', 'Cost', 'Inventory', 'Link']
ws.append(fieldnames)

# Lucky Gunner / 6.5 Creedmoor
lucky_gunner.lucky_gunn(ws, BeautifulSoup, requests)
freedom_munitions.freedom_munition(ws, BeautifulSoup, requests)
cheaper_than_dirt.cheaper_than_dirt(ws, BeautifulSoup, requests)

cwd = os.getcwd()
wb.save(f'{cwd}/Desktop/ammo.xlsx')
#wb.save('../../Desktop/ammo.xlsx')

