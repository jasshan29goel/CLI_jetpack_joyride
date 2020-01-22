Welcome to Jetpack Joyride!
===================
*Coded by:*
**Jasshan Goel**

This **README** file contains :
 1. Information About the Game
 2. Rules of the Game
 3. Description of Classes Created
 4. Instructions on how to Run the Code
 5. Requirements

----------


About The Game
-------------

>**Jetpack Joyride** is a 2011 side-scrolling endless runner action video game created by Halfbrick Studios. The game features the same protagonist from Monster Dash, Barry Steakfries, who the player controls as he steals a jet pack from a top-secret laboratory. The game has been met with very favorable reviews, and has won numerous awards.  
For more information click [here](https://en.wikipedia.org/wiki/Jetpack_Joyride).

----------


Rules of the Game
-------------------

#### Aim:
> - You have a hero whom you can control and you have to cross the obstacles and reach the boss to defeat him
#### Hero:
> - You have 5 lives
> - You loose a life on colliding with the obstacle
> - You loose a life on getting hit by snowball of boss
> - You loose the game on touching the boss
> - You loose the game if the time gets over
#### Boss:
> - The boss has 19 lives
> - Life of boss decrease **ONLY** if he gets hit by the bullet in the eye
#### Shield:
> - There is a shield which can be used for 10 seconds in the game. once you use it you can only use it after 60 secs
#### Score:
> - Collect coins to increse your score +10
> - Fire bullets and decrease your score -1
> - Final score 10*coins - bullets + 2*time_left + 10*lives left
------------------------

Description of Classes Created
--------------------------------------------
#### Board:
The board class which contains the entire game. It is a 30*width_of_the_scree matrix. Board has the main while true loop of the game
#### Beams:
Beam like structures appear as obstacles. There
are three kinds of beams: horizontal, vertical and some at 45 ◦ with the ground/platform. The
hero must ensure to not collide with these beams, else he will lose a life. He can use his
blaster to shoot at them and clear his way.
#### Magnet:
A magnet appears on the way, which will influence the motion of the
hero. So if he is in the range of the magnet, he would be continuously attracted towards
the magnet.
#### Boss:
The boss enemy must appear in the end.The boss enemy a flying dragon that adjusts its
position according to the player. It throws ice balls aimed at the hero, which he must dodge.
#### Bullets and SnowBalls:
These are the weapons of the hero and the dragon respectivly.
__________________

How To Play:
------------------
>- Run the following code to start the game.
```
python3 run.py
```
>- Press enter to start the game.
>- 'w, a, d' use these controls for up, left, and right.
>- use 'b' to fire a bullet.
>- use 'p' to speed up the game.
>- press space bar for shield.
>- press 'q' to quit.

___________________

Reqiurements:
--------------------
- Python3

For Linux:
```
sudo apt-get update
sudo apt-get install python3
```
OOPS concepts
------------

The game exhibits the following features: 
- It demonstrates **Inheritance**. The horizontal vertical and slanting beam inherited from
the beam class.
- It demonstrates **Encapsulation** and **Abstraction**.Classes for each object in the
game has been made.
- It demonstrates **Polymorphism** as function overriding has been used in the slanting , vertical and horizontal beam classes. 

------------
File structure
--------------
```
.
+-- alarmexception.py
+-- ascii_art
│   +-- boss
+-- images
│   +-- gameplay.png     
│   +-- shield.png     
│   +-- boss.png     
│   +-- bullet.png     
+-- beam.py
+-- boss.py
+-- boy.py
+-- bullet.py
+-- coin.py
+-- done.txt
+-- game2.py
+-- game.py
+-- getChUnix.py
+-- magnet.py
+-- music
│   +-- naruto.mp3
│   +-- temp.mp3
+-- Readme.md
+-- snowBall.py
+-- temp
```


ScreenShots
------------

![Alt text](/images/gameplay.png?raw=true "Basic Game Play")
![Alt text](/images/shield.png?raw=true "Shield")
![Alt text](/images/boss.png?raw=true "Boss")
![Alt text](/images/bullet.png?raw=true "Boss")


Jasshan Goel
2018101014









