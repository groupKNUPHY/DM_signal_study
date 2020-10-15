import sys
from rootpy.io import root_open
import rootpy.ROOT as ROOT
from rootpy.plotting import Hist, HistStack, Legend, Canvas
import rootpy.plotting.root2matplotlib as rplt
import matplotlib.pyplot as plt

try:
  input = raw_input
except:
  pass

if len(sys.argv) < 2:
        print(" running method: macro_file_name.py input_file_name.root")
        sys.exit(1)


# --Set your Delphes/libDelphes.so path, header path
ROOT.gSystem.Load("/home/twkim/MG5_aMC_v2_7_3/ExRootAnalysis/libExRootAnalysis.so")



try:
  ROOT.gInterpreter.Declare('#include "/home/twkim/MG5_aMC_v2_7_3/ExRootAnalysis/ExRootAnalysis/ExRootClasses.h"')
  ROOT.gInterpreter.Declare('#include "/home/twkim/MG5_aMC_v2_7_3/ExRootAnalysis/ExRootAnalysis/ExRootTreeReader.h"')
except:
  pass



# Read & Write File

inputFile = sys.argv[1]
outputFile = ROOT.TFile.Open("BKG_ttbar_bpt.root","recreate") ### <- Set Your output file name


# Create chain of root trees
chain = ROOT.TChain("LHEF")
chain.Add(inputFile)

# Create object of class ExRootTreeReader
treeReader = ROOT.ExRootTreeReader(chain)
numberOfEntries = treeReader.GetEntries()

# Get pointers to branches used in this analysis
branchParticle = treeReader.UseBranch("Particle")
# branchElectron = treeReader.UseBranch("Electron")

# Define histograms
histPT = ROOT.TH1F("pt", "p_{T} distribution",80, 0, 400.0)
histEta = ROOT.TH1F("eta", "eta distribution",100, -10, 10)
histPhi = ROOT.TH1F("phi", "phi distribution",100, -10, 10)



# --EventLoop start
for entry in range(0, numberOfEntries):
	# Load selected branches with data from specified event
	treeReader.ReadEntry(entry)

	# If event contains at least 1 electrons
	if branchParticle.GetEntries() == 0:
		continue
	
	for i in range(0, branchParticle.GetEntries()):

		a = branchParticle.At(i)
		if abs(a.PID) in [5]:
			histPT.Fill(a.PT)
			histEta.Fill(a.Eta)
			histPhi.Fill(a.Phi)

# I/O
outputFile.write()
outputFile.close()

# -- EventLoop Ends



