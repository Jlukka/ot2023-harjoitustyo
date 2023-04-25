import pygame

from math import floor

from baseclasses.scene import Scene
from cardcontainers.discardpile import DiscardPile
from cardcontainers.drawpile import DrawPile
from cardcontainers.playerhand import PlayerHand


class Fight(Scene):
    def __init__(self, scenemanager, player, enemy):
        super().__init__(scenemanager, False)
        self.player_energy = 3
        self.player = player
        self.playerhand = PlayerHand()
        self.enemy = enemy
        self.discardpile = DiscardPile()
        self.drawpile = DrawPile(
            self.player.get_deck(), self.playerhand, self.discardpile)
        self.drawpile.draw_cards(5)

    def handle_events(self):
        pass

    def __handle_actions(actions, target):
        pass

    def end_turn(self):
        self.player_energy = 3
        self.discardpile.discard_hand(self.playerhand)
        self.drawpile.draw_cards(5)
        actions = self.enemy.get_actions()
        self.__handle_actions()

    def _draw_background(self, display):
        display.fill((127, 127, 127))

    def __draw_healthbar(self, display, maxhealth, health, center):
        ratio = health / maxhealth
        bar_width = 15
        bar_length = 200
        top_left_x, top_left_y = (
            center[0] - bar_length // 2, center[1] - bar_width // 2)
        pygame.draw.rect(display, (128, 0, 0), (top_left_x,
                         top_left_y, bar_length, bar_width))
        pygame.draw.rect(display, (188, 0, 0), (top_left_x,
                         top_left_y, floor(bar_length*ratio), bar_width))
        font = pygame.font.SysFont(None, 16)
        text = font.render(f"{health}/{maxhealth}", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = center
        display.blit(text, text_rect)

    def _draw_player(self, display):
        pygame.draw.circle(display, (0, 0, 0), (300, 360), 30)
        self.__draw_healthbar(display, self.player.max_health,
                              self.player.health, (300, 410))

    def _draw_enemy(self, display):
        pygame.draw.circle(display, (128, 0, 0), (980, 360), 30)
        self.__draw_healthbar(display, self.enemy.max_health,
                              self.enemy.health, (980, 410))

    def _draw_UI(self, display):
        pygame.draw.rect(display, (30, 30, 30), (0, 570, 1280, 150))

    def __draw_title(self, display, index, card):
        font = pygame.font.SysFont(None, 18)
        title = font.render(f"{card.title} cost: {card.cost}", True, (0, 0, 0))
        title_rect = title.get_rect()
        title_rect.center = (235+index*90, 560)
        display.blit(title, title_rect)

    def __draw_actions(self, display, index, card):
        font = pygame.font.SysFont(None, 14)
        for j in range(0, len(card.actions)):
            action = card.actions[j]
            action = font.render(f"{action[0]} {action[1]}", True, (0, 0, 0))
            action_rect = action.get_rect()
            action_rect.center = (235+index*90, 590+j*15)
            display.blit(action, action_rect)

    def _draw_cards(self, display):
        cards = self.playerhand.get_cards()
        for i in range(0, len(cards)):
            card = cards[i]
            pygame.draw.rect(display, (175, 175, 175),
                             (195+i*90, 550, 80, 120))
            self.__draw_title(display, i, card)
            self.__draw_actions(display, i, card)

    def _draw_drawpile(self, display):
        pygame.draw.rect(display, (175, 175, 175), (20, 550, 80, 120))
        font = pygame.font.SysFont(None, 14)
        draw = font.render(f"{len(self.drawpile.cards)}", True, (0, 0, 0))
        draw_rect = draw.get_rect()
        draw_rect.center = (60, 610)
        display.blit(draw, draw_rect)

    def _draw_discardpile(self, display):
        pygame.draw.rect(display, (175, 175, 175), (1140, 550, 80, 120))
        font = pygame.font.SysFont(None, 14)
        draw = font.render(f"{len(self.discardpile.cards)}", True, (0, 0, 0))
        draw_rect = draw.get_rect()
        draw_rect.center = (60, 1180)
        display.blit(draw, draw_rect)

    def render(self, display):
        self._draw_background(display)
        self._draw_player(display)
        self._draw_enemy(display)
        self._draw_UI(display)
        self._draw_cards(display)
        self._draw_drawpile(display)
        self._draw_discardpile(display)
