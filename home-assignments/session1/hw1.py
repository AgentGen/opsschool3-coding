import json
fo = open("names.yson", "wb")
with open('names.json') as json_data:
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
print('Age range', buckets[a-1], "to", file=open("names.yson", "a"))
for k, v in sorted(ppl.items(), key=lambda p: p[1], reverse=False):
        print(k, file=open("names.yson", "a"))
        del ppl[k]
fo.close()
