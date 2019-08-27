import schedule
import requests
import time
import json
from config import THREAD, DEFAULT_PAGE, DATA_JSON_SAVE, logger
from concurrent.futures import ThreadPoolExecutor, as_completed


def feixiaohao(page=1):
    ret = {}
    target = "https://dncapi.bqiapp.com/api/coin/web-coinrank?page={}&type=-1&pagesize=100&webp=1".format(page)
    r = requests.get(target)

    for i in r.json()["data"]:
        name = i.get("name", None)
        fullname = i.get("fullname", None)
        current_price = i.get("current_price", None)
        change_percent = i.get("change_percent", None)
        market_value = i.get("market_value", None)
        vol = i.get("vol", None)
        t = time.strftime("%Y-%m-%d %H:%M:%S")

        ret[name] = {
            "_name": name,
            "_full": fullname,
            "fullname": "{}({})".format(name, fullname),
            "current_price": current_price,
            "change_percent": change_percent,
            "market_value": market_value,
            "vol": vol,
            "t": t,
            "page": page
        }
    return ret


def worker():
    logger.info(msg="worker start")
    executor = ThreadPoolExecutor(max_workers=THREAD)
    tasks = []
    save = {}

    for p in range(1, DEFAULT_PAGE+1):
        tasks.append(executor.submit(feixiaohao, (p)))

    for f in as_completed(tasks):
        r = f.result()
        save = dict(r, **save)

    with open(DATA_JSON_SAVE, 'w') as f:
        json.dump(save, f, indent=4)
    logger.info("worker end")
