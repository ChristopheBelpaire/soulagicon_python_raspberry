import os, pygame
from pygame.locals import *

screen = pygame.display.set_mode((468, 60))
pygame.display.set_caption('Monkey Fever')
pygame.mouse.set_visible(0)
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=32)
pygame.init()



class Soulagicon():
  IDLE = "Idle"
  SHOOT_READY = "Shoot ready"
  
  COIN = "Coin"
  SHOOT = "Shoot"

  sentences_files = []
  sentences_position = 0

  def __init__(self):
    self.shboing = pygame.mixer.Sound("shboing.wav")
    self.status = Soulagicon.IDLE
    for dirname, dirnames, filenames in os.walk('./sentences'):
      for filename in filenames:
        if filename.endswith('.wav'):
          self.sentences_files.append('./sentences/'+filename)
  
  def handle_event(self, event):
    if (self.status == Soulagicon.IDLE):
      if (event == Soulagicon.COIN):
        self.play_sentence()
        self.status = Soulagicon.SHOOT_READY
    elif (self.status == Soulagicon.SHOOT_READY):
      if(event == Soulagicon.SHOOT):
        self.sentence.stop()
        self.shboing.play()
        self.status = Soulagicon.IDLE

  def play_sentence(self):
    self.sentence =pygame.mixer.Sound(self.sentences_files[self.sentences_position])
    self.sentence.play()
    self.sentences_position = (self.sentences_position +1) % len(self.sentences_files)

def main():
  soulagicon = Soulagicon()  
  while 1:
    for event in pygame.event.get():
      if event.type == QUIT:
        return
      elif event.type == KEYDOWN and event.key == K_ESCAPE:
        return
      elif event.type == KEYDOWN:
        if event.key == K_a:
          soulagicon.handle_event(Soulagicon.COIN)
        elif event.key == K_z:
          soulagicon.handle_event(Soulagicon.SHOOT)
if __name__ == '__main__': main()      