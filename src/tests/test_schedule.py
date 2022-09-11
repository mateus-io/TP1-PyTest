import datetime
from src.entities.schedule import Schedule

def test_create_an_schedule():
    customer = "John Doe"
    schedule = Schedule(
        customer=customer,
        startsAt=datetime.datetime.now(),
        endsAt=datetime.datetime.now(),
    )
    assert isinstance(schedule, Schedule)
    assert schedule.customer == "Cliente: " + customer