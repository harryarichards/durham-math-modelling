from brusselator_pde import BrusselatorPDE

# set paremeter values
a = 1.5
b = 3
Du = 2.8
Dv = 22.4
L = 50
N = 100
tmax = 99.9
fig_dt = tmax/200
epsilon = 0.01

# Prepare the BrusselatorPDE for integration
br = BrusselatorPDE(L, N, 0, Du, Dv, a, b)
br.initial_condition(epsilon)

# Integrate until tmax with data saved every fig_dt
br.iterate(tmax,fig_dt)

# Plot Profile u(x) and v(x) at t=tmax
br.plot_v_u()

# Plot Profile u(3*L/8,t) and v(3*L/8,t)
br.plot_u_v_Lo2(3*L/8.0)
