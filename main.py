import json
import getinfo
import csv
import time

game = input("game:\n")
goods_id = input("goods_id:\n")
SleepTime = int(input("SleepTime:\n"))
cookie = input("cookie:\n")
file = open("HistoryPrice.txt", 'a')
csvfile = open('HistoryPrice.csv', 'a', newline='')
csv_writer = csv.writer(csvfile)

if game == "":
    game = "csgo"

while True:
    InfoJson = getinfo.getinfo(game, goods_id)
    info = json.loads(InfoJson)

    info_data = info['data']
    info_items = info_data['items']
    info_item = info_items[0]
    info_price = info_item['price']
    goods_infos = info_data['goods_infos']
    goods_info = goods_infos[goods_id]
    goods_name = goods_info['name']

    NumJson = getinfo.getnum(game, goods_name, cookie)
    num = json.loads(NumJson)

    num_data = num['data']
    num_items = num_data['items']
    num_item = num_items[0]
    sell_num = num_item['sell_num']

    num_data = num['data']
    num_items = num_data['items']
    num_item = num_items[0]
    sell_num = num_item['sell_num']

    ticks = time.strftime('%Y年%m月%d日%H:%M:%S', time.localtime())

    file.write("%s %s %s\n" % (ticks, info_price, sell_num))
    csv_writer.writerow([ticks, info_price, sell_num])
    print("%s %s %s" % (ticks, info_price, sell_num))
    file.flush()
    csvfile.flush()
    print("Done.")

    time.sleep(SleepTime)