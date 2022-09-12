from collections import namedtuple
Range = namedtuple('Range', ['start', 'end'])

def calc_overlapping_between_rages(range1, range2):
  print("ay ay aaa")
  latest_start = max(range1.start, range2.start)
  earliest_end = min(range1.end, range2.end)
  delta = (earliest_end - latest_start).days + 1
  overlap = max(0, delta)
  print(overlap)
  return overlap