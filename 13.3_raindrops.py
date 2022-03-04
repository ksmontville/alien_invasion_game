# Kyle Montville
# 1.4.21

# A game which creates a steady stream of raindrops down the screen

import sys

import pygame


from misc_work.raindrop import Raindrop


class RaindropGame:
    """A class to manage the behavior of the Raindrop Game."""

    def __init__(self):
        """Initialize the attributes of the game."""
        pygame.init()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        self.bg_color = (255, 255, 255)

        pygame.display.set_caption("Raindrops")

        self.raindrops = pygame.sprite.Group()
        self._draw_raindrop_field()
        self.moving_down = False

    def run_game(self):
        """Manages the main event loops of the game."""
        while True:
            self._check_events()
            if self.moving_down:
                self.raindrops.update()
            self._update_screen()

    def _check_events(self):
        """Checks for key presses and other events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Manages key down events."""
        key_input = pygame.key.get_pressed()
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.moving_down = True

    def _check_keyup_events(self, event):
        if event.key == pygame.K_SPACE:
            self.moving_down = False

    def _draw_raindrop_field(self):
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size

        available_space_x = self.screen_width
        available_space_y = self.screen_height // 2

        number_raindrops = available_space_x // raindrop_width
        number_rows = available_space_y // raindrop_height

        for row_number in range(number_rows):
            for raindrop_number in range(number_raindrops):
                self._draw_raindrop(row_number, raindrop_number)

    def _draw_raindrop(self, row_number, raindrop_number):
        """Draws a raindrop to the screen."""
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size

        raindrop.x = raindrop_width * raindrop_number
        raindrop.y = raindrop_height * row_number
        raindrop.rect.x = raindrop.x
        raindrop.rect.y = raindrop.y

        self.raindrops.add(raindrop)

    def _update_screen(self):
        """Draws and refreshes the screen."""
        self.screen.fill(self.bg_color)
        self.raindrops.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    rg = RaindropGame()
    rg.run_game()



