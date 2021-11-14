import pymysql

db = pymysql.connect(host='localhost',user='root', passwd='', db='shopee')
cursor = db.cursor()

def GetAllProduct():
    try:
        sql="SELECT * FROM `product` WHERE 1"
        cursor.execute(sql)
        results = cursor.fetchall()
        listdic={"ID":[],"Name":[],"AvgPrice":[],"SoldedNum":[]}
        for row in results:
            listdic["ID"].append(row[1])
            listdic["Name"].append(row[2])
            listdic["AvgPrice"].append(row[3])
            listdic["SoldedNum"].append(row[4])
        return listdic
    except:
        import traceback
        traceback.print_exc()
        print ("Error: unable to fetch data")
    db.close()

#新增商品
def addproduct(id,name,price,soldednum):
    try:
        sql="INSERT INTO `product`(`ProductId`, `Name`, `AvgPrice`, `SoldedNum`) VALUES (%s, %s, %s, %s)"
        val=(id,name,price,soldednum)
        cursor.execute(sql,val)
        db.commit()
        return
    except:
        import traceback
        traceback.print_exc()
        print ("Error: unable to fetch data")
    db.close()

