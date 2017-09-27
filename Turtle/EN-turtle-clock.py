#!/usr/bin/python3
# -*- coding: utf-8 -*-
import turtle

wn = turtle.Screen()
wn.bgcolor("blue")
wn.title("Muz Cumhuriyeti")  # in Turkish that means Republic of Banana
jose = turtle.Turtle()
jose.shape("turtle")
jose.color("red")
jose.penup()
jose.speed(1)

for size in range(12):
	jose.forward(70)
	jose.down()
	jose.forward(15)
	jose.up()
	jose.forward(15)
	jose.stamp()
	jose.forward(-100)
	jose.right(30)

wn.exitonclick()