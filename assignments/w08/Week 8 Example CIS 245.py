# CIS 245 Week 8 Example, Mortgage Calculator Program

class Mortgage(object):
	# Base class with attributes loan, rates, period
	def __init__(self, loan, rate, period):
		self.loan = loan
		self.rate = (rate / 100)
		self.period = period

	def setAttributes(self, loan, rate, period):
		self.loan = loan
		self.rate = rate
		self.period = period

	def formula(self):
		return (self.loan * ( self.rate / (1-(1+self.rate) **(-self.period))))

	#Inheriting classes
class Fixed_mortgage(Mortgage):
	# Calculates for fixed mortgage. Takes two additional variablesfor mortgage payment plan and payment period(years/months/weeks)
	def __init__(self, loan, rate, period, m_type, time_period):
		Mortgage.__init__(self, loan, rate, period)
		self.m_type = m_type
		self.time_period = time_period

	def display(self):
		print('Your {m_type} mortgage installment is ${formula} for {period} {time_period} at {rate} interest rate.'
				 .format(m_type= self.m_type, formula=round(self.formula(), 2), period= self.period, rate= round(self.rate, 5), time_period= self.time_period))

		print('\nExpected total amount after {period} {time_period} is: ${mortgage_pay}'
				 .format(time_period= self.time_period, period=self.period, mortgage_pay = round(self.formula()*self.period, 2)))

class Adjustable_mortgage(Mortgage):
	# calculates for fixed mortgage. takes two additional variables for mortgage payment plan and payment period(years/months/weeks)
	def __init__(self, loan, rate, period, m_type, time_period, adjust_rate, time_spent):
		Mortgage.__init__(self, loan, rate, period)
		self.m_type = m_type
		self.time_period = time_period
		self.adjust_rate = adjust_rate
		self.time_spent = time_spent
		
	def display(self):
		print('Your {m_type} mortgage installment is ${formula} for first {time_spent} {time_period} at {rate} interest rate.'
				 .format(m_type= self.m_type, formula=round(self.formula(), 2), time_spent= self.time_spent, rate= round(self.rate, 5), time_period= self.time_period))
					
		self.rate = (self.rate + (self.adjust_rate))
		self.period = (self.period - self.time_spent)

		print('\nAdjusted mortgage installment for remaining {period} {time_period} is $:{mortgage_pay} at {rate} interest rate.'
				.format(time_period= self.time_period, period=self.period, mortgage_pay = round(self.formula(), 2), rate= round(self.rate, 5)))

def adjustedCalc():
	# Function for calculating adjusted mortgage option based on payment plan
	print('\nCompute for:\n1) Yearly\n2) Monthly\n3) Weekly\n4) Daily\n-------------------------------')
	term = int(input('\nInput a corresponding digit for the payment term: '))
	period = int(input('Input the payment period in years: '))
	rate = float(input('Input the interest rate: '))
	loan = float(input('Input the loan value:$'))
	adjust_rate = float(input('Input value less than 1 to adjust rate by after 1 year(eg:-0.2,0.04): '))
	
	if term == 1:
		yearly = Adjustable_mortgage(  loan, rate, period, 'yearly', 'years', adjust_rate, 1)
		yearly.display()
	
	elif term == 2:
		monthly = Adjustable_mortgage(  loan, (rate/12), (period*12), 'monthly', 'months', adjust_rate, 12)
		monthly.display()

	elif term == 3:
		weekly = Adjustable_mortgage(  loan, (rate/52), (period*52), 'weekly', 'weeks', adjust_rate, 52)
		weekly.display()
	
	else:
		daily = Adjustable_mortgage(  loan, (rate/365), (period*365), 'weekly', 'weeks', adjust_rate, 365)
		daily.display()
	

def fixedCalc():
	# Function for calculating fixed mortgage option based on payment plan
	# We cam utilize code from prior function
	print('\nCompute for:\n1) Yearly\n2) Monthly\n3) Weekly\n4) Daily\n-------------------------------')
	term = int(input('\nInput a corresponding digit for the payment term: '))
	period = int(input('Input the payment period in years: '))
	rate = float(input('Input the interest rate: '))
	loan = float(input('Input the loan value:$'))

	if term == 1:
		yearly = Fixed_mortgage(  loan, rate, period, 'yearly', 'years')
		yearly.display()
	   
	elif term == 2:
		monthly = Fixed_mortgage(  loan, (rate/12), (period*12), 'monthly', 'months')
		monthly.display()

	elif term == 3:
		weekly = Fixed_mortgage(  loan, (rate/52), (period*52), 'weekly', 'weeks')
		weekly.display()
	
	else:
		daily = Fixed_mortgage(  loan, (rate/365), (period*365), 'weekly', 'weeks')
		daily.display()
		
#main function		
if __name__ == '__main__':
	print('Selet one of the options below to proceed.\n1)Fixed Mortgage\n2)Adjustable Mortgage')
	value = (int(input('\nInput: ')))

	if value == 1:
		fixedCalc()
	else:
		print('For this option, the first year is calculated as fixed mortgage and the remaining as adjusted using the provided adjusted rate.')
		adjustedCalc()