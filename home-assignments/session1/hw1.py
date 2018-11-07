#!/usr/bin/python
import json


def sort_json_list(filename):

    fo = open("names.yson", "wb")
    with open(filename) as json_data:
        d = json.load(json_data)
    ppl = (d["ppl_ages"])
    buckets = sorted(d["buckets"])
    a = 1
    for i in buckets:
        if a != len(buckets):
            print('Age range', buckets[a - 1], "to", buckets[a], file=open("names.yson", "a"))
            for k, v in sorted(ppl.items(), key=lambda p: p[1], reverse=False):
                if v <= buckets[a]:
                    print(k, file=open("names.yson", "a"))
                    del ppl[k]
            if a <= (len(buckets) - 1):
                a += 1
    z = sorted(ppl.items(), key=lambda p: p[1], reverse=True)[0]
    print('Age range', buckets[a-1], "to", z[1], file=open("names.yson", "a"))
    for k, v in sorted(ppl.items(), key=lambda p: p[1], reverse=False):
        print(k, file=open("names.yson", "a"))
    del ppl[k]
    fo.close()
    print("Sorting complete")