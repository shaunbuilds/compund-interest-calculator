p = int(input("Enter the principal amount: ")) # The principal amount
i = float(input("Enter the interest rate (per annum) : ")) # The interest rate
t = int(input("Enter the time period (in years) : ")) #The time period
n = int(input("Enter the number of times a year is it compounded: ")) #No. of times
class CompoundInterest:
  def __init__(self, p, i, t, n):
    self.p = p
    self.i = i
    self.t = t
    self.n = n
  def calculate(self):
    return self.p * (1 + self.i/self.n) ** (self.n*self.t)
  def display(self):
    print(f"\nInitial Investment: {self.p}")
    print(f"\nInterest Rate: {self.i}%")
    print(f"\nYears: {self.t}")
    for year in range(1, self.t + 1):
        yearly_amount = self.p * (1 + self.i/self.n) ** (self.n * year)
        print(f"\nYear {year}: {yearly_amount}")
    a = self.calculate()
    g = a - self.p
    print(f"\nYour investment grew by {g}!")
ci = CompoundInterest(p, i, t, n)
ci.display()

