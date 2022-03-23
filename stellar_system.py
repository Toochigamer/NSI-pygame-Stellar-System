#! /usr/bin/env python3

import pygame
import sys
import json
from corpsceleste import CorpsCeleste
from vaisseau import Vaisseau

global FPSCLOCK
FPS = 120
WINDOWWIDTH = 1800
WINDOWHEIGHT = 900
ARRIERE_PLAN = (13,13,25)


class Quitte(Exception ):
    pass

def isQuitEvent(event):
    return (event.type == pygame.QUIT or 
            (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE))


def handleEvents():
    for event in pygame.event.get():
        # pour chaque évènement depuis le dernier appel de cette fonction
        if isQuitEvent(event):
            raise Quitte


def drawApp(s_temp, s_pers, ecran, univers):
    """
    Redessine l'écran.
    """
    s_temp.fill((0,0,0,0)) # on remplit avec du transparent
    for objet in univers:
        objet.dessine(s_pers, s_temp)
    ecran.fill(ARRIERE_PLAN)
    ecran.blit(s_pers, (0,0))
    ecran.blit(s_temp, (0,0))
    pygame.display.update()
    
def main():
    temps = 0
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('SpaceX')
    ecran = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    s_pers = pygame.Surface((WINDOWWIDTH, WINDOWHEIGHT), pygame.SRCALPHA)
    s_temp = pygame.Surface((WINDOWWIDTH, WINDOWHEIGHT), pygame.SRCALPHA)
    
    ####################################################################
    ## VOTRE TRAVAIL COMMENCE ICI 
    ####################################################################
    WinW=WINDOWWIDTH
    WinH=WINDOWHEIGHT

    etoile1 = CorpsCeleste(30, 0, (WinW/2,WinH/2), 0, (255, 255, 255))
    planete1 = CorpsCeleste(20, 100, (0,0), 10, (0,255,0), True, 1000)
    planete2 = CorpsCeleste(40, 150, (WinW/2,WinH/2), 5, (255,0,0), True, 500)
    planete3 = CorpsCeleste(20, 100, (1800,0), 10, (253,63,146), True, 750)

    univers = [etoile1, planete1, planete2, planete3]

    ####################################################################
    ## VOTRE TRAVAIL SE TERMINE ICI 
    ####################################################################

    ## etoile1 = Soleil
    
    ecran.fill(ARRIERE_PLAN)

    while True:  #boucle principale
        try:
            handleEvents()
            drawApp(s_temp, s_pers, ecran, univers)

            temps_ecoule = FPSCLOCK.tick(FPS)
            for objet in univers:
                objet.avance(temps_ecoule)

        except Quitte:
            break
            
    pygame.quit()
    sys.exit(0)

main()
 
