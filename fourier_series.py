import numpy as np
import matplotlib.pyplot as plt

def ctfs(x, N):
    ak = np.zeros(N + 1, dtype=complex)
    TO = len(x)
    t = np.arange(TO)
    for k in range(N + 1):
        Ak = (2 / TO) * np.sum(x * np.cos(2 * np.pi * k * t / TO))
        Bk = (2 / TO) * np.sum(x * np.sin(2 * np.pi * k * t / TO))
        ak[k] = Ak / 2 - 1j * Bk / 2
    return ak

x1 = lambda t: t * ((t >= 0) & (t < 1)) + (2 - t) * ((t >= 1) & (t < 2))
Ts = 1 / 10000
t = np.arange(-0.25, 2.25, Ts)  # Time for one period
tp = np.arange(0, 1, Ts)
ak = ctfs(x1(tp), 20)
mag = abs(ak)
ang = np.angle(ak)

fig, axes = plt.subplots(2, 2, figsize=(8, 8))
fig.delaxes(axes[0, 1])
axes[0, 0].plot(t, x1(t))
axes[0, 0].grid()
axes[0, 0].set_xlabel('time[sec]')
axes[0, 0].set_ylabel('Amplitude')
axes[1, 0].plot(mag)
axes[1, 0].grid()
axes[1, 0].set_xlabel('k')
axes[1, 0].set_ylabel('Magnitude')
axes[1, 1].plot(ang)
axes[1, 1].grid()
axes[1, 1].set_xlabel('k')
axes[1, 1].set_ylabel('Angle')
plt.show()
