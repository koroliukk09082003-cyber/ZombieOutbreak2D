from kivy.app import App
        x = randint(0, 350)
        self.zombies.append(Zombie(x, 650))

    def on_touch_down(self, touch):
        self.bullets.append(
            Bullet(self.player_x + 20, self.player_y + 40)
        )

    def update(self, dt):
        self.canvas.clear()

        with self.canvas:
            Color(0.1, 0.1, 0.1)
            Rectangle(pos=(0, 0), size=(400, 700))

            Color(0, 0, 1)
            Rectangle(
                pos=(self.player_x, self.player_y),
                size=(self.player_size, self.player_size)
            )

            Color(1, 0, 0)
            for zombie in self.zombies:
                zombie.y -= zombie.speed
                Rectangle(
                    pos=(zombie.x, zombie.y),
                    size=(zombie.size, zombie.size)
                )

            Color(1, 1, 0)
            for bullet in self.bullets:
                bullet.y += bullet.speed
                Ellipse(
                    pos=(bullet.x, bullet.y),
                    size=(bullet.size, bullet.size)
                )

        for bullet in self.bullets[:]:
            if bullet.y > 700:
                self.bullets.remove(bullet)

        for zombie in self.zombies[:]:
            if zombie.y < 0:
                self.zombies.remove(zombie)

        for zombie in self.zombies[:]:
            for bullet in self.bullets[:]:
                if (
                    bullet.x > zombie.x and
                    bullet.x < zombie.x + zombie.size and
                    bullet.y > zombie.y and
                    bullet.y < zombie.y + zombie.size
                ):
                    if zombie in self.zombies:
                        self.zombies.remove(zombie)

                    if bullet in self.bullets:
                        self.bullets.remove(bullet)

                    self.score += 1
                    self.score_label.text = f'Kills: {self.score}'

class ZombieOutbreakApp(App):
    def build(self):
        return GameWidget()

ZombieOutbreakApp().run()
