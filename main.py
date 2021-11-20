import json
import getinfo
import time

game = input("game:\n")
goods_id = input("goods_id:\n")
goods_name = input("goods_name:\n")
SleepTime = int(input("SleepTime:\n"))
cookie = input("cookie:\n")
file = open("HistoryPrice.txt", 'a')

if game == "":
    game = "csgo"

a=0
while a!=10:
    a+=1
    InfoJson = getinfo.getinfo(game, goods_id)
    NumJson = getinfo.getnum(game, goods_name, cookie)

    num = json.loads(NumJson)
    info = json.loads(InfoJson)
    print(num)

    info_data = info['data']
    info_items = info_data['items']
    info_item = info_items[0]
    info_price = info_item['price']

    num_data = num['data']
    num_items = num_data['items']
    num_item = num_items[0]
    sell_num = num_item['sell_num']

    ticks = time.strftime('%Y年%m月%d日%H:%M:%S', time.localtime())

    file.write("%s %s %s\n" % (ticks, info_price, sell_num))
    print("%s %s %s" % (ticks, info_price, sell_num))
    file.flush()
    print("Done.")

    time.sleep(SleepTime)