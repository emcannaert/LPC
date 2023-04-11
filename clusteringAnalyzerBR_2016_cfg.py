import FWCore.ParameterSet.Config as cms

process = cms.Process("analysis")

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")
process.GlobalTag.globaltag = '106X_upgrade2018_realistic_v16_L1v1'

process.leptonVeto = cms.EDFilter("leptonVeto",
   muonCollection= cms.InputTag("slimmedMuons"),
   electronCollection = cms.InputTag("slimmedElectrons"),
metCollection = cms.InputTag("slimmedMETs"),
   tauCollection = cms.InputTag("slimmedTaus")
)
process.hadronFilter2016 = cms.EDFilter("hadronFilter2016",
   fatJetCollection = cms.InputTag("slimmedJetsAK8"),
metCollection = cms.InputTag("slimmedMETs"), 
  jetCollection = cms.InputTag("slimmedJets"),
   bits = cms.InputTag("TriggerResults", "", "HLT"),
)
process.clusteringAnalyzerAll = cms.EDAnalyzer("clusteringAnalyzerAll",
genPartCollection = cms.InputTag("prunedGenParticles"),
 name = cms.string('BESTGraph'),   path = cms.FileInPath('data/constantgraph.pb'), means = cms.FileInPath('data/ScalerParameters_maxAbs_train.txt'),
   fatJetCollection = cms.InputTag("slimmedJetsAK8"),
   jetCollection = cms.InputTag("slimmedJets"),
   bits = cms.InputTag("TriggerResults", "", "HLT"),
   muonCollection= cms.InputTag("slimmedMuons"),
   electronCollection = cms.InputTag("slimmedElectrons"),
 metCollection = cms.InputTag("slimmedMETs"),
  tauCollection = cms.InputTag("slimmedTaus")
)

process.source = cms.Source("PoolSource",

fileNames = cms.untracked.vstring("/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/2520000/4DE0AF97-A290-0F42-8B97-FE3CF365C623.root"
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
process.p = cms.Path(  process.hadronFilter2016 * process.leptonVeto * 
process.clusteringAnalyzerBR  #needs star 
   # 
)
