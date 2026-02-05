from dataclasses import dataclass


@dataclass
class Stats:
	strength: int
	dexterity: int
	constitution: int
	intelligence: int
	wisdom: int
	charisma: int

	def as_dict(self):
		return {
			"strength": self.strength,
			"dexterity": self.dexterity,
			"constitution": self.constitution,
			"intelligence": self.intelligence,
			"wisdom": self.wisdom,
			"charisma": self.charisma,
		}

	@property
	def str_mod(self) -> int:
		return (self.strength - 10) // 2

	@property
	def dex_mod(self) -> int:
		return (self.dexterity - 10) // 2

	@property
	def con_mod(self) -> int:
		return (self.constitution - 10) // 2

	@property
	def int_mod(self) -> int:
		return (self.intelligence - 10) // 2

	@property
	def wis_mod(self) -> int:
		return (self.wisdom - 10) // 2

	@property
	def cha_mod(self) -> int:
		return (self.charisma - 10) // 2

