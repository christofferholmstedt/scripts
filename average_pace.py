#!/usr/bin/python

import datetime
import sys

for distance in [21, 42, 50, 81, 90, 100]:
    print "### " + str(distance) + " km ###"
    print "04:00 | 05:00 | 06:00 | 07:00 | 08:00 min/km"

    for num in range(4, 9):
        pace_per_km = datetime.time(0, num, 0)

        sys.stdout.write(str(datetime.timedelta(minutes=distance * pace_per_km.minute)) + " ")

    print ""
