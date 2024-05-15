
class Warehouse:
	def __init__(self,
								 name,
								 address,
								 distance,
								 supply_cost,
								 product_name,
								 unit_cost,
								 quantity,
								 ) -> None:
		self.name = name
		self.address = address
		self.distance = distance
		self.supply_cost = supply_cost
		self.product_name = product_name
		self.unit_cost = unit_cost
		self.quantity = quantity

	def __str__(self) -> str:
		return f"{self.name}: ${self.product_name} = ${self.unit_cost}"