from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook
import lucky_gunner

wb = Workbook()
ws = wb.active
ws.title = 'data'
fieldnames = ['Company', 'Product', 'Caliber', 'Price-Per-Round', 'Cost', 'Inventory', 'Link']
ws.append(fieldnames)

# Lucky Gunner / 6.5 Creedmoor
lucky_gunner.lucky_gunn(ws, BeautifulSoup, requests)

wb.save('ammo.xlsx')





