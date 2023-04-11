from CRABClient.UserUtilities import config
config = config()
config.General.requestName = 'clustAlg_TTToHadronic_golden_000' #'diquark_QCD_background_data_0003' #
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.JobType.allowUndistributedCMSSW = True
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'clusteringAnalyzerBR_cfg.py'
config.Data.inputDataset = '/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM'
config.Data.publication = False
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
#config.Data.lumiMask = 'Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt'
config.Data.outputDatasetTag = 'clustAlg_TTToHadronic_golden'
config.Site.storageSite = 'T3_US_FNALLPC'
