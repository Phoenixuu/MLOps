from abc import ABC, abstractmethod

# Step 1: Define Strategy Interface
class PaymentMethod(ABC):
	@abstractmethod
	def pay(self, amount):
		pass

# Step 2: Implement Concrete Strategies
class CreditCardPayment(PaymentMethod):
	def pay(self, amount):
		return f"Paying {amount}$ using Credit Card."

class Paypal(PaymentMethod):
	def pay(self, amount):
		return f"Paying {amount}$ using Paypal."

class BitcoinPayment(PaymentMethod):
	def pay(self, amount):
		return f"Paying {amount}B using Bitcoin."

class MasterCardPayment(PaymentMethod):
	def pay(self, amount):
		return f"Paying {amount}$ using MasterCardPayment."

# Step 3: Implement the Context
class ShoppingCart:
	def __init__(self, payment_method: PaymentMethod):
		self.payment_method = payment_method

	def checkout(self, amount):
		return self.payment_method.pay(amount)

# Step 4: Use the Strategy in the Context
if __name__ == "__main__":
	cart = ShoppingCart(CreditCardPayment())
	print(cart.checkout(100))

	cart = ShoppingCart(Paypal())
	print(cart.checkout(200))

	cart = ShoppingCart(MasterCardPayment())
	print(cart.checkout(80))

	cart = ShoppingCart(BitcoinPayment())
	print(cart.checkout(0.01))