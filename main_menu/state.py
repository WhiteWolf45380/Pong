# ======================================== IMPORTS ========================================
import pygame_manager as pm

# ======================================== ETAT ========================================
class MainMenuState(pm.states.State):
    """
    Menu principal
    """
    def __init__(self):
        super().__init__('main_menu')
    
    def init(self):
        """Chargement de l'état"""

    def update(self):
        """Actualisation par frame"""