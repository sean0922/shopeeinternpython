from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import json
import coculation
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    
    totalsalesprice=str(coculation.totalsalesprice())
    totalsalesnub=str(coculation.totalsalenum()) 
    avgproductprice=str(coculation.avgsalesprice())
    medianprice=str(coculation.medianprice())
    maxprice=str(coculation.maxprice())
    minprice=str(coculation.minprice())  

    content = {
    'totalsalesprice':totalsalesprice,   #銷售總額
    'totalsalesnub':totalsalesnub,     #總銷售商品數
    'avgproductprice':avgproductprice,   #平均一件商品賣價   
    'medianprice':medianprice,       #商品價錢的中位數
    'maxprice':maxprice,          #最高商品價錢
    'minprice':minprice           #最低商品價錢
    }
    return content




if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3000,debug=True)