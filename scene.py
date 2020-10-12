import pygame

class SceneBase:
    """ Parent class for Scenes
    """

    def __init__(self):
        self.next = self

    def process_input(self, events):
        pass

    def update(self):
        pass

    def render(self, screen: pygame.Surface):
        pass

    def switch_to_scene(self, next_scene):
        self.next = next_scene

    def terminate(self):
        self.switch_to_scene(None)


class TitleScene(SceneBase):
    def process_input(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # Move to the next scene when the user pressed Space
                self.switch_to_scene(GameScene())

    def update(self):
        pass

    def render(self, screen: pygame.Surface):
        super().render(screen)


class GameScene(SceneBase):
    def process_input(self, events):
        pass

    def update(self):
        pass

    def render(self, screen: pygame.Surface):
        # The game scene is just a blank blue screen
        super().render(screen)
