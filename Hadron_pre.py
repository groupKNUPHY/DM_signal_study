## Warning ##
## This code designed at a hybrid conda-environment! ##
## If you want to contact the code designer, please visit ROOM 208 and call Tau Kim ##

import uproot as ROOT
import awkward1 as ak
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib import font_manager
import mplhep as hep
#import os
import glob
import timeit


def Eagles(filepath, filetype):
	## Get file list
	print("Start of",filetype)
	targetPattern = r""+ filepath +""
	filelist = glob.glob(targetPattern)

	## Define an empty list
	MET = []
	count = 1
	## Fileloop
	for f in filelist:
		## Open file
		data = ROOT.open(f)["Delphes"]

		## Make array
		MET_arr, Jet_arr = data.arrays(['PuppiMissingET.MET', 'JetPUPPI.PT'],outputtype=tuple)
		MET_arr = MET_arr.flatten()
		nEvents = len(MET_arr)

		## Minor loop
		for i in range(nEvents):
			MET.append(MET_arr[i])

		## EOF
		print("Number of Events",len(MET))

		## Debuging term
		#count += 1
		#if count == 3:
		#	break

	np.save(""+ filetype +"_MET",MET)
	print("End of",filetype,filepath)
	## EOF

## Main code
pathlist = ["/x4/cms/jyshin/TT_Had/condorDelPyOut/*.root", "/x4/cms/jyshin/TT_1l/condorDelPyOut/*.root"]
labellist = ["TT_had","TT_semi"]

for i in range(len(pathlist)):
	Eagles(pathlist[i],labellist[i])

print("End of Code")
