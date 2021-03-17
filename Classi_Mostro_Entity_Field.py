class Entity:
    def __init__(self, x, y, field):
        self.x = x
        self.y = y
        self.field = field
        self.field.entities.append(self)
    
    def move(self, direction):
        if direction == "up":
            self.y -= 1
        elif direction == "down":
            self.y += 1
        if direction == "left":
            self.x -= 1
        if direction == "right":
            self.x += 1
    
    def corners(self):
        if self.x > self.field.w:
            print("l'entità non può muoversi più a destra di così")
            self.x -= 1
        elif self.x < 1:
            print("l'entità non può muoversi più a sinistra di così")
            self.x += 1
        elif self.y > self.field.h:
            print("l'entità non può muoversi più in basso di così")
            self.y -= 1
        elif self.y < 1:
            print("l'entità non può muoversi più in alto di così")
            self.y += 1


class Monster(Entity):
    def __init__(self, x, y, name, damage, field):
        super().__init__(x, y, field)
        self.name = name
        self.hp = 10
        self.damage = damage
    
    def info(self):
        print("Sono", self.name, "hp:", self.hp, "/15", "e sono a", (self.x, self.y))
    
    def attack(self, enemy):
        print(self.name, "attacca", enemy.name)
        if self.hp <=0:
            print(self.name, "è morto e non può più attaccare")
        else:
            print(self.name, "attacca", enemy.name)

        if (enemy.hp <= 0):
            print(enemy.name, "è morto")
        else:
            enemy.hp -= self.damage

class Field:
    def __init__(self):
        self.w = 5
        self.h = 5
        self.entities = []
    
    def draw(self):
        for y in range(self.h):
            for x in range(self.w):
                for e in self.entities:
                    if x == e.x and y == e.y:
                        print("[x]", end = "")
                        break
                else:
                    print("[ ]", end = "")
            print()

field = Field() 
m = Monster(2, 2, "Pino", 5, field)
m1 = Monster(1, 1, "Franco", 5, field)
m.info()
m1.info()
field.draw()

for n in range(5):
  print()
  m.move("down")
  m.corners()
  m.info()
  m1.info()
  field.draw()

print()
m1.move("down")
m1.corners()
m.info()
m1.info()
field.draw()

for a in range(3):
  print()
  m.attack(m1)
  m.info()
  m1.info()
  field.draw()

print()
m1.attack(m)
m.info()
m1.info()
field.draw()
