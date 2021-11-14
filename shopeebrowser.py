import requests
import urllib
import sql
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.68'
}
s = requests.Session()
for totalpage in range(100):
    url = 'https://shopee.tw/api/v4/search/search_items?by=pop&limit=30&match_id=106973794&newest='+str(30*totalpage)+'&order=desc&page_type=shop&scenario=PAGE_OTHERS&version=2' 

    r = s.get(url, headers=headers)

    if r.status_code == requests.codes.ok:
        data = r.json()
        item=data['items']
        for i in range(int(len(item))):
            item=data['items'][i]
            itembasic=item['item_basic']
            itemid=itembasic['itemid']
            itemname=itembasic['name']
            itemprice=(itembasic['price_min']+itembasic['price_max'])/200000
            itemsolded=itembasic['historical_sold']
            #print(itemid,itemname,itemprice,itemsolded)
            sql.addproduct(itemid,itemname,itemprice,itemsolded)


