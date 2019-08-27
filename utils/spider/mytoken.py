import requests
import time
import json
from config import THREAD, DEFAULT_PAGE, DATA_JSON_SAVE, logger
from concurrent.futures import ThreadPoolExecutor, as_completed
from wxBotServer.settings import BASE_DIR


def _replace(s):
    return s.replace(",", "").replace("$", "")


def mytoken(page=1):
    r = requests.get("https://api.mytokenapi.com/ticker/currencylist?page={page}&size=200&subject=market_cap"
                     "&timestamp=1564197170939&code=c7de403d93d8c627ed4c2787faa34edd"
                     "&platform=web_pc&v=1.0.0&language=zh_CN&legal_currency=USD".format(page=page))
    rets = r.json().get("data").get("list")
    ret = {}

    for r in rets:
        name = r.get("currency", None)
        fullname = r.get("alias", None)
        current_price = r.get("price_display", None)
        change_percent = r.get("percent_change_display", None)
        market_value = r.get("market_cap_display", None)
        vol = r.get("volume_24h", None)
        t = time.strftime("%Y-%m-%d %H:%M:%S")

        # 去掉 $ 符号 和,
        market_value = _replace(str(market_value))
        vol = _replace(str(vol))

        ret[name] = {
            "_name": name,
            "_full": fullname,
            "fullname": "{}({})".format(name, fullname),
            "current_price": current_price,
            "change_percent": change_percent,
            "market_value": market_value,
            "vol": vol,
            "t": t
        }
    return ret


def worker():
    logger.info(msg="worker start")
    executor = ThreadPoolExecutor(max_workers=THREAD)
    tasks = []
    save = {}

    for p in range(1, DEFAULT_PAGE+1):
        tasks.append(executor.submit(mytoken, (p)))

    for f in as_completed(tasks):
        r = f.result()

        if r:
            save = dict(r, **save)

    with open(BASE_DIR + "/" + DATA_JSON_SAVE, 'w') as f:
        json.dump(save, f, indent=4)
    logger.info("worker end")


# worker()
