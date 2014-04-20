"""Color processing."""


def MakeColorTuple(hc):
  R, G, B = hc[1:3], hc[3:5], hc[5:7]
  R, G, B = int(R, 16), int(G, 16), int(B, 16)
  return R, G, B


def IntermediateColor(startcol, targetcol, frac):
  """Return an intermediate color.

  Fraction can be any rational number, but only the 0-1 range produces
  gradients.
  """
  if frac < 0:
    frac = 0
  if frac >= 1.0:
    frac = 1.0
  sc = MakeColorTuple(startcol)
  tc = MakeColorTuple(targetcol)
  dR = tc[0] - sc[0]
  dG = tc[1] - sc[1]
  dB = tc[2] - sc[2]
  R = sc[0] + dR * frac
  G = sc[1] + dG * frac
  B = sc[2] + dB * frac
  return "#%02x%02x%02x" % (R, G, B)
