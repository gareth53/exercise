
def sort_dict(dict_list, key=None):
	"""
	:param dict_list: <list> of <dict>s [{}, {}]
	:param sort_keys: <list> of <str>
	:return: <list>
	"""
	if key:
		if not type(key) in (list, tuple):
			return sorted(dict_list, key=lambda x: x[key])
		else:
			return sorted(dict_list, key=lambda x: "".join([x[k] for k in key]))
	return dict_list