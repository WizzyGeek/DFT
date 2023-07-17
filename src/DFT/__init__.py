from cmath import exp, tau
from numbers import Complex


def dft(signal: list[Complex]) -> list[complex]:
    ret: list[complex] = []
    for k in range(len(signal)):
        resp = 0 + 0j
        for n, x in enumerate(signal):
            resp += x * exp(-1j * tau * k * n / len(signal))
        ret.append(resp)
    return ret

def idft(freq: list[Complex]) -> list[complex]:
    ret: list[complex] = []
    for n in  range(len(freq)):
        amp = 0 + 0j
        for k, X in enumerate(freq):
            amp += X * exp(1j * tau * k * n / len(freq))
        ret.append(amp / len(freq))

    return ret
