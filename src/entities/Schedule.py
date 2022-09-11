class Schedule:
  def __init__(self, customer, startsAt, endsAt):
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
    return self._startsAt
  
  @startsAt.setter
  def startsAt(self, value):
    self._startsAt = value
  
  @property
  def endsAt(self):
    return self._endsAt
  
  @endsAt.setter
  def endsAt(self, value):
    self._endsAt = value