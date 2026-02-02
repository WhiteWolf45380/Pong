# ======================================== IMPORTS ========================================
import pygame
import pygame_manager as pm
from ._view import GameView
from .objects._ball import Ball
from .objects._paddle import Paddle

# ======================================== ETAT ========================================
class Game(pm.states.State):
    """
    Une partie de jeu
    """
    def __init__(self):
        super().__init__('game')

        # panel de vue du jeu
        self.view = GameView()
        self.bind_panel(self.view)

        # temporaire
        self.game_mode = 2

        # lancement de la partie
        self.game_frozen = True
        def toggle_freeze(self):
            self.game_frozen = not self.game_frozen
        pm.inputs.add_listener(pygame.K_SPACE, toggle_freeze, args=[self])

        # objets
        self.ball = None    # balle
        self.paddles = []   # raquettes

        # wall game
        self.score = 0

    def init(self):
        """Initialisation d'une partie"""
        # balle
        self.ball = Ball()

        # raquettes
        offset = 50
        self.paddles.append(Paddle(offset, self.surface_rect.height / 2, up=pygame.K_z, down=pygame.K_s))
        if self.game_mode == 2:
            self.paddles.append(Paddle(self.surface_rect.width - offset, self.surface_rect.height / 2, up=pygame.K_UP, down=pygame.K_DOWN))
        
        pm.states.activate("game") 
        return self

    def update(self):
        """Actualisation de la frame"""
        # jeu en pause
        if self.game_frozen:
            return

    def end(self, result: int=0):
        """
        Fin de partie

        Args:
            winner (int) : le gagnant
        """
        if self.game_mode == 1:
            print(f"Score : {result}")
        else:
            print(f"Le gagnant est le joueur {result}")
        pm.stop()