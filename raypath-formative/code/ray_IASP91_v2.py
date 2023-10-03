import numpy as np
import matplotlib.pyplot as plt

RE = 6371.0 # Earth Radius
RM = 3482.0 # Bottom of mantel radius
RC = 1217.1 # Inner core radius
# Slowness as function of r
#

class Raytrace:

    def __init__(self):
        self.list_r = []  # list of values for radial coordinates
        self.list_th= []  # list of values for theta  coordinates
        self.list_wave = [] # list of wave types
       
    def Vp(self, r):
        """ Vp as a function of radial position
            SOURCE: DOI: http://doi.org/10.2312/GFZ.NMSOP_r1_DS_2.1

        : param r : distance from Earth centre
        """
        x = r/RE
        if(r <1217.1):
            v=11.24094-4.09689*x*x
        elif(r<3482):
            v=10.03904+3.75665*x-13.67046*x*x
        elif(r<3631):
            v=14.49470-1.47089*x
        elif(r<5611):
            v=25.1486-41.1538*x+51.9932*x*x-26.6083*x*x*x
        elif(r<5711):
            v=25.96984-16.93412*x
        elif(r<5961):
            v=29.38896-21.40656*x
        elif(r<6161):
            v=30.78765-23.25415*x
        elif(r<6251):
            v=25.41389-17.69722*x
        elif(r<6336):
            v=8.78541-0.74953*x
        elif(r<6351):
            v=6.50
        else:
            v=5.80
        return(v)

    def Vs(self, r):
        """ Vs as a function of radial position
            SOURCE: DOI: http://doi.org/10.2312/GFZ.NMSOP_r1_DS_2.1

        : param r : distance from Earth centre
        """
        x = r/RE
        if(r <1217.1):
            v=3.56454-3.45241*x*x
        elif(r<3482):
            v=0.0
        elif(r<3631):
            v=8.16616-1.58206*x
        elif(r<5611):
            v=12.9303-21.2590*x+27.8988*x*x-14.1080*x*x*x
        elif(r<5711):
            v=20.76890-16.53147*x
        elif(r<5961):
            v=17.70732-13.50652*x
        elif(r<6161):
            v=15.24213-11.08552*x
        elif(r<6251):
            v=5.75020-1.27420*x
        elif(r<6336):
            v=6.706231-2.248585*x
        elif(r<6351):
            v=3.75
        else:
            v=3.36
        return(v)

    def u(self, r, wave):
        """ Return slowness for the specified wave and position

        : param r : distance from Earth centre
        : param wave : wave type : 'P' and 'S'
        """
        if(wave=='P') : return(1./self.Vp(r))
        return(1./self.Vs(r))

### MARKING coding 1
    def T_Delta_Int(self, r, p, wave):
        result1 = (r ** 2 * self.u(r, wave) ** 2)/ (r * np.sqrt(r ** 2 * self.u(r, wave) ** 2 - p ** 2))
        result2 = (p) / (r * np.sqrt(r ** 2 * self.u(r, wave) ** 2 - p ** 2))

        return np.array([result1, result2])

### END MARKING

    def Int(self, dr, p, wave):
        """ Integrate function T_Delta_Int from RE to bottom.
        Save the values of r, Delta and wave in the class lists 'list_r', 
        'list_th' and 'list_wave', used by 'plot_trajectory' to generate figures
        Return [T,Delta] for the path or [-1, 0] if the path does not exist.

        :param dr: radial step
        :param p : ray parameter
        :param wave : type of wave: 'P' or 'S'
        """
        V = np.array([0., 0.])
        r = RE
        self.list_r.append(r)
        self.list_th.append(0)
        self.list_wave.append(wave)
        r+= dr*0.5 # move to middle of segment

        while(r*self.u(r, wave) > p): # while still going down
          V += self.T_Delta_Int(r, p, wave)*dr
          r -= dr
          self.list_r.append(r)
          self.list_th.append(V[1])
          self.list_wave.append(wave)
          if((wave == "S") and (r < RM)): # no S wave in outer core
            return(np.array([-1, 0]))
          
        r += dr  # gone too far: move back
### MARKING coding 1
        while(r < RE):
### END MARKING
          V += self.T_Delta_Int(r, p, wave)*dr 
### MARKING coding 1
          r += dr
### END MARKING
          self.list_r.append(r)
          self.list_th.append(V[1])
          self.list_wave.append(wave)

        return(V)
    
### MARKING: coding 2
    def Int_mPm(self, dr, p, wave):
        V = np.array([0., 0.])
        r = RE
        self.list_r.append(r)
        self.list_th.append(0)
        self.list_wave.append(wave)
        r += dr * 0.5  # move to middle of segment

        while (r > RM and r * self.u(r, wave) > p):  # while still going down
            V += self.T_Delta_Int(r, p, wave) * dr
            r -= dr
            self.list_r.append(r)
            self.list_th.append(V[1])
            self.list_wave.append(wave)


        if (r > RM):
            return np.array([-1, 0]) # wave turned back before reaching mantel - not of desired type.

        wave = "P" # waves typeset as primary
        r += dr # dr changes sign as we will now compute upper part of path


        while (r < RE):
            V += self.T_Delta_Int(r, p, wave) * dr
            r += dr
            self.list_r.append(r)
            self.list_th.append(V[1])
            self.list_wave.append(wave)
        return (V)

    def Int_mSm(self, dr, p, wave):
        V = np.array([0., 0.])
        r = RE
        self.list_r.append(r)
        self.list_th.append(0)
        self.list_wave.append(wave)
        r += dr * 0.5  # move to middle of segment

        while (r > RM and r * self.u(r, wave) > p):  # while still going down
            V += self.T_Delta_Int(r, p, wave) * dr
            r -= dr
            self.list_r.append(r)
            self.list_th.append(V[1])
            self.list_wave.append(wave)
            if ((wave == "S") and (r < RM)):  # no S wave in outer core
                return (np.array([-1, 0]))
        if (r > RM):
            return np.array([-1, 0])

        wave = "S"
        r += dr

        while (r < RE):
            V += self.T_Delta_Int(r, p, wave) * dr
            r += dr
            self.list_r.append(r)
            self.list_th.append(V[1])
            self.list_wave.append(wave)
        return (V)



    def Int_mPoSm(self, dr, p, wave):
        V = np.array([0., 0.])
        r = RE
        self.list_r.append(r)
        self.list_th.append(0)
        self.list_wave.append(wave)
        r += dr * 0.5  # move to middle of segment

        while (r > RM and r * self.u(r, wave) > p):  # while still going down and not yet at bottom of mantel
            V += self.T_Delta_Int(r, p, wave) * dr
            r -= dr
            self.list_r.append(r)
            self.list_th.append(V[1])
            self.list_wave.append(wave)

        if (r > RM): # if never reaching the mantel
            return np.array([-1, 0])

        wave = "P" # set wave type to primary

        while (r * self.u(r, wave) > p):
            V += self.T_Delta_Int(r, p, wave) * dr
            r -= dr
            self.list_r.append(r)
            self.list_th.append(V[1])
            self.list_wave.append(wave)

        r += dr

        while (r < RM):  # while still going up
            V += self.T_Delta_Int(r, p, wave) * dr
            r += dr
            self.list_r.append(r)
            self.list_th.append(V[1])
            self.list_wave.append(wave)

        wave = "S"

        while (r < RE): # while still going up
            V += self.T_Delta_Int(r, p, wave) * dr
            r += dr
            self.list_r.append(r)
            self.list_th.append(V[1])
            self.list_wave.append(wave)
        return (V)

### END MARKING

### MARKING coding 1
    def plot_VpVs(self):
        Vp_list = []
        Vs_list = []
        R_list = []
        for r in range(int(RE)):
            R_list.append(r)
            value1 = self.Vp(r)
            value2 = self.Vs(r)
            Vp_list.append(value1)
            Vs_list.append(value2)
        plt.xlabel('r', fontsize = 12)
        plt.ylabel('Vp, Vs', fontsize = 12)
        plt.plot(R_list, Vp_list, 'b-')
        plt.plot(R_list, Vs_list, 'r-') # plot Vp and Vs afainst eachother in red and blue
        plt.legend(['Vp', 'Vs']) # label graph
        plt.show()

### END MARKING
        
    def plot_circle(self, R, col):
        """ Plot a circle of radius R in colour col

        :param R : circle radius
        :param col : circle color ('r', 'g', 'b', 'k', 'c', 'm', or 'y')
        """
        circle2 = plt.Circle((0, 0), R, color=col, fill=False, linewidth=2)
        ax = plt.gca()
        #ax.cla() # clear things for fresh plot
        ax.add_artist(circle2)

    def trajectory(self, theta, wave, dr):
        """ Compute the trajectory of the specified wave 
            Return Traveling time and angle (T, Delta)

        :param theta : incident angle in degrees
        :param path : Pm PmPm PmSm PmPoSm Sm SmPm SmSm SmPoSm
        :param dr : integration step in km
        """
        self.list_r = []
        self.list_th = []
        self.list_wave = []
        self.theta=theta
        self.path=wave

### MARKING coding 2
        th = np.radians(theta)
        p = RE*self.u(RE, wave)*np.sin(th)

        T, DeltaP = self.Int(dr, p, wave)
### END MARKING

        return(T, np.degrees(DeltaP))


    def trajectory(self, theta, path, dr):
        self.list_r = []
        self.list_th = []
        self.list_wave = []
        self.theta = theta
        self.path = path

        ### MARKING coding 2
        wave = path[0]
        th = np.radians(theta)
        p = RE * self.u(RE, wave) * np.sin(th)
        path = path.lower()
        if path == "pm" or path == "sm":
            T, DeltaP = self.Int(dr, p, wave)
        elif path == "pmpm" or path == "smpm":
            T, DeltaP = self.Int_mPm(dr, p, wave)
        elif path == "pmsm" or path == "smsm":
            T, DeltaP = self.Int_mSm(dr, p, wave)
        elif path == "smposm" or path == "pmposm":
            T, DeltaP = self.Int_mPoSm(dr, p, wave)

        ### END MARKING

        return (T, np.degrees(DeltaP))

    
    
    def plot_trajectory(self):
        """ Plot the Earth Radius in green the boundary between the mantel and
            the outer core in magenta and the boundary between the 2 cores in
            red. Then plot the trajectory of the waves in black for P waves
            and blue for S waves.
        """
        self.plot_circle(RE, "g")
        self.plot_circle(RM, "m")
        self.plot_circle(RC, "r")
    
        xl = []
        yl = []
        thmax = self.list_th[-1]*0.5 # to generate symmetric figure
        n = len(self.list_r)         # number of data points
        wave = self.list_wave[0]     # wave type
        oldWaveType = wave

### MARKING coding 1
        # POPULATE xl and yl with data
        for i in range(n):
            xl.append(self.list_r[i] * np.cos(self.list_th[i] - thmax))
            yl.append(self.list_r[i] * np.sin(self.list_th[i] - thmax))

            if (wave != oldWaveType) or (i == (n-1)):
                if (wave == "P"):
                    col = 'k'
                else:
                    col ='b'

                plt.plot(xl, yl, col)
                xl.clear()
                yl.clear()
### END MARKING
        
        # select colour
        if(wave == "P") : col = "k"
        else: col = "b"
        
        plt.title(r'$\theta=$'+str(self.theta)+", path="+self.path)
        plt.plot(xl, yl, col)
        plt.axis([-8500, 8500, -6500, 6500], 'equal')
        plt.show()

        
### MARKING coding 3
    def plot_multi_trajectory(self, nocircle=False):
        """ Plot the Earth Radius in green the boundary between the mantel and
            the outer core in magenta and the boundary between the 2 cores in
            red. Then plot the trajectory of the waves in black for P waves
            and blue for S waves.
        """
        if nocircle == False:
            self.plot_circle(RE, "g")
            self.plot_circle(RM, "m")
            self.plot_circle(RC, "r")

        xl = []
        yl = []
        thmax = self.list_th[-1] * 0.5  # to generate symmetric figure
        n = len(self.list_r)  # number of data points
        wave = self.list_wave[0]  # wave type
        oldWaveType = wave

        for i in range(n):
            xl.append(self.list_r[i] * np.cos(self.list_th[i] - thmax))
            yl.append(self.list_r[i] * np.sin(self.list_th[i] - thmax))

            if (wave != oldWaveType) or (i == (n - 1)):
                if (wave == 'P'):
                    col = 'k'
                else:
                    col = 'b'

                plt.plot(xl, yl, col)
                xl.clear()
                yl.clear()

        plt.title("Path=" + self.path)
        plt.axis([-8500, 8500, -6500, 6500], 'equal')
### END MARKING



