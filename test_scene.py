import pytest
import pygame
import scene

def test_title_scene_transition():
    t_scene = scene.TitleScene()
    assert isinstance(t_scene.next, scene.TitleScene)
    t_event = pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_SPACE})
    t_scene.process_input([t_event])
    assert isinstance(t_scene.next, scene.GameScene)
