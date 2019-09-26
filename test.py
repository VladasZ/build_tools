#!/usr/bin/python
# Compute the position of a Lighthouse given
# sensor readings in a known configuration.

import sympy
from math import pi
from sys import stdin

import Time

Time.stamp()


# The few vector math functions that we need
def cross(a, b):
    return [
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0]
    ]


def vector_multiply(a, k):
    return [
        a[0] * k,
        a[1] * k,
        a[2] * k
    ]


def vector_subtract(a, b):
    return [
        a[0] - b[0],
        a[1] - b[1],
        a[2] - b[2]
    ]


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def vector_len(a):
    return sympy.sqrt(dot(a, a))


def normalize(a):
    mag = vector_len(a)
    return [a[0] / mag, a[1] / mag, a[2] / mag]


def ray(a1, a2):
    # print "a1=", a1*180/pi
    # print "a2=", a2*180/pi

    print("a1: " + str(a1))
    print("a2: " + str(a2))

    # Normal to X plane
    plane1 = [+sympy.cos(a1), 0, -sympy.sin(a1)]
    # Normal to Y plane
    plane2 = [0, +sympy.cos(a2), +sympy.sin(a2)]

    # Cross the two planes to get the ray vector
    return normalize(cross(plane2, plane1))


def tick2angle(a):
    print("angle: " + str(a))
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
r01 = sympy.N(vector_len(vector_subtract(pos[0], pos[1])))
r02 = sympy.N(vector_len(vector_subtract(pos[0], pos[2])))
r03 = sympy.N(vector_len(vector_subtract(pos[0], pos[3])))
r12 = sympy.N(vector_len(vector_subtract(pos[1], pos[2])))
r13 = sympy.N(vector_len(vector_subtract(pos[1], pos[3])))
r23 = sympy.N(vector_len(vector_subtract(pos[2], pos[3])))


# Translate them into angles, compute each ray vector for each sensor
# and then compute the angles between them
def lighthouse_pos(samples, id):
    v0 = ray(tick2angle(samples[0][id * 2]), tick2angle(samples[0][id * 2 + 1]))
    v1 = ray(tick2angle(samples[1][id * 2]), tick2angle(samples[1][id * 2 + 1]))
    v2 = ray(tick2angle(samples[2][id * 2]), tick2angle(samples[2][id * 2 + 1]))
    v3 = ray(tick2angle(samples[3][id * 2]), tick2angle(samples[3][id * 2 + 1]))

    print(v0)
    print(v1)
    print(v2)
    print(v3)

    v01 = dot(v0, v1)
    v02 = dot(v0, v2)
    v03 = dot(v0, v3)
    v12 = dot(v1, v2)
    v13 = dot(v1, v3)
    v23 = dot(v2, v3)

    # print "v0=", v0
    # print "v1=", v1
    # print "v2=", v2
    # print "v3=", v3
    print("v01=", sympy.acos(v01) * 180 / pi, " deg")
    print("v02=", sympy.acos(v02) * 180 / pi, " deg")
    print("v03=", sympy.acos(v03) * 180 / pi, " deg")
    print("v12=", sympy.acos(v12) * 180 / pi, " deg")
    print("v13=", sympy.acos(v13) * 180 / pi, " deg")
    print("v23=", sympy.acos(v23) * 180 / pi, " deg")

    k0, k1, k2, k3 = sympy.symbols('k0, k1, k2, k3')

    sol = sympy.nsolve((
        k0 ** 2 + k1 ** 2 - 2 * k0 * k1 * v01 - r01 ** 2,
        k0 ** 2 + k2 ** 2 - 2 * k0 * k2 * v02 - r02 ** 2,
        k0 ** 2 + k3 ** 2 - 2 * k0 * k3 * v03 - r03 ** 2,
        k2 ** 2 + k1 ** 2 - 2 * k2 * k1 * v12 - r12 ** 2,
        k3 ** 2 + k1 ** 2 - 2 * k3 * k1 * v13 - r13 ** 2,
        k2 ** 2 + k3 ** 2 - 2 * k2 * k3 * v23 - r23 ** 2,
    ),
        (k0, k1, k2, k3),
        (1000, 1000, 1000, 1000),
        verify=False  # ignore tolerance of solution
    )

    # print sol

    p0 = vector_multiply(v0, sol[0])
    p1 = vector_multiply(v1, sol[1])
    p2 = vector_multiply(v2, sol[2])
    p3 = vector_multiply(v3, sol[3])

    print("p0=", p0)
    print("p1=", p1)
    print("p2=", p2)
    print("p3=", p3)

    # compute our own estimate of the error
    print("err01=", vector_len(vector_subtract(p0, p1)) - r01, " mm")
    print("err02=", vector_len(vector_subtract(p0, p2)) - r02, " mm")
    print("err03=", vector_len(vector_subtract(p0, p3)) - r03, " mm")
    print("err12=", vector_len(vector_subtract(p1, p2)) - r12, " mm")
    print("err13=", vector_len(vector_subtract(p1, p3)) - r13, " mm")
    print("err23=", vector_len(vector_subtract(p2, p3)) - r23, " mm")


samples = [
    [3986, 2156, 4421, 2612],
    [4033, 2274, 4346, 2485],
    [3807, 2291, 4628, 2434],
    [3742, 2176, 4678, 2567],
]

lighthouse_pos(samples, 0)
lighthouse_pos(samples, 1)

print(Time.duration())
