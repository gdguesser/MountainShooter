#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        if self.name == 'Enemy3':
            self.rect.centerx -= ENTITY_SPEED[self.name]
        
            # Movimento vertical especial para Enemy3
            if not hasattr(self, 'moving_up'):
                self.moving_up = False
                self.vertical_speed = ENTITY_SPEED[self.name]
            
            if self.moving_up:
                self.rect.centery -= self.vertical_speed
                if self.rect.top <= 0:  # Bateu no topo
                    self.moving_up = False
                    self.vertical_speed = ENTITY_SPEED[self.name] * 2  # Velocidade dupla ao descer
            else:
                self.rect.centery += self.vertical_speed
                if self.rect.bottom >= WIN_HEIGHT:  # Bateu no fundo
                    self.moving_up = True
                    self.vertical_speed = ENTITY_SPEED[self.name]  # Velocidade normal ao subir
        else:
            self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
