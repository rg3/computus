#!/usr/bin/env python3
#
# Written in 2018 by Ricardo Garcia <r@rg3.name>
#
# To the extent possible under law, the author(s) have dedicated all copyright
# and related and neighboring rights to this software to the public domain
# worldwide. This software is distributed without any warranty.
#
# You should have received a copy of the CC0 Public Domain Dedication along
# with this software. If not, see
# <http://creativecommons.org/publicdomain/zero/1.0/>.
#
# The algorithm below calculates the calendar date of Easter in the Gregorian
# Calendar. The calculation is valid as long as the Gregorian Calendar is, will
# be or was in use in the requested year. As of the time I'm writing this code,
# the world has not transitioned completely to the Gregorian Calendar, and the
# earliest adoption date was 1582 in some countries. Thanks to leap second
# corrections, we expect to be using the Gregorian Calendar for a long time, but
# I have set a comfortable upper limit too.
#
# https://en.wikipedia.org/wiki/Adoption_of_the_Gregorian_calendar
#
# Reference: https://en.wikipedia.org/wiki/Computus
#

import sys
import datetime

MINYEAR = 1900
MAXYEAR = 4000

def usage():
    sys.exit('Usage: %s YEAR, with YEAR in range %s-%s'
            % (sys.argv[0], MINYEAR, MAXYEAR))

if len(sys.argv) != 2:
    usage()

try:
    year = int(sys.argv[1])
except:
    usage()

if year < MINYEAR or year > MAXYEAR:
    usage()

# "A New York correspondent" submission to the Nature journal, 1876.
A = year % 19
B, C = divmod(year, 100)
D, E = divmod(B, 4)
F = (B + 8) // 25
G = (B - F + 1) // 3
H = (19*A + B - D - G + 15) % 30
I, K = divmod(C, 4)
L = (32 + 2*E + 2*I - H - K) % 7
M = (A + 11*H + 22*L) // 451
N = H + L - 7*M + 114

month = N // 31
day = 1 + (N % 31)

# Easter and some significant dates that depend on it.
easter = datetime.date(year, month, day)
palm_sunday = easter - datetime.timedelta(days=7)
ash_wednesday = palm_sunday - datetime.timedelta(days=39)
tuesday_of_carnival = ash_wednesday - datetime.timedelta(days=1)
maundy_thursday = tuesday_of_carnival - datetime.timedelta(days=5)

def print_monthday(label, date):
    print('%-20s  %d-%02d-%02d' % (label, date.year, date.month, date.day))

print('Year %d' % year)
print_monthday('Maundy Thursday', maundy_thursday)
print_monthday('Tuesday of Carnival', tuesday_of_carnival)
print_monthday('Ash Wednesday', ash_wednesday)
print_monthday('Palm Sunday', palm_sunday)
print_monthday('Easter', easter)
