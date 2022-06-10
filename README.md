# Asteroid Field

## Simple asteroid avoiding game for the BBC micro:bit

I'm working on this game to learn a bit about MicroPython and physical computing but mainly just for fun. 

There are **2 versions of the game**; version in root directory requires an external breadboard and buttons (see below) and /noExternal version, that only requires a micro:bit

### Index
- **Game Instructions
- **Installation
- **Files and directories of this repo
- **Required hardware

### Game Instructions

You are piloting a space ship into a field of asteroids, your goal is to dodge all asteroids as your ship accelerates

- use external buttons wired to pin 1 and 2 to move left and right
- every 25 asteroids speed will increase up to level 6 
- if you complete level 6 you will exit the asteroid field into safety
- whenever you complete a level you will get access to a missile, an indicator light will go on
- you can't have more than one missile at any time
- fire with button B to destroy all asteroids in sight, you will get a new missile at the next level up
- get points for every dodged asteroid and bonus for level, remaining lifes and unused missile (the more you travel without firing the missile more points you'll get
- game ends when you crash tree times or you complete all the levels
- you can start a new game pressing button A whenever a game is not in progress

Good luck pilot!

### Installation

1 - clone this repo or copy all three python scripts of the desired version you want to play
2 - go to beta version of the official web [micropython editor](https://python.microbit.org/v/beta)
3 - use the connect button to pair your micro:bit 
4 - click into **Project** and upload all three files
5 - flash **Asteroid field** into your micro:bit
6 - Don't forget to build the controller ! (look below this document for an schematic) 

### Files and directories of this repo

#### /

|File|Description|
|----|-----------|
|main.py|Game "stable version"|
|asteroid.py| Functions required for the game (tested)  |
|characters.py|Classes for the game (tested)| 
|README.md| This document |

#### /noExternal

Version to play without external buttons and leds, this version uses button A and B to navigate the ship, so to restart micro:bit must be reseted

**Current version does not have missile included and score system is different to "main" version"

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

### Required hardware

For this part you will need an adaptor to access all GPIO pins to the micro:bit

- If you are using micro:bit V2 you don't need an external buzzer
- Buttons a and b are redirected to the breadboard altough that is completely optional

#### Components
   - micro:bit (any version should work)
   - breadboard
   - 4 push buttons
   - micro:bit breadboard adapter
   - 4 leds
   - jumper cables
   - passive buzzer

![asteroid_game](https://user-images.githubusercontent.com/13229623/172957446-c6aced09-d06d-4ead-952c-e9421b65b825.png)

