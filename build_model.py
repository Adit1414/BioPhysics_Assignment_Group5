from modeller import *
from modeller.automodel import *

env = Environ()
a = AutoModel(env, alnfile='n1-mult.ali',
              knowns=('6e07B','6e08L','7snfA','7sniA'), sequence='P11413') #changes made here
a.starting_model = 1
a.ending_model = 3 #important - jitne bologe utni files banengi of types  NS3.B99990001.pdb, NS3.D00000001, NS3.V99990001
a.make()

