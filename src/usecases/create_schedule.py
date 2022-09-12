from src.entities.schedule import Schedule

class CreateSchedule:
  def __init__(self, scheduleRepository):
    self.scheduleRepository = scheduleRepository

  def execute(self, customer, startsAt, endsAt):
    schedulesOverlapped = self.scheduleRepository.find_overlapping_schedule(
      startsAt=startsAt,
      endsAt=endsAt,
    )
    if (len(schedulesOverlapped) > 0):
      raise Exception("Exists another schedule overlapping this range")
    else:
      schedule = Schedule(
        customer=customer,
        startsAt=startsAt,
        endsAt=endsAt
      )
      self.scheduleRepository.create(schedule)
      return schedule