from src.utils.overlapping import Range, calc_overlapping_between_rages

class InMemoryScheduleRepository:
  schedules = []

  def __init__(self):
    self.schedules = []

  def create(self, schedule):
    self.schedules.append(schedule)
  
  def find_overlapping_schedule(self, startsAt, endsAt):
    result = list(filter(
      lambda schedule: (
        calc_overlapping_between_rages(
          range1=Range(start=startsAt, end=endsAt),
          range2=Range(start=schedule._startsAt, end=schedule._endsAt)
        ) != 0
      ),
      self.schedules
    ))
    return result