import pygame
import pygame_manager as pm


class Selection(pm.states.State):
    """
    Menu de modification des paramètres de la partie
    """
    def __init__(self, width: int=1920, height: int=1080):
        super().__init__('selection')

        # surface
        self.surface_width = width
        self.surface_height = height
        self.surface = pygame.Surface((self.surface_with, self.surface_height))
        self.surface_rect = self.surface.get_rect()

        

    def init(self):
        """Chargement de l'état"""

    def update(self):
        """Actualisation par frame"""