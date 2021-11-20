import jsonparse
import getinfo
import time

game = input("game:\n")
goods_id = input("goods_id:\n")
SleepTime = int(input("SleepTime:\n"))
file = open("HistoryPrice.txt", 'a')

if game == "":
    game = "csgo"

while True:
    json = getinfo.getinfo(game, goods_id)
    info = jsonparse.jsonparse(json)

    data = info['data']
    items = data['items']
    item = items[0]
    price = item['price']

    ticks = time.strftime('%Y年%m月%d日%H:%M:%S', time.localtime())

    file.write("%s %s\n" % (ticks, price))
    file.flush()
    print("%s %s" % (ticks, price))
    print("Done.")

    time.sleep(SleepTime)
