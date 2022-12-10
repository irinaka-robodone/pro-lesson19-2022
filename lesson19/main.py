#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
ev3.speaker.beep()

"""
# 今まで習った処理
- 条件分岐 if, else, elif
- ループ文 while, for
- 関数（定義と使用）
- 変数（定義と使用）
- 値の比較（==, <, >=)
"""

"""
以下の処理をするコードをかけ
1. 自分の年齢を変数に定義する(変数名はお好きに)
2. 年齢が12より大きいなら年齢の数だけbeep音を鳴らす(for文で繰り返す)
3. 年齢が12以下なら、1回だけbeep音を鳴らす
"""



def tosidake_narasu():
    your_age = 22
    if your_age > 12:
        for i in range(your_age):
            ev3.speaker.beep()
            wait(1000)
    else:
        ev3.speaker.beep()

tosidake_narasu()