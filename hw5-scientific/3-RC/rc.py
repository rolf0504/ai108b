import sympy as sp

R1=R3=R5 = 1e3
R2=R4=R6 = 2e3
C1 = 1e-6
C2 = 0.5e-6
w = 1000
V0 = 5

t = sp.Symbol('t')
E = sp.exp(1j*w*t)

V1, V2, V3 = sp.symbols('V1 V2 V3')

V_plus = V0*E
V_minus = 0

V1_eqn = (V1-V_plus)/R1 + (V1-V2)/(1/(1j*w*C1)) + (V1-V_minus)/R4
V2_eqn = (V2-V_plus)/R2 + (V2-V1)/(1/(1j*w*C1)) + (V2-V_minus)/R5 + (V2-V3)/(1/(1j*w*C2))
V3_eqn = (V3-V_plus)/R3 + (V3-V2)/(1/(1j*w*C2)) + (V3-V_minus)/R6

print(sp.solve([ sp.Eq(V1_eqn, 0), sp.Eq(V2_eqn, 0), sp.Eq(V3_eqn, 0)], [V1, V2, V3] ))