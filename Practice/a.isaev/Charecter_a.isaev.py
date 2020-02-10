class Character():
    def __init__(self,name,health=100,damage=10,armor=50,speed=100):
        self.name = name
        self.health = health
        self.damage = damage
        self.speed = speed
        self.armor = armor

    def shoot(self):
        print(f"Персонаж {self.name} выстерлил")

    def run(self):
        print(f"Персонаж {self.name} побежал")

    def pick_up(self):
        print(f"Персонаж {self.name} подбирает предмет")

    def is_dead(self):
        return self.health == 0

    def coca_cola(self):
        speed = 120
        print(f"Персонаж {self.name} выпил Кока-полу и его скорость увеличена")

    def beer(self):
        speed = 70
        damage = 8
        health = 70
        print(f"Персонаж {self.name} выпил Пиво и его скорость,здоровье и урон понижены")

class CharacterFly(Character):

    def __init__(self,name,fly_speed = 200):
        Character.__init__(self,name)
        self.name = name
        self.fly_speed = fly_speed

    def fly(self):
        print(f"Персонаж {self.name} полетел")




