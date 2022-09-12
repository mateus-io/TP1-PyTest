import pytest
import datetime
from src.usecases.create_schedule import CreateSchedule
from src.entities.schedule import Schedule
from src.repositories.in_memory.in_memory_schedule_repository import InMemoryScheduleRepository

class TestCreateSchedule:
  def test_create_schedule(self):
    customer = "John Doe"
    future_date = datetime.datetime.now() + datetime.timedelta(days=30)
    
    inMemoryScheduleRepository = InMemoryScheduleRepository()
    createSchedule = CreateSchedule(inMemoryScheduleRepository)

    schedule = createSchedule.execute(
      customer=customer,
      startsAt=future_date + datetime.timedelta(days=10),
      endsAt=future_date + datetime.timedelta(days=25),
    )
    assert isinstance(schedule, Schedule)
  
  def test_cannot_create_schedule_when_overlap_another_one(self):
    customer = "John Doe"
    future_date = datetime.datetime.now() + datetime.timedelta(days=30)

    inMemoryScheduleRepository = InMemoryScheduleRepository()
    createSchedule = CreateSchedule(inMemoryScheduleRepository)

    createSchedule.execute(
      customer=customer,
      startsAt=future_date + datetime.timedelta(days=10),
      endsAt=future_date + datetime.timedelta(days=25),
    )

    with pytest.raises(Exception) as exception_info:
      createSchedule.execute(
        customer=customer,
        startsAt=future_date + datetime.timedelta(days=15),
        endsAt=future_date + datetime.timedelta(days=20),
      )
    assert str(exception_info.value) == "Exists another schedule overlapping this range"
  
  def test_create_multiple_schedules_with_different_intervals(self):
    customer = "John Doe"
    future_date = datetime.datetime.now() + datetime.timedelta(days=30)

    inMemoryScheduleRepository = InMemoryScheduleRepository()
    createSchedule = CreateSchedule(inMemoryScheduleRepository)

    createSchedule.execute(
      customer=customer,
      startsAt=future_date + datetime.timedelta(days=10),
      endsAt=future_date + datetime.timedelta(days=25),
    )

    createSchedule.execute(
      customer=customer,
      startsAt=future_date + datetime.timedelta(days=26),
      endsAt=future_date + datetime.timedelta(days=40),
    )

    createSchedule.execute(
      customer=customer,
      startsAt=future_date + datetime.timedelta(days=41),
      endsAt=future_date + datetime.timedelta(days=60),
    )

    assert len(inMemoryScheduleRepository.schedules) == 3