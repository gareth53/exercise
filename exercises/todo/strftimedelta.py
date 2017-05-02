
"""

expectations = 

HH:MM.SS

02:01.21
1 day, 2:13.01
2 days, 12:09.01
24 hours
32 hours
3 days, 2 hours
14 days
3 weeks
4 months
18 months
2 years, 3months


the interface:

%Y = Years
%M = Total months
%m = months (less the years)
%W = total weeks
%w = total weeks (less the months)

%D = total days
%d = days (less the months)
%H = total hours (zero padded)
%h = hours (less the days)
%J = total minutes
%j = minutes (less the hours)
%F = total millseconds
%f = milliseconds (less the seconds)

for zero-padded numbers, add a hyphen e.g.

%-h:%-m:%-s

Not passing a format string leaves the function to figure it out...
auto formatting is human readable, zero-pads for hours/mins/secs, but not for years/weeks/days
"""

class T:
	"""
	A representation a measurement of time
	"""

	def __init__(name, ms, format_pattern)
		self.name = name
		self.ms = ms
		self.pattern = pattern
 


class Diff:

	in_ms = OrderedDict(
		'year': T('year', 1000 * 60 * 60 *24 * 364.25, "Y")
		'month',
		'week',
		'day',
		'hour',
		'minute',
		'second', 
		'millisecond',
	)


	def __init__(ms):
		self.ms = ms

	def calculate_totals(ms):
		# do a lopp, use __setattr__
		self.years
		self.months
		self.weeks
		self.days
		self.hours, remainder = divmod(ms, 36000)
		self.minutes, remainder = divmod(remainder, 600)
		self.seconds, remainder = divmod(remainder, 10)
		self.milliseconds = remainder


	def calculate_subtotals(ms):
		self.years, r = divmod(r, 36000)
		self.months, r = divmod(r, 36000)
		self.weeks, r = divmod(r, 36000)
		self.days, r = divmod(r, 36000)
		self.hours, r = divmod(r, 36000)
		self.minutes, r = divmod(r, 600)
		self.seconds, r = divmod(r, 10)
		self.milliseconds = r

	@staticmethod
	def _pad_zero(val):
		if val < 10:
			return "0{}".format(val)
		return str(val)


format_map = {
	'%Y' : { 'attr': '', 'func': _pad_zero }
}


def strftimedelta(timedelta):
	hours, remainder = divmod(duration_time_delta, 3600)
	minutes, seconds = divmod(remainder, 60) 
	duration_formatted = ‘%d:%02d:%02d’ % (hours, minutes, seconds)



