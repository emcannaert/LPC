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
process.hadronFilter = cms.EDFilter("hadronFilter",
   fatJetCollection = cms.InputTag("slimmedJetsAK8"),
metCollection = cms.InputTag("slimmedMETs"), 
  jetCollection = cms.InputTag("slimmedJets"),
   bits = cms.InputTag("TriggerResults", "", "HLT"),
)
process.clusteringAnalyzerData = cms.EDAnalyzer("clusteringAnalyzerData",
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

fileNames = cms.untracked.vstring("/store/data/Run2018C/JetHT/MINIAOD/UL2018_MiniAODv2-v1/280000/0E538044-8EAF-6A46-9179-0CAEC8A5CA11.root","/store/data/Run2018C/JetHT/MINIAOD/UL2018_MiniAODv2-v1/280000/6BE358B8-6D6A-D04B-A92F-994616E1DF44.root","/store/data/Run2018C/JetHT/MINIAOD/UL2018_MiniAODv2-v1/280000/800A2086-127C-D84F-9686-558DFCC72327.root","/store/data/Run2018C/JetHT/MINIAOD/UL2018_MiniAODv2-v1/280000/DB3DB403-B661-0646-B490-688FC930DC21.root"
)
)
process.TFileService = cms.Service("TFileService",fileName = cms.string("ClusteringAlgorithmData_output.root")

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
process.p = cms.Path(  process.hadronFilter * process.leptonVeto * 
process.clusteringAnalyzerData  #needs star 
   # 
)
