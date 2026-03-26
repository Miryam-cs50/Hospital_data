import requests
import csv
import os
from datetime import datetime

API_URL = "https://services9.arcgis.com/h6mZqZEHZgE1ZmLI/arcgis/rest/services/Waiting_List/FeatureServer/0/query?f=json&cacheHint=true&resultOffset=0&resultRecordCount=25&where=1%3D1&orderByFields=&outFields=*&resultType=standard&returnGeometry=false&spatialRel=esriSpatialRelIntersects"
CSV_FILE = "hospital_waiting_data.csv"
FIELD_HOSPITAL = "Name"  
FIELD_WAITING = "Waiting_List"      
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

def init_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            writer.writerow(['時間', '醫院名稱', '輪候人數'])

def fetch_and_save():
    try:
        resp = requests.get(API_URL, headers=headers, timeout=15)
        data = resp.json()
        now_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        records = []
        
        for feature in data.get('features', []):
            attrs = feature.get('attributes', {})
            hospital = attrs.get(FIELD_HOSPITAL, '未知醫院')
            waiting = attrs.get(FIELD_WAITING, 'N/A')
            records.append([now_str, hospital, waiting])
        
        with open(CSV_FILE, 'a', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            writer.writerows(records)
        print(f"✓ {now_str} 成功記錄 {len(records)} 條數據")
    except Exception as e:
        print(f"✗ 錯誤: {e}")

if __name__ == "__main__":
    init_csv()
    fetch_and_save()
