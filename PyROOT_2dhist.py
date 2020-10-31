import sys
import ROOT
import matplotlib.pyplot as plt
import numpy as np

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
outputFile = ROOT.TFile.Open("BKG_ttbar_vec.root","recreate") ### <- Set Your output file name

## Create chain of root trees
chain = ROOT.TChain("Delphes")
chain.Add(inputFile)

## Create object of class ExRootTreeReader
treeReader = ROOT.ExRootTreeReader(chain)
numberOfEntries = treeReader.GetEntries()

## Get pointers to branches used in this analysis
branchParticle = treeReader.UseBranch("Particle")

## if you want to use another branch, follow this line after"
branchMET = treeReader.UseBranch("MissingET")

## Define histograms
histVec = ROOT.TH1F("Vec", "MET distribution",200, 0, 1000.0)
histMET = ROOT.TH1F("MET", "MET distribution",200, 0, 1000.0)

cnt = 0
vec_2d = []
met_2d = []

## EventLoop start
for entry in range(0, numberOfEntries):
	# Load selected branches with data from specified event
	treeReader.ReadEntry(entry)

	ve = 0.0
	vm = 0.0
#	dm = 0.0
	
	# If event contains at least 1 particle
	if branchParticle.GetEntries() == 0:
		continue
	
	for i in range(0, branchParticle.GetEntries()):

		a = branchParticle.At(i)
		if abs(a.PID) == 12 and a.Status == 1:
			ve = (a.PT)
		if abs(a.PID) == 14 and a.Status ==1:
			vm = (a.PT)
#		if abs(a.PID) == 9000007:
#			dm = (a.PT)

	vec_nu = ve + vm # + dm
	vec_2d.append(vec_nu)
        histVec.Fill(vec_nu)
	cnt += 1
	if (cnt%100 == 0):
		print("working", cnt) 

	if branchMET.GetEntries() == 0:
		continue

	for i in range(0, branchMET.GetEntries()):
		a = branchMET.At(i)
		histMET.Fill(a.MET)
		met_2d.append(a.MET)

outputFile.Write()
outputFile.Close()


plt.xlim(0, 1000)
plt.ylim(0, 1000)
plt.title("MET versus Vector", fontsize=15)
plt.xlabel("MET [GeV]")
plt.ylabel("Vector [GeV]")
plt.hist2d(met_2d, vec_2d, bins=(100,100), cmap=plt.cm.jet)
plt.savefig("2d_ttbar.png")


# -- EventLoop Ends
