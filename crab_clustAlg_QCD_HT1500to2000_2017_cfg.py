from CRABClient.UserUtilities import config
config = config()
config.General.requestName = 'crab_clustAlg_QCD_HT1500to2000_2017_2'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
#config.JobType.allowUndistributedCMSSW = True
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'clusteringAnalyzerBR_cfg.py'
config.Data.inputDataset = '/QCD_HT1500to2000_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM'
#'/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM'
config.Data.publication = False
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
#config.Data.lumiMask = 'Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt'
config.Data.outputDatasetTag = 'clustAlg_QCD_HT1500to2000_2017'
config.Site.storageSite = 'T3_US_FNALLPC'
