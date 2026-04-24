"""
App - Main application class
"""

import pygame
from src.constants import WINDOW_WIDTH, WINDOW_HEIGHT, FPS
from src.scenes.gameplay_scene import GameplayScene


class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        self.running = False

        # Scenes
        self.scenes = {}
        self.current_scene_name = None
        self.current_scene = None

        # Register scenes
        self._register_scenes()

        # Start with menu scene (for now, start directly with gameplay for MVP)
        self.change_scene("gameplay")

    def _register_scenes(self):
        """Register all available scenes"""
        self.scenes["gameplay"] = GameplayScene(self)
        self.scenes["menu"] = None  # Will be added in Sprint 2

    def change_scene(self, scene_name):
        """Switch to a different scene"""
        if scene_name in self.scenes:
            self.current_scene_name = scene_name
            if scene_name == "gameplay" and self.scenes["gameplay"] is None:
                self.scenes["gameplay"] = GameplayScene(self)
            self.current_scene = self.scenes[scene_name]

    def run(self):
        """Main game loop"""
        self.running = True
        while self.running:
            current_time = pygame.time.get_ticks()

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif self.current_scene:
                    self.current_scene._handle_event(event)

            # Update current scene
            if self.current_scene:
                self.current_scene.update(current_time)

            # Render current scene
            if self.current_scene:
                self.current_scene.render(self.screen)

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()

    def stop(self):
        """Stop the game loop"""
        self.running = False
