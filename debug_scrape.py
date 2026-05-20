#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
اسکریپت دیباگ برای بررسی ساختار HTML از tgju.org
"""

import requests
from bs4 import BeautifulSoup

url = "https://www.tgju.org/profile/price_dollar_rl/history"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    print(f"درحال درخواست از: {url}")
    response = requests.get(url, headers=headers, timeout=30)
    print(f"Status Code: {response.status_code}")
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # پیدا کردن تمام جداول
    tables = soup.find_all('table')
    print(f"\nتعداد جداول پیدا شده: {len(tables)}")
    
    for i, table in enumerate(tables):
        print(f"\n--- جدول {i+1} ---")
        print(f"Class: {table.get('class')}")
        print(f"ID: {table.get('id')}")
        
        tbody = table.find('tbody')
        if tbody:
            rows = tbody.find_all('tr')
            print(f"تعداد ردیف‌ها در tbody: {len(rows)}")
            
            if rows:
                print(f"\nاولین ردیف:")
                first_row = rows[0]
                cells = first_row.find_all('td')
                print(f"تعداد ستون‌ها: {len(cells)}")
                
                for j, cell in enumerate(cells[:10]):  # نمایش اولین 10 ستون
                    print(f"  ستون {j}: {cell.get_text(strip=True)[:100]}")
        else:
            print("tbody پیدا نشد")
    
    # بررسی محتوای کل (اولین 2000 کاراکتر)
    print("\n--- بخشی از کد HTML ---")
    print(response.text[:2000])
    
except Exception as e:
    print(f"خطا: {e}")
    import traceback
    traceback.print_exc()
