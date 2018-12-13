name = "opap"

import requests, json
from pprint import pprint
url = "https://api.opap.gr/"

#==========================================================================

def get_draw_id(game):
    if game == "super3":
        return "2100"
    elif game == "extra5":
        return "5106"
    elif game == "proto":
        return "2101"
    elif game == "lotto":
        return "5103"
    elif game == "kino":
        return "1100"
    elif game == "joker":
        return "5104"
    else:
        exc = DrawNameException("get_last_draw(name)", "Wrong draw name.")
        raise exc

def get_draw_id_ex_k(game):
    if game == "super3":
        return "2100"
    elif game == "extra5":
        return "5106"
    elif game == "proto":
        return "2101"
    elif game == "lotto":
        return "5103"
    elif game == "joker":
        return "5104"
    else:
        exc = DrawNameException("get_last_draw(name)", "Wrong draw name.")
        raise exc

#==========================================================================

def get_last_draw(game):
    gameid = get_draw_id(game)
    surl = url + "draws/v3.0/" + gameid + "/last-result-and-active"

    resp = requests.get(surl)
    j = resp.text
    jdata = json.loads(j)

    if game == "joker" or game == "lotto":
        t = list(jdata["last"]["winningNumbers"]["list"]), int(jdata["last"]["winningNumbers"]["bonus"][0])
        rval = t

    else:
        rval = list(jdata["last"]["winningNumbers"]["list"])

    return rval

def get_draw_from_id(game, id):
    gameid = get_draw_id(game)
    surl = url + "draws/v3.0/" + gameid + "/" + id

    resp = requests.get(surl)
    j = resp.text
    jdata = json.loads(j)

    if game == "joker" or game == "lotto":
        t = list(jdata["winningNumbers"]["list"]), int(jdata["winningNumbers"]["bonus"][0])
        rval = t

    else:
        rval = list(jdata["winningNumbers"]["list"])

    return rval

def get_draw_from_id_range(game, start, end):
    gameid = get_draw_id(game)
    surl = url + "draws/v3.0/" + gameid + "/draw-id/" + start + "/" + end

    resp = requests.get(surl)
    j = resp.text
    jdata = json.loads(j)
    rval = []

    for item in jdata["content"]:

        if game == "joker" or game == "lotto":
            t = int(item["drawId"]), list(item["winningNumbers"]["list"]), int(item["winningNumbers"]["bonus"][0])
            rval.append(t)

        else:
            t = int(item["drawId"]), list(item["winningNumbers"]["list"])
            rval.append(t)

    return rval

def get_last_draws(game, n):
    gameid = get_draw_id(game)
    surl = url + "draws/v3.0/" + gameid + "/last/" + str(int(n) + 1)

    resp = requests.get(surl)
    j = resp.text
    jdata = json.loads(j)[1:]
    rval = []

    for item in jdata:
        if game == "joker" or game == "lotto":
            t = int(item["drawId"]), list(item["winningNumbers"]["list"]), int(item["winningNumbers"]["bonus"][0])
            rval.append(t)

        else:
            t = int(item["drawId"]), list(item["winningNumbers"]["list"])
            rval.append(t)

    return rval

def get_draws_between(game, start, end):
    gameid = get_draw_id_ex_k(game)
    surl = url + "draws/v3.0/" + gameid + "/draw-date/" + start + "/" + end

    resp = requests.get(surl)
    j = resp.text
    jdata = json.loads(j)
    rval = []

    for item in jdata['content']:
        if game == "joker" or game == "lotto":
            t = int(item["drawId"]), list(item["winningNumbers"]["list"]), int(item["winningNumbers"]["bonus"][0])
            rval.append(t)

        else:
            t = int(item["drawId"]), list(item["winningNumbers"]["list"])
            rval.append(t)

    return rval

def get_draw_ids_between(game, start, end):
    gameid = get_draw_id(game)
    surl = url + "draws/v3.0/" + gameid + "/draw-date/" + start + "/" + end + "/draw-id"

    resp = requests.get(surl)
    j = resp.text
    jdata = json.loads(j)
    rval = []
    if "code" in jdata and game == "kino":
        exc = Exception("Kino only supprots one day range date searches")
        raise exc
    for item in jdata:
        rval.append(item)

    return rval

def get_last_draw_id(game):
    gameid = get_draw_id(game)
    surl = url + "draws/v3.0/" + gameid + "/last-result-and-active"

    resp = requests.get(surl)
    j = resp.text
    jdata = json.loads(j)

    return int(jdata["last"]["drawId"])


def get_active_draw_id(game):
    gameid = get_draw_id(game)
    surl = url + "draws/v3.0/" + gameid + "/active"

    resp = requests.get(surl)
    j = resp.text
    jdata = json.loads(j)

    return int(jdata["drawId"])


class DrawNameException(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message