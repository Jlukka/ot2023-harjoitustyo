import pygame


from mainloop import MainLoop
from eventqueue import EventQueue
from clock import Clock
from renderer import Renderer
from scenemanager import SceneManager

from cardcontainers.playerdeck import PlayerDeck

from cards.cards import Slash, Defend, DrawDiscard

from enemies.enemy1 import FirstEnemy

from player import Player

from scenes.fight import Fight


def main():
    height = 720
    width = 1280
    display = pygame.display.set_mode((width, height))

    pygame.display.set_caption("random korttipeli idk")

    player_deck = PlayerDeck()

    for i in range(0, 6):
        player_deck.add_card(Slash())
        player_deck.add_card(Defend())
    player_deck.add_card(DrawDiscard())

    print(player_deck.cards)

    player = Player(100, player_deck)

    first_enemy = FirstEnemy()

    scene_manager = SceneManager()
    scene_manager.enter_scene(Fight(scene_manager, player, first_enemy))

    event_queue = EventQueue()
    clock = Clock()
    renderer = Renderer(display, scene_manager)

    main_loop = MainLoop(event_queue, clock, renderer)

    pygame.init()
    main_loop.start()


if __name__ == "__main__":
    main()
