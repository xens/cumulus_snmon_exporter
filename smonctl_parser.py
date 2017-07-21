#!/usr/bin/python

import json
import subprocess

proc = subprocess.Popen(['/usr/sbin/smonctl', '-j'], stdout=subprocess.PIPE)
smonctl = json.loads(proc.stdout.read())

metrics = {}

for metric in smonctl:
    metric['name'] = metric['name'].lower()
    kind = metric.pop('type')

    metrics.setdefault(kind, [])
    metrics[kind].append(metric)

for kind, metric in metrics.items():
    print('# HELP smon_%s (-1=ABSENT, 0=BAD, 1=OK)' % kind)
    print('# TYPE smon_%s gauge' % kind)

    for record in metric:
        if record['state'] == "ABSENT":
            value == -1
        elif record['state'] == "BAD":
            value == 0
        elif record['state'] == "OK":
            value = 1

        print(
            'smon_%s{name="%s",description="%s"} %d' %
            (kind, record['name'], record['description'], value)
        )

    print
