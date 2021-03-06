import sys
import ROOT

try:
  input = raw_input
except:
  pass

if len(sys.argv) < 2:
	print(" running method: macro_file_name.py input_file_name.root")
	sys.exit(1)


## Set your Delphes/libDelphes.so path, header path
ROOT.gSystem.Load("/home/twkim/Delphes3.4.2/libDelphes.so") ### <- If you wanna change to delphes, rewrite this line to your PATH

try:
  ROOT.gInterpreter.Declare('#include "/home/twkim/Delphes3.4.2/classes/DelphesClasses.h"') ### <- If you wanna change to delphes, rewrite this line to your PATH
  ROOT.gInterpreter.Declare('#include "/home/twkim/MG5_aMC_v2_7_3/ExRootAnalysis/ExRootAnalysis/ExRootTreeReader.h"')
except:
  pass


## Read & Write File
inputFile = sys.argv[1]
outputFile = ROOT.TFile.Open("DM_100GeV_MET.root","recreate") ### <- Set Your output file name

## Create chain of root trees
chain = ROOT.TChain("Delphes")
chain.Add(inputFile)

## Create object of class ExRootTreeReader
treeReader = ROOT.ExRootTreeReader(chain)
numberOfEntries = treeReader.GetEntries()

## Get pointers to branches used in this analysis
branchMET = treeReader.UseBranch("MissingET")

## if you want to use another branch, follow this line after"
# branchXXX = treeReader.UseBranch("your_own_branch")

## Define histograms
histMET = ROOT.TH1F("MET", "MET distribution",200, 0, 1000.0)
#histETA = ROOT.TH1F("eta", "eta distribution", 100, -5, 5)
#histPHI = ROOT.TH1F("phi", "phi distribution", 100, -5, 5)


## EventLoop start
for entry in range(0, numberOfEntries):
	# Load selected branches with data from specified event
	treeReader.ReadEntry(entry)

	# If event contains at least 1 particle
	if branchMET.GetEntries() == 0:
		continue
	
	for i in range(0, branchMET.GetEntries()):

		a = branchMET.At(i)
		histMET.Fill(a.MET)




outputFile.Write()
outputFile.Close()

# -- EventLoop Ends
