"""
Your company built an in-house calendar tool called HiCal. You want to add a feature to see the times 
in a day when everyone is available.
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
