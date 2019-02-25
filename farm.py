class Farm:

    harvested_food = 0
    corn_size = 0
    wheat_size = 0

    def __init__(self, type, size):
        self.type = type
        self.size = size

    @classmethod
    def add(cls, type, size):
        if type == "corn":
            cls.corn_size += size
        elif type == "wheat":
            cls.wheat_size += size
        return True

    @classmethod
    def total_harvest(cls):
        if cls.corn_size > 0:
            print("Corn field is {} hectares.".format(cls.corn_size))
        if cls.wheat_size > 0:
            print("Wheat field is {} hectares.".format(cls.wheat_size))

        print("The farm has {} harvested food so far.".format(cls.harvested_food))

    @classmethod
    def harvest(cls):
        harvested_corn = cls.corn_size * 20
        harvested_wheat = cls.wheat_size * 30
        cls.harvested_food = harvested_corn + harvested_wheat
        if cls.corn_size > 0:
            print("Harvesting {} food from {} hectare corn field.".format(harvested_corn, cls.corn_size))
        if cls.wheat_size > 0:
            print("Harvesting {} food from {} hectare wheat field.".format(harvested_wheat, cls.wheat_size))
        print("The farm has {} harvested food so far.".format(cls.harvested_food))
        return cls.harvested_food

    @classmethod
    def relax_message(cls):
        print("{} hectares of tall green stalks rustling in the breeze fill your horizon.".format(cls.corn_size))
        print("The sun hangs low, casting an orange glow on a sea of {} hectares of wheat.".format(cls.wheat_size))
