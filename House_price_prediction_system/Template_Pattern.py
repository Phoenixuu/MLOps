from abc import ABC, abstractmethod

#Step 1 Create an abstract base class
class DininngExperience(ABC):

	#The template method defining the skeleton of the dining ex
	def serve_dinner(self):
		self.serve_appetizer()
		self.serve_main_couse()
		self.serve_dessert()
		self.serve_beverage()

	#Abstract methods to serve each course (to be implement)
	@abstractmethod
	def serve_appetizer(self):
		pass

	@abstractmethod
	def serve_main_couse(self):
		pass

	@abstractmethod
	def serve_dessert(self):
		pass

	@abstractmethod
	def serve_beverage(self):
		pass

#Step 2: Create concrete classes that implement the template design pattern
class ItatlianDinner(DininngExperience):
	def serve_appetizer(self):
		print("Serving bruschetta as appetizer.")

	def serve_main_couse(self):
		print("Serving pasta as main course.")

	def serve_dessert(self):
		print("Serving tiramisu as dessert.")

	def serve_beverage(self):
		print("Serveing wine as the beverage.")

class ChineseDinner(DininngExperience):
	def serve_appetizer(self):
		print("Serving spring rolls as appetizer.")

	def serve_main_couse(self):
		print("Serving stir-fried noodles as the main course.")

	def serve_dessert(self):
		print("Serving fortune cookies as dessert.")

	def serve_beverage(self):
		print("Serving tea as the beverage.")

#Step 3: Client code
if __name__ == "__main__":
	print("ItatlianDinner: ")
	italian_dinner = ItatlianDinner()
	italian_dinner.serve_dinner()

	print("\nChinese Dinner: ")
	chinese_dinner = ChineseDinner()
	chinese_dinner.serve_dinner()