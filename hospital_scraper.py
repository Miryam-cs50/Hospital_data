{\rtf1\ansi\ansicpg1252\cocoartf2821
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import requests\
import csv\
import os\
from datetime import datetime\
\
API_URL = "https://services9.arcgis.com/h6mZqZEHZgE1ZmLI/arcgis/rest/services/Waiting_List/FeatureServer/0/query?f=json&cacheHint=true&resultOffset=0&resultRecordCount=25&where=1%3D1&orderByFields=&outFields=*&resultType=standard&returnGeometry=false&spatialRel=esriSpatialRelIntersects"\
CSV_FILE = "hospital_waiting_data.csv"\
FIELD_HOSPITAL = "Name"  \
FIELD_WAITING = "Waiting_List"      \
headers = \{'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'\}\
\
def init_csv():\
    if not os.path.exists(CSV_FILE):\
        with open(CSV_FILE, 'w', newline='', encoding='utf-8-sig') as f:\
            writer = csv.writer(f)\
            writer.writerow(['\uc0\u26178 \u38291 ', '\u37291 \u38498 \u21517 \u31281 ', '\u36650 \u20505 \u20154 \u25976 '])\
\
def fetch_and_save():\
    try:\
        resp = requests.get(API_URL, headers=headers, timeout=15)\
        data = resp.json()\
        now_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')\
        records = []\
        \
        for feature in data.get('features', []):\
            attrs = feature.get('attributes', \{\})\
            hospital = attrs.get(FIELD_HOSPITAL, '\uc0\u26410 \u30693 \u37291 \u38498 ')\
            waiting = attrs.get(FIELD_WAITING, 'N/A')\
            records.append([now_str, hospital, waiting])\
        \
        with open(CSV_FILE, 'a', newline='', encoding='utf-8-sig') as f:\
            writer = csv.writer(f)\
            writer.writerows(records)\
        print(f"\uc0\u10003  \{now_str\} \u25104 \u21151 \u35352 \u37636  \{len(records)\} \u26781 \u25976 \u25818 ")\
    except Exception as e:\
        print(f"\uc0\u10007  \u37679 \u35492 : \{e\}")\
\
if __name__ == "__main__":\
    init_csv()\
    fetch_and_save() # \uc0\u21482 \u22519 \u34892 \u19968 \u27425 \u23601 \u32080 \u26463 }