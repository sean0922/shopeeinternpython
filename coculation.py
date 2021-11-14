import sql
import pandas as pd
def totalsalesprice():
    result=sql.GetAllProduct()
    totalnum=0
    for i in range(len(result['ID'])):
        totalnum=totalnum+(int(result['AvgPrice'][i])*int(result['SoldedNum'][i]))
    #print(totalnum)
    return totalnum

def totalsalenum():
    result=sql.GetAllProduct()
    totalnum=0
    for i in range(len(result['ID'])):
        totalnum=totalnum+int(result['SoldedNum'][i])
    #print(totalnum)
    return totalnum


def avgsalesprice():
    result=sql.GetAllProduct()
    totalprice=0
    totalnum=0
    for i in range(len(result['ID'])):
        totalprice=totalprice+(int(result['AvgPrice'][i])*int(result['SoldedNum'][i]))
        totalnum=totalnum+int(result['SoldedNum'][i])
    avgprice=totalprice/totalnum
    #print(avgprice)
    return avgprice


def medianprice():
    result=sql.GetAllProduct()
    arr=[]
    for i in range(len(result['ID'])):
        arr.append(int(result['AvgPrice'][i])) 
    data=pd.Series(arr)
    median=data.median()
    #print(median)
    return median


def maxprice():
    result=sql.GetAllProduct()
    arr=[]
    for i in range(len(result['ID'])):
        arr.append(int(result['AvgPrice'][i])) 
    data=pd.Series(arr)
    max=data.max()
    #print(max)
    return max

def minprice():
    result=sql.GetAllProduct()
    arr=[]
    for i in range(len(result['ID'])):
        arr.append(int(result['AvgPrice'][i])) 
    data=pd.Series(arr)
    min=data.min()
    #print(min)
    return min
