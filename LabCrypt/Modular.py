def gcd(a, b):
  while b:
      a, b = b, a % b
  return a
def mod_inverse(a, m):
  g, x, y = extended_gcd(a, m)
  if g != 1:
      return None
  else:
      return x % m
def extended_gcd(a, b):
  if a == 0:
      return (b, 0, 1)
  else:
      g, x, y = extended_gcd(b % a, a)
      return (g, y - (b // a) * x, x)
def solve_modular_equation(a, b, m):
  common_divisor = gcd(a, m)

  if b % common_divisor != 0:
      return None

  a_mod = a // common_divisor
  m_mod = m // common_divisor
  a_inverse_mod = mod_inverse(a_mod, m_mod)

  x_0 = (a_inverse_mod * (b // common_divisor)) % m_mod

  solutions = [(x_0 + k * m_mod) for k in range(common_divisor)]

  return solutions[0]