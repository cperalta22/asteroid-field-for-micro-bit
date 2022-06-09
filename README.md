# Asteroid Field

## Simple asteroid avoiding game for the BBC micro:bit

I'm working on this game to learn a bit about MicroPython and physical computing but mainly just for fun. 

There are **2 versions of the game**; version in root directory requires an external breadboard and buttons (see below) and /noExternal version, that only requires a micro:bit

### Repo content

#### /

|File|Description|
|----|-----------|
|main.py|Game "stable version"|
|asteroid.py| Functions required for the game (tested)  |
|characters.py|Classes for the game (tested)| 
|README.md| This document |

#### /noExternal

Version to play without external buttons and leds, this version uses button A and B to navigate the ship, so to restart micro:bit must be reseted

|File|Description|
|----|-----------|
|main.py|Game "stable noExternal version"|
|asteroid.py| Functions required for the game (tested)  |
|characters.py|Classes for the game (tested)| 

#### /testZone

Development test and experimental funtions and classes

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

