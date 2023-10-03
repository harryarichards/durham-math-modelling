if __name__ == "__main__":
  # Compute a reference solution using RK4 and a small dt
  tmax=1
  lv = LotkaVolterraRK4()  # create a RK4 LV object
  lv.set_K(1)               # set the parameter
  lv.reset(V0=[0.1,0.1],dt=1e-5) # use RK4 and dt=1e05 for reference value
  lv.iterate(tmax,0.1)      # compute reference value
  V_ref = lv.V              # Make copy of reference function values 


  dt = 0.2
  # Solve using RK4
  lv.reset(V0=[0.1,0.1],dt=dt)
  lv.iterate(tmax,0.1)
  V = lv.V
  print("RK4 : dt="+str(dt)+": Error =",np.sqrt((V_ref-V).dot(V_ref-V))) 

  # Solve using Euler
  lve = LotkaVolterra()     # LV for Euler method
  lve.set_K(1)

  lve.reset(V0=[0.1,0.1],dt=dt)
  lve.iterate(tmax,0.1)
  V = lve.V
  print("Euler : dt="+str(dt)+": Error =",np.sqrt((V_ref-V).dot(V_ref-V))) 
  
