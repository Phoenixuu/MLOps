from abc import ABC, abstractmethod

# Step 1: Define the Product interface
class SportStore(ABC):
	@abstractmethod
	def Price(self):
		pass

# Step 2: Implement Concrete Products
class Basketball(SportStore):
	def Price(self):
		return "One Basketball costs 25$ for size 7."

class Baseball(SportStore):
	def Price(self):
		return "One Baseball costs 20$ for size 5."

class TennisBall(SportStore):
	def Price(self):
		return "One TennisBall costs 10$ for size 2."

class GolfBall(SportStore):
	def Price(self):
		return "One GolfBall costs 18$ for size 1."

# Step 3: Implement the Factory (SportStore)
class CreateShopping:
	def buy_ball(self, ball_type):
		if ball_type == "Basketball":
			return Basketball().Price()
		elif ball_type == "Baseball":
			return Baseball().Price()
		elif ball_type == "GolfBall":
			return GolfBall().Price()
		elif ball_type == "TennisBall":
			return TennisBall().Price()
		else:
			return "There is no type of ball in SportStore."

# Step 4: Use the Factory to Create Products
if __name__ == "__main__":
	Customer = CreateShopping()

	Sunday_shopping = Customer.buy_ball("Basketball")
	print(Sunday_shopping)

	Wednesday_shopping = Customer.buy_ball("Baseball")
	print(Wednesday_shopping)

	Saturday_shopping = Customer.buy_ball("GolfBall")
	print(Saturday_shopping)

	Thurday_shopping = Customer.buy_ball("TennisBall")
	print(Thurday_shopping)

	Tuesday_shopping = Customer.buy_ball("FootBall")
	print(Tuesday_shopping)