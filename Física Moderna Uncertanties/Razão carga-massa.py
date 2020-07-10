"""
- Lab. Física Moderna: cálculos da razão carga-massa
* Bobinas de Helmholtz

Autor: Thiago Ferreira Santos <thiagoferresan@gmail.com>

License: MIT License (https://opensource.org/licenses/MIT)
"""

from uncertainties import *
from uncertainties import unumpy

# permissividade elétrica no vácuo
u0 = 1.26e-6

# raio do arranjo de Helmholtz com duas bobinas: 0.20 m
R = 0.20

# número de espiras
n = 154

# raios da trajetória do elétron
r1 = 0.02

r2 = 0.03

r3 = 0.04

r4 = 0.05

# potencial elétrico para a configuração r1
U1vetor = unumpy.uarray([100, 120, 140, 160, 180, 200, 220, 240, 260],[0.8, 0.9, 1, 1, 1, 1, 1, 2, 2])

# corrente elétrica para a configuração r1
I1vetor = unumpy.uarray([2.16, 2.64, 2.95, 3.07, 3.3, 3.5, 3.8, 4, 4],[0.27, 0.28, 0.29, 0.29, 0.3, 0.3, 0.3, 0.3, 0.3])

# campo magnético para a configuração r1
B1vetor = ((4/5)**(3/2))*u0*n*(I1vetor/R)
for x in B1vetor:
    print("{0:.2e} T".format(x))

# razão carga-massa para a configuração r1
carga_massa = 2*U1vetor/((r1*B1vetor)**2)
for x in carga_massa:
    print("{0:.2e} As/kg".format(x))

# potencial elétrico para a configuração r2
U2vetor = unumpy.uarray([100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300],[0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 2, 2, 2, 2])

# corrente elétrica para a configuração r2
I2vetor = unumpy.uarray([1.60, 1.62, 1.84, 2.02, 2.17, 2.33, 2.43, 2.50, 2.65, 2.79, 2.87],[0.25, 0.25, 0.26, 0.26, 0.27, 0.27, 0.27, 0.27, 0.28, 0.28, 0.29])

# campo magnético para a configuração r2
B2vetor = ((4/5)**(3/2))*u0*n*(I2vetor/R)
for x in B2vetor:
    print("{0:.2e} T".format(x))

# razão carga-massa para a configuração r2
carga_massa = 2*U2vetor/((r2*B2vetor)**2)
for x in carga_massa:
    print("{0:.2e} As/kg".format(x))

# potencial elétrico para a configuração r3
U3vetor = unumpy.uarray([100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300],[0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 2, 2, 2, 2])

# corrente elétrica para a configuração r3
I3vetor = unumpy.uarray([1.12, 1.13, 1.33, 1.47, 1.59, 1.70, 1.79, 1.90, 2.00, 1.67, 2.12],[0.23, 0.23, 0.24, 0.24, 0.25, 0.25, 0.25, 0.26, 0.26, 0.25, 0.27])

# campo magnético para a configuração r3
B3vetor = ((4/5)**(3/2))*u0*n*(I3vetor/R)
for x in B3vetor:
    print("{0:.2e} T".format(x))

# razão carga-massa para a configuração r3
carga_massa = 2*U3vetor/((r3*B3vetor)**2)
for x in carga_massa:
    print("{0:.2e} As/kg".format(x))

# potencial elétrico para a configuração r4
U4vetor = unumpy.uarray([100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300],[0.8, 0.9, 1, 1, 1, 1, 1, 2, 2, 2, 2])

# corrente elétrica para a configuração r4
I4vetor = unumpy.uarray([0.89, 0.90, 1.07, 1.17, 1.26, 1.35, 1.42, 1.48, 1.56, 1.62, 1.77],[0.24, 0.24, 0.24, 0.25, 0.25, 0.25, 0.25, 0.25, 0.26, 0.26, 0.26])

# campo magnético para a configuração r4
B4vetor = ((4/5)**(3/2))*u0*n*(I4vetor/R)
for x in B4vetor:
    print("{0:.2e} T".format(x))

# razão carga-massa para a configuração r4
carga_massa = 2*U4vetor/((r4*B4vetor)**2)
for x in carga_massa:
    print("{0:.2e} As/kg".format(x))
