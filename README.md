# Asteroid Field

## Simple asteroid avoiding game for the BBC micro:bit

I'm working on this game to learn a bit about MicroPython and physical computing but mainly just for fun. 

Currently is designed to work using external buttons for movement control and external leds to show remaining lifes; check below

### Repo content

#### /

|File|Description|
|----|-----------|
|main.py|Game "stable version"|
|asteroid.py| Functions required for the game (tested)  |
|characters.py|Classes for the game (tested)| 
|README.md| This document |

#### /noExternal

To be added .... Version to play without external buttons and leds, this version uses button A and B to navigate the ship, so to restart micro:bit must be reseted

#### /testZone

|File|Description|
|----|-----------|
|asteroid_b.py | All tested and untested functions  |
|characters_b.py |All tested and untested classes | 
|other .py files |testing scripts |
|README.md | dev notes  |

### Required circuit

For this part you will need an adaptor to access all GPIO pins to the micro:bit

- If you are using micro:bit V2 you don't need an external buzzer
- Buttons a and b are redirected to the breadboard altough that is completely optional

![asteroid_game](https://user-images.githubusercontent.com/13229623/172957446-c6aced09-d06d-4ead-952c-e9421b65b825.png)

