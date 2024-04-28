import math

# Verilen değerler
f = 1e6  # Frekans (1 MHz)
E = 1  # Enerji (1 Joule)
c = 3e8  # Işık hızı (m/s)
G = 6.674e-11  # Kütleçekim sabiti (m^3/kg/s^2)
lambd = 1.616e-35  # Planck uzunluğu (m)

# Genlik hesaplama
h = math.sqrt((32 * math.pi * G * E) / (c**3 * f**2 * lambd**2))

print("Genlik (h) ≈", h)
