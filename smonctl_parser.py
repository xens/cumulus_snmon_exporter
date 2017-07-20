#!/usr/bin/python

import json
import subprocess

proc = subprocess.Popen(['/usr/sbin/smonctl', '-j'], stdout=subprocess.PIPE)
smonctl_output = json.loads(proc.stdout.read())

metrics = {}

for i in smonctl_output:

    if i['type'] not in metrics:
        metrics[i['type']] = []

    name = i['name'].lower()
    descr = i['description']
    state = i['state']

    metrics[i['type']].append([name, descr, state])

for k in metrics:

    print("# HELP smon_%s (-1=ABSENT, 0=BAD, 1=OK)" % (k))
    print("# TYPE smon_%s gauge" % k)

    for v in metrics[k]:

        if v[2] == "OK":
            value = 1
        elif v[2] == "ABSENT":
            value == -1
        elif v[2] == "BAD":
            value == 0

        print('smon_%s{name="%s"} %s' % (k,v[0],value))
