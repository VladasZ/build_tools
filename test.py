#!/usr/bin/python
# Compute the position of a Lighthouse given
# sensor readings in a known configuration.

from sympy import *
from sympy import solve_poly_system
from math import pi
from sys import stdin

import Time

Time.stamp()

# The few vector math functions that we need
def cross(a, b):
	return [
		a[1]*b[2] - a[2]*b[1],
		a[2]*b[0] - a[0]*b[2],
		a[0]*b[1] - a[1]*b[0]
	]

def vecmul(a, k):
	return [
		a[0]*k,
		a[1]*k,
		a[2]*k
	]
def vecsub(a, b):
	return [
		a[0] - b[0],
		a[1] - b[1],
		a[2] - b[2]
	]

def dot(a, b):
	return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

def len(a):
	return sqrt(dot(a,a))

def unitv(a):
	mag = len(a)
	return [a[0]/mag, a[1]/mag, a[2]/mag]

def ray(a1,a2):
	#print "a1=", a1*180/pi
	#print "a2=", a2*180/pi

	# Normal to X plane
	plane1 = [+cos(a1), 0, -sin(a1)]
	# Normal to Y plane
	plane2 = [0, +cos(a2), +sin(a2)]

	# Cross the two planes to get the ray vector
	return unitv(cross(plane2,plane1))

def tick2angle(a):
	return pi * (a - 4000) / 8333


# The default sensor array is 22mm square
# This fits easily on a breadboard.

pos = [
	[+100, -100, 65],
	[-100, -100, 65],
	[-100, +100, 65],
	[+100, +100, 65],
]

# Compute the distances between each of the sensors
r01 = N(len(vecsub(pos[0],pos[1])))
r02 = N(len(vecsub(pos[0],pos[2])))
r03 = N(len(vecsub(pos[0],pos[3])))
r12 = N(len(vecsub(pos[1],pos[2])))
r13 = N(len(vecsub(pos[1],pos[3])))
r23 = N(len(vecsub(pos[2],pos[3])))


# Translate them into angles, compute each ray vector for each sensor
# and then compute the angles between them
def lighthouse_pos(samples,id):
	v0 = ray(tick2angle(samples[0][id*2]), tick2angle(samples[0][id*2+1]))
	v1 = ray(tick2angle(samples[1][id*2]), tick2angle(samples[1][id*2+1]))
	v2 = ray(tick2angle(samples[2][id*2]), tick2angle(samples[2][id*2+1]))
	v3 = ray(tick2angle(samples[3][id*2]), tick2angle(samples[3][id*2+1]))

	v01 = dot(v0,v1)
	v02 = dot(v0,v2)
	v03 = dot(v0,v3)
	v12 = dot(v1,v2)
	v13 = dot(v1,v3)
	v23 = dot(v2,v3)

	#print "v0=", v0
	#print "v1=", v1
	#print "v2=", v2
	#print "v3=", v3
	print("v01=", acos(v01) * 180/pi, " deg")
	print("v02=", acos(v02) * 180/pi, " deg")
	print("v03=", acos(v03) * 180/pi, " deg")
	print("v12=", acos(v12) * 180/pi, " deg")
	print("v13=", acos(v13) * 180/pi, " deg")
	print("v23=", acos(v23) * 180/pi, " deg")

	k0, k1, k2, k3 = symbols('k0, k1, k2, k3')

	sol = nsolve((
		k0**2 + k1**2 - 2*k0*k1*v01 - r01**2,
		k0**2 + k2**2 - 2*k0*k2*v02 - r02**2,
		k0**2 + k3**2 - 2*k0*k3*v03 - r03**2,
		k2**2 + k1**2 - 2*k2*k1*v12 - r12**2,
		k3**2 + k1**2 - 2*k3*k1*v13 - r13**2,
		k2**2 + k3**2 - 2*k2*k3*v23 - r23**2,
	),
		(k0, k1, k2, k3),
		(1000,1000,1000,1000),
		verify=False  # ignore tolerance of solution
	)

	#print sol

	p0 = vecmul(v0,sol[0])
	p1 = vecmul(v1,sol[1])
	p2 = vecmul(v2,sol[2])
	p3 = vecmul(v3,sol[3])

	print("p0=", p0)
	print("p1=", p1)
	print("p2=", p2)
	print("p3=", p3)

	# compute our own estimate of the error
	print("err01=", len(vecsub(p0,p1)) - r01, " mm")
	print("err02=", len(vecsub(p0,p2)) - r02, " mm")
	print("err03=", len(vecsub(p0,p3)) - r03, " mm")
	print("err12=", len(vecsub(p1,p2)) - r12, " mm")
	print("err13=", len(vecsub(p1,p3)) - r13, " mm")
	print("err23=", len(vecsub(p2,p3)) - r23, " mm")

  
 
samples = [
	[3986, 2156, 4421, 2612],
	[4033, 2274, 4346, 2485],
	[3807, 2291, 4628, 2434],
	[3742, 2176, 4678, 2567],
]


print(samples)

lighthouse_pos(samples, 0)
lighthouse_pos(samples, 1)

print(Time.duration())
