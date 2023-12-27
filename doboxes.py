from pprint import pprint

f = open("boxes")
entry={}
for aline in f:
    line=aline.strip().replace("#","");
    #print len(line),line,entry
    if not len(line):
        if entry:
            pprint(dict(entry),width=250)
        entry={}
    else:
        if "=" in line:
            v=line.split("=")
            entry[v[0]]=v[1]
        else:
            entry["xdesc"]=line

pprint(dict(entry),width=250)
