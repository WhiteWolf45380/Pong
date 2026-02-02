# ======================================== IMPORTS ========================================
import sys

# ======================================== GESTIONNAIRE ========================================
class ContextManager:
    """
    Context Manager
    """
    def __init__(self):
        # Menus
        self.main = None
        self.modes = None
        self.modifiers = None

        # Jeu
        self.game = None

    def __getattr__(self, name):
        raise AttributeError(f"context has no attribute {name!r}")

# ======================================== CLASSE MODULAIRE ========================================
sys.modules[__name__] = ContextManager()