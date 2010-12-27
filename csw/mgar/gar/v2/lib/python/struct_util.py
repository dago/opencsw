"""A module for generic data structure processing functions.
"""

def IndexDictsBy(list_of_dicts, field_key):
  """Creates an index of list of dictionaries by a field name.

  Returns a dictionary of lists.
  """
  index = {}
  for d in list_of_dicts:
    index.setdefault(d[field_key], [])
    index[d[field_key]].append(d)
  return index
