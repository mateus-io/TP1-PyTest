import pytest
import datetime
from src.entities.schedule import Schedule

class TestSchedule:
  def test_create_an_scheduling(self):
    customer = "John Doe"
    future_date = datetime.datetime.now() + datetime.timedelta(days=30)
    schedule = Schedule(
        customer=customer,
        startsAt=future_date + datetime.timedelta(days=2),
        endsAt=future_date + datetime.timedelta(days=5),
    )
    assert isinstance(schedule, Schedule)
    assert schedule.customer == "Cliente: " + customer

  def test_cannot_create_schedule_dates_in_past(self):
    current_date = datetime.datetime.now()
    customer = "John Doe"
    with pytest.raises(Exception) as exception_info:
      Schedule(
        customer=customer,
        startsAt=current_date + datetime.timedelta(days=-5),
        endsAt=current_date + datetime.timedelta(days=-5),
      )
    assert str(exception_info.value) == "Dates provided can't be in the past"

  def test_cannot_create_schedule_with_end_date_before_start_date(self):
    future_date = datetime.datetime.now() + datetime.timedelta(days=30)
    customer = "John Doe"
    with pytest.raises(Exception) as exception_info:
        Schedule(
            customer=customer,
            startsAt=future_date + datetime.timedelta(days=3),
            endsAt=future_date + datetime.timedelta(days=2),
        )
    assert str(exception_info.value) == "End Date provided can't be before than Start Date"
