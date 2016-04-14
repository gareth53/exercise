"""
Your company built an in-house calendar tool called HiCal. You want to add a feature to see the times in a 
day when everyone is available.
To do this, you'll need to know when any team is having a meeting. In HiCal, a meeting is stored as tuples 
of integers (start_time, end_time). These integers represent the number of 30-minute blocks past 9:00am.

For example:

(2, 3) # meeting from 10:00 - 10:30 am
(6, 9) # meeting from 12:00 - 1:30 pm

Write a function condense_meeting_times() that takes a list of meeting time ranges and returns a list of 
'busy' condensed ranges.

For example, given:

  [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

your function would return:

  [(0, 1), (3, 8), (9, 12)]

Do not assume the meetings are in order. The meeting times are coming from multiple teams.

In this case the possibilities for start_time and end_time are bounded by the number of 30-minute slots in a day. But soon you plan to refactor HiCal to store times as Unix timestamps (which are big numbers). Write something that's efficient even when we can't put a nice upper bound on the numbers representing our time ranges.
"""

from datetime import datetime

testcases = [
	{
		'desc': 'Meetings simultaneous, equal in length',
		'in':   [(0, 1), (0, 1)],
		'expect': [(0, 1)]
	},
	{
		'desc': 'Meetings overlap',
		'in':   [(0, 2), (1, 3)],
		'expect': [(0, 3)]
	},
	{
		'desc': 'Meetings overlap, 2nd meeting starts earlier',
		'in':   [(2, 4), (0, 3)],
		'expect': [(0, 4)]
	},
	{
		'desc': 'First meeting encompasses asubsequent meeting',
		'in':   [(0, 4), (1, 3)],
		'expect': [(0, 4)]
	},
	{
		'desc': 'Meeting encompasses a previous meeting',
		'in':   [(1, 3), (0, 4)],
		'expect': [(0, 4)]
	},
	{
		'desc': 'Meetings in an unhelpful order',
		'in':   [(1, 3), (0, 4), (0, 1), (13, 14), (5, 6), (15, 16), (12, 13)],
		'expect': [(0, 4), (5, 6), (12, 14), (15, 16)]
	},
	{
		'desc': 'Meetings don\'t overlap, but run into each other',
		'in':   [(0, 4), (4, 6)],
		'expect': [(0, 6)]
	},
	{
		'desc': 'Meeting joins two meetings that doidnlt poreviously overlap',
		'in':   [(0, 1), (3, 6), (1, 3)],
		'expect': [(0, 6)]
	},
	{
		'desc': 'Account for a break',
		'in':   [(0, 1), (3, 6), (7, 8)],
		'expect': [(0, 1), (3, 6), (7, 8)]
	},
	{
		'desc': 'Given testcase',
		'in':   [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)],
		'expect': [(0, 1), (3, 8), (9, 12)]
	}
]


def condense_meeting_times(slots):
	"""
	loop through the existing meetings, build a list of meetings as we go
	merge overlaps
	"""
	slots = sorted(slots)
	condensed_slots = [slots[0]]
	for slot in slots[1:]:
		prev = condensed_slots[-1]
		if slot[0] <= prev[1]:
			new_slot = (min(slot[0], prev[0]), max(slot[1], prev[1]))
			condensed_slots[-1] = new_slot
		elif slot[0] > prev[1]:
			condensed_slots.append(slot)
	return condensed_slots


def test(func):
	for test in testcases:
		st = datetime.now()
		actual = func(test['in'])
		end = datetime.now()
		res = actual ==  test['expect']
		if res:
			print "OK: %s (%sms)" % (test['desc'], (end - st).microseconds)
		else:
			print "FAIL: %s expected: %s, actual: %s" % (test['desc'], test['expect'], actual)

test(condense_meeting_times)
