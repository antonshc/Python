#!/usr/bin/python3
# -*- coding: utf-8 -*-
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")

print(list(range(5, 90, 2)))
tess.up()                     # this is new
for size in range(5, 90, 2):    # start with size = 5 and grow by 2
    tess.stamp()                # leave an impression on the canvas
    tess.forward(size)          # move tess along
    tess.right(20)              # and turn her

wn.exitonclick()