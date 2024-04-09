# direct inputs
# source to this solution and code:
# http://stackoverflow.com/questions/14489013/simulate-python-keypresses-for-controlling-a-game

# find keys here
# https://gist.github.com/dretax/fe37b8baf55bc30e9d63

import ctypes
import time

SendInput = ctypes.windll.user32.SendInput


A = 0x1E
B = 0x30
C = 0x2E
D = 0x20
E = 0x12
F = 0x21
G = 0x22
H = 0x23
I = 0x17
J = 0x24
K = 0x25
L = 0x26
M = 0x32
N = 0x31
O = 0x18
P = 0x19
Q = 0x10
R = 0x13
S = 0x1F
T = 0x14
U = 0x16
V = 0x2F
W = 0x11
X = 0x2C
Y = 0x15
Z = 0x2C
CTRL = 0x1D
SPACE = 0x39
ENTER  = 0x1C
SPACE = 0x39
ONE = 0x02
#key pad arrow keys num lock can mess it up
UP_ARROW = 0xC8
DOWN_ARROW = 0xD0
RIGHT_ARROW = 0xCD
LEFT_ARROW = 0xCB
ALT = 0x38 #LEFT ALT
TAB = 0x0F
LSHIFT = 0x2A
MINUS = 0x0C


# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def PR(hexKeyCode , delay = 0.05):
    PressKey(hexKeyCode)
    time.sleep(delay)
    ReleaseKey(hexKeyCode)


def enter(delay=0.02):
    PressKey(ENTER)
    time.sleep(delay)
    ReleaseKey(ENTER)


def paste(delay=0.02):
    PressKey(CTRL)
    PressKey(V)
    time.sleep(delay)
    ReleaseKey(CTRL)
    ReleaseKey(V)


def shift_min(delay=0.02):
    PressKey(LSHIFT)
    PressKey(MINUS)
    time.sleep(delay)
    ReleaseKey(LSHIFT)
    ReleaseKey(MINUS)

def WASD(dir,delay = 0.02,mode = "Arrow"):
    if mode == "Arrow":
        if dir == 'U':
            PR(UP_ARROW,delay)
        elif dir == 'R':
            PR(RIGHT_ARROW,delay)
        elif dir == 'D':
            PR(DOWN_ARROW,delay)
        elif dir == 'L':
            PR(LEFT_ARROW,delay)


def twokeys():
    pass

# I only learned that pyauto gui had the write function after I wrote this :(
def typeing(word,delay=0.1):
    for i in word:
        if i == 'a':
            PressKey(A)
            time.sleep(delay)
            ReleaseKey(A)
        elif i == 'b':
            PressKey(B)
            time.sleep(delay)
            ReleaseKey(B)
        elif i == 'c':
            PressKey(C)
            time.sleep(delay)
            ReleaseKey(C)
        elif i == 'd':
            PressKey(D)
            time.sleep(delay)
            ReleaseKey(D)
        elif i == 'e':
            PressKey(E)
            time.sleep(delay)
            ReleaseKey(E)
        elif i == 'f':
            PressKey(F)
            time.sleep(delay)
            ReleaseKey(F)
        elif i == 'g':
            PressKey(G)
            time.sleep(delay)
            ReleaseKey(G)
        elif i == 'h':
            PressKey(H)
            time.sleep(delay)
            ReleaseKey(H)
        elif i == 'i':
            PressKey(I)
            time.sleep(delay)
            ReleaseKey(I)
        elif i == 'j':
            PressKey(J)
            time.sleep(delay)
            ReleaseKey(J)
        elif i == 'k':
            PressKey(K)
            time.sleep(delay)
            ReleaseKey(K)
        elif i == 'l':
            PressKey(L)
            time.sleep(delay)
            ReleaseKey(L)
        elif i == 'm':
            PressKey(M)
            time.sleep(delay)
            ReleaseKey(M)
        elif i == 'n':
            PressKey(N)
            time.sleep(delay)
            ReleaseKey(N)
        elif i == 'o':
            PressKey(O)
            time.sleep(delay)
            ReleaseKey(O)
        elif i == 'p':
            PressKey(P)
            time.sleep(delay)
            ReleaseKey(P)
        elif i == 'q':
            PressKey(Q)
            time.sleep(delay)
            ReleaseKey(Q)
        elif i == 'r':
            PressKey(R)
            time.sleep(delay)
            ReleaseKey(R)
        elif i == 's':
            PressKey(S)
            time.sleep(delay)
            ReleaseKey(S)
        elif i == 't':
            PressKey(T)
            time.sleep(delay)
            ReleaseKey(T)
        elif i == 'u':
            PressKey(U)
            time.sleep(delay)
            ReleaseKey(U)
        elif i == 'v':
            PressKey(V)
            time.sleep(delay)
            ReleaseKey(V)
        elif i == 'w':
            PressKey(W)
            time.sleep(delay)
            ReleaseKey(W)
        elif i == 'x':
            PressKey(X)
            time.sleep(delay)
            ReleaseKey(X)
        elif i == 'y':
            PressKey(Y)
            time.sleep(delay)
            ReleaseKey(Y)
        elif i == 'z':
            PressKey(Z)
            time.sleep(delay)
            ReleaseKey(Z)
        elif i == ' ':
            PressKey(SPACE)
            time.sleep(delay)
            ReleaseKey(SPACE)

        
if __name__ == '__main__':
    time.sleep(2)
    ReleaseKey(M)
    WASD("D",1)
    WASD("U",1)
    WASD("L",1)
    WASD("R",1)
    '''
    while True:
        PressKey(M)

    '''
