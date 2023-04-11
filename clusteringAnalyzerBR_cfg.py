import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.tools.jetTools import updateJetCollection

process = cms.Process("analysis")

process.load('Configuration.StandardSequences.Services_cff')
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")
process.GlobalTag.globaltag = '106X_upgrade2018_realistic_v16_L1v1'



####################### new JEC stuff########################################
#process.load('JetMETCorrections.Configuration.JetCorrectors_cff')
##################################################################################
#                            BEST Jet Correction                                     #
##################################################################################
from PhysicsTools.PatAlgos.tools.jetTools import updateJetCollection

updateJetCollection(
   process,
   jetSource = cms.InputTag('slimmedJetsAK8'),
   labelName = 'UpdatedJEC',
   jetCorrections = ('AK8PFPuppi', cms.vstring(['L2Relative', 'L3Absolute', 'L2L3Residual']), 'None'),  # Update: Safe to always add 'L2L3Residual' as MC contains dummy L2L3Residual corrections (always set to 1)
   postfix = '',
   printWarning = False
)
"""
from PhysicsTools.PatAlgos.tools.jetTools import *
from RecoBTag.ONNXRuntime.pfDeepBoostedJet_cff import *
#from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import * #runMetCorAndUncFromMiniAOD

updateJetCollection(
    process,
    jetSource = cms.InputTag('slimmedJetsAK8'),
    pvSource  = cms.InputTag('offlineSlimmedPrimaryVertices'),
    svSource  = cms.InputTag('slimmedSecondaryVertices'),
    rParam    = 0.8,
    jetCorrections = ('AK8PFPuppi', cms.vstring(['L2Relative', 'L3Absolute', 'L2L3Residual']), 'None'),
    postfix        = '',
    printWarning   = True
)

process.JECSequence = cms.Sequence(
    process.patJetCorrFactors   *
    process.updatedPatJets      *
    #process.patJetCorrFactorsTransientCorrected *
    #process.updatedPatJetsTransientCorrected    *
    process.selectedUpdatedPatJets
    )
"""
##############################################################################

process.leptonVeto = cms.EDFilter("leptonVeto",
   muonCollection= cms.InputTag("slimmedMuons"),
   electronCollection = cms.InputTag("slimmedElectrons"),
metCollection = cms.InputTag("slimmedMETs"),
   tauCollection = cms.InputTag("slimmedTaus")
)
process.hadronFilter = cms.EDFilter("hadronFilter",
   fatJetCollection = cms.InputTag("slimmedJetsAK8"),
metCollection = cms.InputTag("slimmedMETs"), 
  jetCollection = cms.InputTag("slimmedJets"),
   bits = cms.InputTag("TriggerResults", "", "HLT"),
)
process.clusteringAnalyzerAll = cms.EDAnalyzer("clusteringAnalyzerAll",
runType = cms.string("BRMC"),
genPartCollection = cms.InputTag("prunedGenParticles"),
 name = cms.string('BESTGraph'),   path = cms.FileInPath('data/constantgraph.pb'), means = cms.FileInPath('data/ScalerParameters_maxAbs_train.txt'),
   fatJetCollection = cms.InputTag("slimmedJetsAK8"),
   jetCollection = cms.InputTag("slimmedJets"),
   bits = cms.InputTag("TriggerResults", "", "HLT"),
   muonCollection= cms.InputTag("slimmedMuons"),
   electronCollection = cms.InputTag("slimmedElectrons"),
 metCollection = cms.InputTag("slimmedMETs"),
  tauCollection = cms.InputTag("slimmedTaus"),
  pileupCollection = cms.InputTag("slimmedAddPileupInfo")
)

process.source = cms.Source("PoolSource",

fileNames = cms.untracked.vstring("/store/mc/RunIISummer20UL18MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2520000/253E974C-8873-AA49-A1CD-2D03622F0A2E.root"
)
)
#"file:ttbar_skim_events_1.root", "file:ttbar_skim_events_2.root"
process.TFileService = cms.Service("TFileService",fileName = cms.string("ClusteringAlgorithmBR_data_output.root")
)

process.maxEvents = cms.untracked.PSet(
   input = cms.untracked.int32(5000000)
)

process.options = cms.untracked.PSet(
   wantSummary = cms.untracked.bool(True),
)

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")

"""process.printTree = cms.EDAnalyzer("ParticleTreeDrawer",
   src = cms.InputTag("prunedGenParticles"),
   printP4 = cms.untracked.bool(False),
   printPtEtaPhi = cms.untracked.bool(False),
   printVertex = cms.untracked.bool(False),
   printStatus = cms.untracked.bool(True),
   printIndex = cms.untracked.bool(False),
   #status = cms.untracked.vint32(3),
)
"""
process.p = cms.Path( process.hadronFilter * process.leptonVeto * 
process.clusteringAnalyzerAll  #needs star  process.JECSequence*
   # 
)
