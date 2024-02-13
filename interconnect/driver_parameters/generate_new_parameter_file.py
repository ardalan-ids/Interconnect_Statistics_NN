import numpy as np

# # driver dependent  variables
'''
# 45nm d0 #
name = "comm_45nm_d0"
R_on = np.array([15.77, 14.45, 14.32])*1e3  # on resistance (WC)
t_0 = np.array([35.5, 36.4, 36.8])*1e-12  # delay offset (WC)
E_toggle = np.array([0.8, 0.81, 0.815])*1e-15  # mean energy for lh and hl (TC)
boundaries = np.array([0, 0.67, 10.93])*1e-15
C_in = 0.47e-15  # gate capacitance (TC)
A = 0.7056e-12  # Area in [um]*[um]
V_dd = 0.99
max_loadC = 21.86e-15

# 45nm d4 #
name = "comm_45nm_d4"
R_on = np.array([1.95, 1.57, 1.55])*1e3  # on resistance (WC)
t_0 = np.array([26.4, 27.7, 28])*1e-12  # delay offset (WC)
E_toggle = np.array([2.85, 2.95, 3])*1e-15  # mean energy for lh and hl (TC)
boundaries = np.array([0, 5.02, 129.5])*1e-15
C_in = 1.2e-15  # gate capacitance (TC)
A = 1.5876e-12  # Area in [um]*[um]
V_dd = 0.99
max_loadC = 174.9e-15

# 180nm d0 #
name = "comm_180nm_d0"
R_on = np.array([13.25, 12.83, 12.75])*1e3  # on resistance (WC)
t_0 = np.array([105, 107, 109])*1e-12  # delay offset (WC)
E_toggle = np.array([51, 10.7, 1.7])*1e-15  # mean energy for lh and hl (TC)
boundaries = np.array([0, 4.56, 74.36])*1e-15
C_in = 3.088e-15  # gate capacitance (TC)
A = 8.7808e-12  # Area in [um]*[um]
V_dd = 1.8
max_loadC = 146.9e-15



# 180nm d2 #
name = "comm_180nm_d2"
R_on = np.array([3.48, 3.15, 3.12])*1e3  # on resistance (WC)
t_0 = np.array([105, 110, 113])*1e-12  # delay offset (WC)
E_toggle = np.array([85, 14.8, 2])*1e-15  # mean energy for lh and hl (TC)
boundaries = np.array([0, 13.04, 294.8])*1e-15
C_in = 5.36e-15  # gate capacitance (TC)
A = 13.17e-12  # Area in [m]*[m]
V_dd = 1.8
max_loadC = 595.3e-15
'''

# 45nm freepdk X1 (delay calculated without driver offset)
name = "nangate45_d1"
R_on = np.array([6.5, 6.2])*1e3  # on resistance (WC)
t_0 = np.array([0, 0])*1e-12  # delay offset (WC)
E_toggle = np.array([2.64, 1.39])*1e-15
boundaries = np.array([0, 60.73])*1e-15
C_in = 1.7002e-15  # gate capacitance (TC)
A = 0.532e-12
V_dd = 1.1
max_loadC = 60.73e-15

'''
# 45nm freepdk X2 (delay calculated without driver offset)
name = "nangate45_d2"
A = 2*0.532e-12
R_on = np.array([3.25, 3.1])*1e3  # on resistance (WC)
t_0 = np.array([0, 0])*1e-12  # delay offset (WC)
E_toggle = np.array([2*2.64, 2*1.39])*1e-15
boundaries = np.array([0, 2*60.73])*1e-15
C_in = 2*1.7002e-15  # gate capacitance (TC)
V_dd = 1.1
max_loadC = 2*60.73e-15


# 15nm freepdk X1 (delay calculated without driver offset)
name = "nangate15_d1"
A = 0.147456e-12
R_on = np.array([3.25, 3.1])*1e3  # on resistance (WC)
t_0 = np.array([0, 0])*1e-12  # delay offset (WC)
E_toggle = np.array([0.88, 0.46])*1e-15
boundaries = np.array([0, 60.73])*1e-15
C_in = 0.82e-15  # gate capacitance (TC)
V_dd = 0.8
max_loadC = 50.148e-15


# 15nm freepdk X2 (delay calculated without driver offset)
name = "nangate15_d2"
A = 2*0.147456e-12
R_on = np.array([3.25/2, 3.1/2])*1e3  # on resistance (WC)
t_0 = np.array([0, 0])*1e-12  # delay offset (WC)
E_toggle = np.array([0.88*2, 0.46*2])*1e-15
boundaries = np.array([0, 60.73*2])*1e-15
C_in = 2*0.82e-15  # gate capacitance (TC)
V_dd = 0.8
max_loadC = 2*50.148e-15


# 180nm d4 #
name = "comm_180nm_d4"
R_on = np.array([1.734, 1.575, 1.561])*1e3  # on resistance (WC)
t_0 = np.array([97.3, 101.1, 104.6])*1e-12  # delay offset (WC)
E_toggle = np.array([60.35, 10.6, 1.7])*1e-15  # mean energy for lh and hl (TC)
boundaries = np.array([0, 25.3, 589.1])*1e-15
C_in = 10.15e-15  # gate capacitance (TC)
A = 19.76e-12  # Area in [m]*[m]
V_dd = 1.8
max_loadC = 1191e-15






# 180nm mixed signal d0 #
name = "comm_ms180nm_d0"
R_on = np.array([41.72, 40.25, 40])*1e3  # on resistance (WC)
t_0 = np.array([342, 347.4, 356.9])*1e-12  # delay offset (WC)
E_toggle = np.array([4.4, 4.5, 4.6])*1e-15  # mean energy for lh and hl (TC)
boundaries = np.array([0, 3.39, 60.37])*1e-15
C_in = 2.87e-15  # gate capacitance (TC)
A = 8.7808e-12  # Area in [um]*[um]
V_dd = 1
max_loadC = 119.9e-15
'''
'''
# 180nm mixed signal d2 (highest avail. strength) #
name = "comm_ms180nm_d2"
R_on = np.array([10.533, 9.742, 9.67])*1e3  # on resistance (WC)
t_0 = np.array([331, 339.5, 345.7])*1e-12  # delay offset (WC)
E_toggle = np.array([11.05, 11.6, 12.1])*1e-15  # mean energy for lh and hl (TC)
boundaries = np.array([0, 10.24, 239.7])*1e-15
C_in = 4.872e-15  # gate capacitance (TC)
A = 13.17e-12  # Area in [um]*[um]
V_dd = 1
max_loadC = 484.6e-15
'''

# # main part
np.savez('driver_%s' % name,
         id=name, R_on=R_on, t_0=t_0, E_toggle=E_toggle,
         boundaries=boundaries, C_in=C_in, A=A, V_dd=V_dd, max_loadC=max_loadC)

'''
# example how to read file later
driver_parameter = np.load('driver_%s.npz' % name)

# example how to read the scalar parameters
A_readed = float(driver_parameter['A'])
'''
