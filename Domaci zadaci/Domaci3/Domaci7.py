class Player:
    def __init__(self, x, y, width, height, health):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width

    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height = height

    def get_health(self):
        return self.health

    def set_health(self, health):
        if 0 <= health <= 100:
            self.health = health

    def decrease_health(self, damage):
        if damage > 0:
            self.health -= damage
            if self.health < 0:
                self.health = 0


class Enemy:
    def __init__(self, x, y, width, height, damage):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.damage = damage

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width

    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height = height

    def get_damage(self):
        return self.damage

    def set_damage(self, damage):
        if 0 <= damage <= 100:
            self.damage = damage


def check_collision(player, enemy):
    player_x, player_y = player.get_x(), player.get_y()
    player_width, player_height = player.get_width(), player.get_height()
    enemy_x, enemy_y = enemy.get_x(), enemy.get_y()
    enemy_width, enemy_height = enemy.get_width(), enemy.get_height()

    if (player_x < enemy_x + enemy_width and
            player_x + player_width > enemy_x and
            player_y < enemy_y + enemy_height and
            player_y + player_height > enemy_y):
        return True
    return False


def decrease_health(player, enemy):
    if check_collision(player, enemy):
        player.decrease_health(enemy.get_damage())

player = Player(0, 0, 20, 20, 100)
enemy1 = Enemy(10, 10, 15, 15, 20)
enemy2 = Enemy(30, 30, 15, 15, 30)

print("Prije sudara: Zdravlje igrača:", player.get_health())
print("Sudar s enemy1:", check_collision(player, enemy1))
decrease_health(player, enemy1)
print("Nakon sudara s enemy1: Zdravlje igrača:", player.get_health())

print("Sudar s enemy2:", check_collision(player, enemy2))
decrease_health(player, enemy2)
print("Nakon sudara s enemy2: Zdravlje igrača:", player.get_health())
