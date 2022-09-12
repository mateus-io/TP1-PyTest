import datetime

class Schedule:
  def __init__(self, customer, startsAt, endsAt):
    current_date = datetime.datetime.now()
    if (startsAt < current_date or endsAt < current_date):
      raise Exception("Dates provided can't be in the past")
    if (endsAt <= startsAt):
      raise Exception("End Date provided can't be before than Start Date")
    self.customer = customer
    self.startsAt = startsAt
    self.endsAt = endsAt
  
  @property
  def customer(self):
    return "Cliente: " + self._customer

  @customer.setter
  def customer(self, value):
    self._customer = value
  
  @property
  def startsAt(self):
    return self._startsAt.strftime("%m/%d/%Y, %H:%M:%S")
  
  @startsAt.setter
  def startsAt(self, value):
    self._startsAt = value
  
  @property
  def endsAt(self):
    return self._endsAt.strftime("%m/%d/%Y, %H:%M:%S")
  
  @endsAt.setter
  def endsAt(self, value):
    self._endsAt = value