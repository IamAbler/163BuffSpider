import urllib.request


def getinfo(game, goods_id):
    get = urllib.request.urlopen(
        "https://buff.163.com/api/market/goods/sell_order?game=%s&goods_id=%s" % (game, goods_id))
    return get.read().decode('utf-8')
