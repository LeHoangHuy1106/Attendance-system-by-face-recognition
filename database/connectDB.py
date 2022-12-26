import sqlite3


def getData(query):
    conn = sqlite3.connect('DBDiemDanh.db')
    cursor = conn.execute(query)
    profile = None
    listData=[]
    for row in cursor:
        profile = row
        listData.append(profile)
    conn.close()
    return listData

def setData(query):
    conn = sqlite3.connect('DBDiemDanh.db')
    conn.execute(query)
    conn.commit()
    conn.close()

