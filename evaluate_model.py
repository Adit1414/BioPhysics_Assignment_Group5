from modeller import *
from modeller.scripts import complete_pdb

log.verbose()    # request verbose output
env = Environ()
env.libs.topology.read(file='$(LIB)/top_heav.lib') # read topology
env.libs.parameters.read(file='$(LIB)/par.lib') # read parameters

# read model file
# mdl1 = complete_pdb(env, 'P11413M.B99990001.pdb')
# mdl2 = complete_pdb(env, 'P11413M.B99990002.pdb')
# mdl3 = complete_pdb(env, 'P11413M.B99990003.pdb')

# tem1 = complete_pdb(env, 'P11413.B99990001.pdb')
# tem2 = complete_pdb(env, 'P11413.B99990002.pdb')
# tem3 = complete_pdb(env, 'P11413.B99990003.pdb')
# temM1 = complete_pdb(env, 'P11413M.B99990001.pdb')
# temM2 = complete_pdb(env, 'P11413M.B99990002.pdb')
temM3 = complete_pdb(env, 'P11413M.B99990003.pdb')

# Assess all atoms with DOPE:
# s1 = Selection(tem1)
# s1.assess_dope(output='ENERGY_PROFILE NO_REPORT', file='dope_shope_P11413_B99990001.profile',
#               normalize_profile=True, smoothing_window=15)
# s2 = Selection(tem2)
# s2.assess_dope(output='ENERGY_PROFILE NO_REPORT', file='dope_shope_P11413_B99990002.profile',
#               normalize_profile=True, smoothing_window=15)
# s3 = Selection(tem3)
# s3.assess_dope(output='ENERGY_PROFILE NO_REPORT', file='dope_shope_P11413_B99990003.profile',
#               normalize_profile=True, smoothing_window=15)
# m1 = Selection(temM1)
# m1.assess_dope(output='ENERGY_PROFILE NO_REPORT', file='dope_shope_P11413M_B99990001.profile',
#               normalize_profile=True, smoothing_window=15)
# m2 = Selection(temM2)
# m2.assess_dope(output='ENERGY_PROFILE NO_REPORT', file='dope_shope_P11413M_B99990002.profile',
#               normalize_profile=True, smoothing_window=15)
m3 = Selection(temM3)
m3.assess_dope(output='ENERGY_PROFILE NO_REPORT', file='dope_shope_P11413M_B99990003.profile',
              normalize_profile=True, smoothing_window=15)