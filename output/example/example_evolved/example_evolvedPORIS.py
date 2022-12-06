from PORIS import *

class example_evolvedPORIS:
	def __init__(self):
		idcounter = 1
		self.sysEngineer = PORISSys("Engineer")
		self.mdEngineerMode_UNKNOWN = PORISMode("EngineerMode_UNKNOWN")
		self.root = self.sysEngineer
		self.sysOperator = PORISSys("Operator")
		self.mdOperatorMode_UNKNOWN = PORISMode("OperatorMode_UNKNOWN")
		self.sysInstrument = PORISSys("Instrument")
		self.mdInstrumentMode_UNKNOWN = PORISMode("InstrumentMode_UNKNOWN")
		self.prMasks = PORISParam("Masks")
		self.mdMasksMode_UNKNOWN = PORISMode("MasksMode_UNKNOWN")
		self.vlMasks_UNKNOWN = PORISValue("Masks_UNKNOWN")
		self.prDispersion = PORISParam("Dispersion")
		self.mdDispersionMode_UNKNOWN = PORISMode("DispersionMode_UNKNOWN")
		self.vlDispersion_UNKNOWN = PORISValue("Dispersion_UNKNOWN")
		self.sysDetector = PORISSys("Detector")
		self.mdDetectorMode_UNKNOWN = PORISMode("DetectorMode_UNKNOWN")
		self.prexpTime = PORISParam("expTime")
		self.mdexpTimeMode_UNKNOWN = PORISMode("expTimeMode_UNKNOWN")
		self.vlexpTime_UNKNOWN = PORISValue("expTime_UNKNOWN")
		self.prBinning = PORISParam("Binning")
		self.mdBinningMode_UNKNOWN = PORISMode("BinningMode_UNKNOWN")
		self.vlBinning_UNKNOWN = PORISValue("Binning_UNKNOWN")
		self.sysFilter = PORISSys("Filter")
		self.mdFilterMode_UNKNOWN = PORISMode("FilterMode_UNKNOWN")
		self.prClassicFilters = PORISParam("ClassicFilters")
		self.mdClassicFiltersMode_UNKNOWN = PORISMode("ClassicFiltersMode_UNKNOWN")
		self.vlClassicFilters_UNKNOWN = PORISValue("ClassicFilters_UNKNOWN")
		self.sysSlicer = PORISSys("Slicer")
		self.mdSlicerMode_UNKNOWN = PORISMode("SlicerMode_UNKNOWN")
		self.prDoblador = PORISParam("Doblador")
		self.mdDobladorMode_UNKNOWN = PORISMode("DobladorMode_UNKNOWN")
		self.vlDoblador_UNKNOWN = PORISValue("Doblador_UNKNOWN")
		self.vlMasks_0_6 = PORISValue("Masks_0_6")
		self.vlMasks_1_0 = PORISValue("Masks_1_0")
		self.vlMasks_2_0 = PORISValue("Masks_2_0")
		self.mdMasksMode_Spectroscopy = PORISMode("MasksMode_Spectroscopy")
		self.vlMasks_Half_field = PORISValue("Masks_Half_field")
		self.mdMasksMode_FastImg = PORISMode("MasksMode_FastImg")
		self.mdMasksMode_Slicer = PORISMode("MasksMode_Slicer")
		self.vlMasks_SlicerMask = PORISValue("Masks_SlicerMask")
		self.mdMasksMode_Passthrough = PORISMode("MasksMode_Passthrough")
		self.vlDispersion_R500 = PORISValue("Dispersion_R500")
		self.vlDispersion_R1000 = PORISValue("Dispersion_R1000")
		self.vlDispersion_R2000 = PORISValue("Dispersion_R2000")
		self.mdDispersionMode_Normal = PORISMode("DispersionMode_Normal")
		self.vlexpTime_NormalRange = PORISValueFloat("expTime_NormalRange")
		self.mdexpTimeMode_Normal = PORISMode("expTimeMode_Normal")
		self.mdexpTimeMode_Fast = PORISMode("expTimeMode_Fast")
		self.vlexpTime_FastRange = PORISValueFloat("expTime_FastRange")
		self.vlBinning_1x1 = PORISValue("Binning_1x1")
		self.vlBinning_2x1 = PORISValue("Binning_2x1")
		self.vlBinning_1x2 = PORISValue("Binning_1x2")
		self.vlBinning_2x2 = PORISValue("Binning_2x2")
		self.mdBinningMode_Normal = PORISMode("BinningMode_Normal")
		self.mdBinningMode_Square = PORISMode("BinningMode_Square")
		self.mdBinningMode_Fast = PORISMode("BinningMode_Fast")
		self.mdDetectorMode_Normal = PORISMode("DetectorMode_Normal")
		self.mdDetectorMode_Image = PORISMode("DetectorMode_Image")
		self.mdDetectorMode_FastImage = PORISMode("DetectorMode_FastImage")
		self.mdInstrumentMode_Photometry = PORISMode("InstrumentMode_Photometry")
		self.mdInstrumentMode_SlicerSpec = PORISMode("InstrumentMode_SlicerSpec")
		self.mdInstrumentMode_FastPhotometry = PORISMode("InstrumentMode_FastPhotometry")
		self.mdFilterMode_Classic = PORISMode("FilterMode_Classic")
		self.mdFilterMode_TFBlue = PORISMode("FilterMode_TFBlue")
		self.mdFilterMode_TFRed = PORISMode("FilterMode_TFRed")
		self.vlClassicFilters_HAlpha = PORISValue("ClassicFilters_HAlpha")
		self.vlClassicFilters_Fe1 = PORISValue("ClassicFilters_Fe1")
		self.mdClassicFiltersMode_Standard = PORISMode("ClassicFiltersMode_Standard")
		self.mdClassicFiltersMode_Blue = PORISMode("ClassicFiltersMode_Blue")
		self.mdClassicFiltersMode_Red = PORISMode("ClassicFiltersMode_Red")
		self.vlClassicFilters_userFilter = PORISValueText("ClassicFilters_userFilter")
		self.mdClassicFiltersMode_User = PORISMode("ClassicFiltersMode_User")
		self.mdInstrumentMode_LSSlit = PORISMode("InstrumentMode_LSSlit")
		self.mdSlicerMode_Disabled = PORISMode("SlicerMode_Disabled")
		self.mdSlicerMode_Enabled = PORISMode("SlicerMode_Enabled")
		self.vlDoblador_0 = PORISValue("Doblador_0")
		self.vlDoblador_90 = PORISValue("Doblador_90")
		self.mdDobladorMode_Slicer = PORISMode("DobladorMode_Slicer")
		self.mdDobladorMode_NoSlicer = PORISMode("DobladorMode_NoSlicer")
		self.mdInstrumentMode_Bias = PORISMode("InstrumentMode_Bias")
		self.mdInstrumentMode_Flat = PORISMode("InstrumentMode_Flat")
		self.mdOperatorMode_Ciencia = PORISMode("OperatorMode_Ciencia")
		self.mdOperatorMode_Calibracion = PORISMode("OperatorMode_Calibracion")
		self.mdEngineerMode_Operator = PORISMode("EngineerMode_Operator")
		self.mdEngineerMode_Engineering = PORISMode("EngineerMode_Engineering")
		self.mdOperatorMode_Engineering = PORISMode("OperatorMode_Engineering")
		self.mdInstrumentMode_Engineering = PORISMode("InstrumentMode_Engineering")
		self.mdDetectorMode_Engineering = PORISMode("DetectorMode_Engineering")
		self.mdFilterMode_Engineering = PORISMode("FilterMode_Engineering")
		self.mdSlicerMode_Engineering = PORISMode("SlicerMode_Engineering")

		self.sysEngineer.id = idcounter
		idcounter += 1
		self.sysEngineer.ident = "Engineer"
		self.sysEngineer.description = ""

		self.mdEngineerMode_UNKNOWN.id = idcounter
		idcounter += 1
		self.mdEngineerMode_UNKNOWN.ident = "EngineerMode_UNKNOWN"
		self.mdEngineerMode_UNKNOWN.description = ""
		self.sysEngineer.addMode(self.mdEngineerMode_UNKNOWN)

		self.sysOperator.id = idcounter
		idcounter += 1
		self.sysOperator.ident = "Operator"
		self.sysOperator.description = ""
		self.sysEngineer.addSubsystem(self.sysOperator)

		self.mdOperatorMode_UNKNOWN.id = idcounter
		idcounter += 1
		self.mdOperatorMode_UNKNOWN.ident = "OperatorMode_UNKNOWN"
		self.mdOperatorMode_UNKNOWN.description = ""
		self.sysOperator.addMode(self.mdOperatorMode_UNKNOWN)

		self.sysInstrument.id = idcounter
		idcounter += 1
		self.sysInstrument.ident = "Instrument"
		self.sysInstrument.description = ""
		self.sysOperator.addSubsystem(self.sysInstrument)

		self.mdInstrumentMode_UNKNOWN.id = idcounter
		idcounter += 1
		self.mdInstrumentMode_UNKNOWN.ident = "InstrumentMode_UNKNOWN"
		self.mdInstrumentMode_UNKNOWN.description = ""
		self.sysInstrument.addMode(self.mdInstrumentMode_UNKNOWN)

		self.prMasks.id = idcounter
		idcounter += 1
		self.prMasks.ident = "Masks"
		self.prMasks.description = ""
		self.sysInstrument.addParam(self.prMasks)

		self.vlMasks_UNKNOWN.id = idcounter
		idcounter += 1
		self.vlMasks_UNKNOWN.ident = "Masks_UNKNOWN"
		self.vlMasks_UNKNOWN.description = "Unknown value for Masks"
		self.prMasks.addValue(self.vlMasks_UNKNOWN)

		self.mdMasksMode_UNKNOWN.id = idcounter
		idcounter += 1
		self.mdMasksMode_UNKNOWN.ident = "MasksMode_UNKNOWN"
		self.mdMasksMode_UNKNOWN.description = "Unknown mode for Masks"
		self.prMasks.addMode(self.mdMasksMode_UNKNOWN)
		self.mdMasksMode_UNKNOWN.addValue(self.vlMasks_UNKNOWN)
		self.mdInstrumentMode_UNKNOWN.addSubMode(self.mdMasksMode_UNKNOWN)

		self.prDispersion.id = idcounter
		idcounter += 1
		self.prDispersion.ident = "Dispersion"
		self.prDispersion.description = ""
		self.sysInstrument.addParam(self.prDispersion)

		self.vlDispersion_UNKNOWN.id = idcounter
		idcounter += 1
		self.vlDispersion_UNKNOWN.ident = "Dispersion_UNKNOWN"
		self.vlDispersion_UNKNOWN.description = "Unknown value for Dispersion"
		self.prDispersion.addValue(self.vlDispersion_UNKNOWN)

		self.mdDispersionMode_UNKNOWN.id = idcounter
		idcounter += 1
		self.mdDispersionMode_UNKNOWN.ident = "DispersionMode_UNKNOWN"
		self.mdDispersionMode_UNKNOWN.description = "Unknown mode for Dispersion"
		self.prDispersion.addMode(self.mdDispersionMode_UNKNOWN)
		self.mdDispersionMode_UNKNOWN.addValue(self.vlDispersion_UNKNOWN)
		self.mdInstrumentMode_UNKNOWN.addSubMode(self.mdDispersionMode_UNKNOWN)

		self.sysDetector.id = idcounter
		idcounter += 1
		self.sysDetector.ident = "Detector"
		self.sysDetector.description = ""
		self.sysInstrument.addSubsystem(self.sysDetector)

		self.mdDetectorMode_UNKNOWN.id = idcounter
		idcounter += 1
		self.mdDetectorMode_UNKNOWN.ident = "DetectorMode_UNKNOWN"
		self.mdDetectorMode_UNKNOWN.description = ""
		self.sysDetector.addMode(self.mdDetectorMode_UNKNOWN)

		self.prexpTime.id = idcounter
		idcounter += 1
		self.prexpTime.ident = "expTime"
		self.prexpTime.description = ""
		self.sysDetector.addParam(self.prexpTime)

		self.vlexpTime_UNKNOWN.id = idcounter
		idcounter += 1
		self.vlexpTime_UNKNOWN.ident = "expTime_UNKNOWN"
		self.vlexpTime_UNKNOWN.description = "Unknown value for expTime"
		self.prexpTime.addValue(self.vlexpTime_UNKNOWN)

		self.mdexpTimeMode_UNKNOWN.id = idcounter
		idcounter += 1
		self.mdexpTimeMode_UNKNOWN.ident = "expTimeMode_UNKNOWN"
		self.mdexpTimeMode_UNKNOWN.description = "Unknown mode for expTime"
		self.prexpTime.addMode(self.mdexpTimeMode_UNKNOWN)
		self.mdexpTimeMode_UNKNOWN.addValue(self.vlexpTime_UNKNOWN)
		self.mdDetectorMode_UNKNOWN.addSubMode(self.mdexpTimeMode_UNKNOWN)

		self.prBinning.id = idcounter
		idcounter += 1
		self.prBinning.ident = "Binning"
		self.prBinning.description = ""
		self.sysDetector.addParam(self.prBinning)

		self.vlBinning_UNKNOWN.id = idcounter
		idcounter += 1
		self.vlBinning_UNKNOWN.ident = "Binning_UNKNOWN"
		self.vlBinning_UNKNOWN.description = "Unknown value for Binning"
		self.prBinning.addValue(self.vlBinning_UNKNOWN)

		self.mdBinningMode_UNKNOWN.id = idcounter
		idcounter += 1
		self.mdBinningMode_UNKNOWN.ident = "BinningMode_UNKNOWN"
		self.mdBinningMode_UNKNOWN.description = "Unknown mode for Binning"
		self.prBinning.addMode(self.mdBinningMode_UNKNOWN)
		self.mdBinningMode_UNKNOWN.addValue(self.vlBinning_UNKNOWN)
		self.mdDetectorMode_UNKNOWN.addSubMode(self.mdBinningMode_UNKNOWN)

		self.sysFilter.id = idcounter
		idcounter += 1
		self.sysFilter.ident = "Filter"
		self.sysFilter.description = ""
		self.sysInstrument.addSubsystem(self.sysFilter)

		self.mdFilterMode_UNKNOWN.id = idcounter
		idcounter += 1
		self.mdFilterMode_UNKNOWN.ident = "FilterMode_UNKNOWN"
		self.mdFilterMode_UNKNOWN.description = ""
		self.sysFilter.addMode(self.mdFilterMode_UNKNOWN)

		self.prClassicFilters.id = idcounter
		idcounter += 1
		self.prClassicFilters.ident = "ClassicFilters"
		self.prClassicFilters.description = ""
		self.sysFilter.addParam(self.prClassicFilters)

		self.vlClassicFilters_UNKNOWN.id = idcounter
		idcounter += 1
		self.vlClassicFilters_UNKNOWN.ident = "ClassicFilters_UNKNOWN"
		self.vlClassicFilters_UNKNOWN.description = "Unknown value for ClassicFilters"
		self.prClassicFilters.addValue(self.vlClassicFilters_UNKNOWN)

		self.mdClassicFiltersMode_UNKNOWN.id = idcounter
		idcounter += 1
		self.mdClassicFiltersMode_UNKNOWN.ident = "ClassicFiltersMode_UNKNOWN"
		self.mdClassicFiltersMode_UNKNOWN.description = "Unknown mode for ClassicFilters"
		self.prClassicFilters.addMode(self.mdClassicFiltersMode_UNKNOWN)
		self.mdClassicFiltersMode_UNKNOWN.addValue(self.vlClassicFilters_UNKNOWN)
		self.mdFilterMode_UNKNOWN.addSubMode(self.mdClassicFiltersMode_UNKNOWN)

		self.sysSlicer.id = idcounter
		idcounter += 1
		self.sysSlicer.ident = "Slicer"
		self.sysSlicer.description = ""
		self.sysInstrument.addSubsystem(self.sysSlicer)

		self.mdSlicerMode_UNKNOWN.id = idcounter
		idcounter += 1
		self.mdSlicerMode_UNKNOWN.ident = "SlicerMode_UNKNOWN"
		self.mdSlicerMode_UNKNOWN.description = ""
		self.sysSlicer.addMode(self.mdSlicerMode_UNKNOWN)

		self.prDoblador.id = idcounter
		idcounter += 1
		self.prDoblador.ident = "Doblador"
		self.prDoblador.description = ""
		self.sysSlicer.addParam(self.prDoblador)

		self.vlDoblador_UNKNOWN.id = idcounter
		idcounter += 1
		self.vlDoblador_UNKNOWN.ident = "Doblador_UNKNOWN"
		self.vlDoblador_UNKNOWN.description = "Unknown value for Doblador"
		self.prDoblador.addValue(self.vlDoblador_UNKNOWN)

		self.mdDobladorMode_UNKNOWN.id = idcounter
		idcounter += 1
		self.mdDobladorMode_UNKNOWN.ident = "DobladorMode_UNKNOWN"
		self.mdDobladorMode_UNKNOWN.description = "Unknown mode for Doblador"
		self.prDoblador.addMode(self.mdDobladorMode_UNKNOWN)
		self.mdDobladorMode_UNKNOWN.addValue(self.vlDoblador_UNKNOWN)
		self.mdSlicerMode_UNKNOWN.addSubMode(self.mdDobladorMode_UNKNOWN)

		self.vlMasks_0_6.id = idcounter
		idcounter += 1
		self.vlMasks_0_6.ident = "Masks_0_6"
		self.vlMasks_0_6.description = ""
		self.prMasks.addValue(self.vlMasks_0_6)

		self.vlMasks_1_0.id = idcounter
		idcounter += 1
		self.vlMasks_1_0.ident = "Masks_1_0"
		self.vlMasks_1_0.description = ""
		self.prMasks.addValue(self.vlMasks_1_0)

		self.vlMasks_2_0.id = idcounter
		idcounter += 1
		self.vlMasks_2_0.ident = "Masks_2_0"
		self.vlMasks_2_0.description = ""
		self.prMasks.addValue(self.vlMasks_2_0)

		self.mdMasksMode_Spectroscopy.id = idcounter
		idcounter += 1
		self.mdMasksMode_Spectroscopy.ident = "MasksMode_Spectroscopy"
		self.mdMasksMode_Spectroscopy.description = ""
		self.prMasks.addMode(self.mdMasksMode_Spectroscopy)

		self.vlMasks_Half_field.id = idcounter
		idcounter += 1
		self.vlMasks_Half_field.ident = "Masks_Half_field"
		self.vlMasks_Half_field.description = ""
		self.prMasks.addValue(self.vlMasks_Half_field)

		self.mdMasksMode_FastImg.id = idcounter
		idcounter += 1
		self.mdMasksMode_FastImg.ident = "MasksMode_FastImg"
		self.mdMasksMode_FastImg.description = ""
		self.prMasks.addMode(self.mdMasksMode_FastImg)

		self.mdMasksMode_Slicer.id = idcounter
		idcounter += 1
		self.mdMasksMode_Slicer.ident = "MasksMode_Slicer"
		self.mdMasksMode_Slicer.description = ""
		self.prMasks.addMode(self.mdMasksMode_Slicer)

		self.vlMasks_SlicerMask.id = idcounter
		idcounter += 1
		self.vlMasks_SlicerMask.ident = "Masks_SlicerMask"
		self.vlMasks_SlicerMask.description = ""
		self.prMasks.addValue(self.vlMasks_SlicerMask)

		self.mdMasksMode_Passthrough.id = idcounter
		idcounter += 1
		self.mdMasksMode_Passthrough.ident = "MasksMode_Passthrough"
		self.mdMasksMode_Passthrough.description = ""
		self.prMasks.addMode(self.mdMasksMode_Passthrough)

		self.vlDispersion_R500.id = idcounter
		idcounter += 1
		self.vlDispersion_R500.ident = "Dispersion_R500"
		self.vlDispersion_R500.description = ""
		self.prDispersion.addValue(self.vlDispersion_R500)

		self.vlDispersion_R1000.id = idcounter
		idcounter += 1
		self.vlDispersion_R1000.ident = "Dispersion_R1000"
		self.vlDispersion_R1000.description = ""
		self.prDispersion.addValue(self.vlDispersion_R1000)

		self.vlDispersion_R2000.id = idcounter
		idcounter += 1
		self.vlDispersion_R2000.ident = "Dispersion_R2000"
		self.vlDispersion_R2000.description = ""
		self.prDispersion.addValue(self.vlDispersion_R2000)

		self.mdDispersionMode_Normal.id = idcounter
		idcounter += 1
		self.mdDispersionMode_Normal.ident = "DispersionMode_Normal"
		self.mdDispersionMode_Normal.description = ""
		self.prDispersion.addMode(self.mdDispersionMode_Normal)

		self.vlexpTime_NormalRange.id = idcounter
		idcounter += 1
		self.vlexpTime_NormalRange.ident = "expTime_NormalRange"
		self.vlexpTime_NormalRange.description = ""
		self.vlexpTime_NormalRange.min = 0
		self.vlexpTime_NormalRange.default_data = 1
		self.vlexpTime_NormalRange.max = 3600
		self.prexpTime.addValue(self.vlexpTime_NormalRange)

		self.mdexpTimeMode_Normal.id = idcounter
		idcounter += 1
		self.mdexpTimeMode_Normal.ident = "expTimeMode_Normal"
		self.mdexpTimeMode_Normal.description = ""
		self.prexpTime.addMode(self.mdexpTimeMode_Normal)

		self.mdexpTimeMode_Fast.id = idcounter
		idcounter += 1
		self.mdexpTimeMode_Fast.ident = "expTimeMode_Fast"
		self.mdexpTimeMode_Fast.description = ""
		self.prexpTime.addMode(self.mdexpTimeMode_Fast)

		self.vlexpTime_FastRange.id = idcounter
		idcounter += 1
		self.vlexpTime_FastRange.ident = "expTime_FastRange"
		self.vlexpTime_FastRange.description = ""
		self.vlexpTime_FastRange.min = 0
		self.vlexpTime_FastRange.default_data = 0.01
		self.vlexpTime_FastRange.max = 0.5
		self.prexpTime.addValue(self.vlexpTime_FastRange)

		self.vlBinning_1x1.id = idcounter
		idcounter += 1
		self.vlBinning_1x1.ident = "Binning_1x1"
		self.vlBinning_1x1.description = ""
		self.prBinning.addValue(self.vlBinning_1x1)

		self.vlBinning_2x1.id = idcounter
		idcounter += 1
		self.vlBinning_2x1.ident = "Binning_2x1"
		self.vlBinning_2x1.description = ""
		self.prBinning.addValue(self.vlBinning_2x1)

		self.vlBinning_1x2.id = idcounter
		idcounter += 1
		self.vlBinning_1x2.ident = "Binning_1x2"
		self.vlBinning_1x2.description = ""
		self.prBinning.addValue(self.vlBinning_1x2)

		self.vlBinning_2x2.id = idcounter
		idcounter += 1
		self.vlBinning_2x2.ident = "Binning_2x2"
		self.vlBinning_2x2.description = ""
		self.prBinning.addValue(self.vlBinning_2x2)

		self.mdBinningMode_Normal.id = idcounter
		idcounter += 1
		self.mdBinningMode_Normal.ident = "BinningMode_Normal"
		self.mdBinningMode_Normal.description = ""
		self.prBinning.addMode(self.mdBinningMode_Normal)

		self.mdBinningMode_Square.id = idcounter
		idcounter += 1
		self.mdBinningMode_Square.ident = "BinningMode_Square"
		self.mdBinningMode_Square.description = ""
		self.prBinning.addMode(self.mdBinningMode_Square)

		self.mdBinningMode_Fast.id = idcounter
		idcounter += 1
		self.mdBinningMode_Fast.ident = "BinningMode_Fast"
		self.mdBinningMode_Fast.description = ""
		self.prBinning.addMode(self.mdBinningMode_Fast)

		self.mdDetectorMode_Normal.id = idcounter
		idcounter += 1
		self.mdDetectorMode_Normal.ident = "DetectorMode_Normal"
		self.mdDetectorMode_Normal.description = ""
		self.sysDetector.addMode(self.mdDetectorMode_Normal)

		self.mdDetectorMode_Image.id = idcounter
		idcounter += 1
		self.mdDetectorMode_Image.ident = "DetectorMode_Image"
		self.mdDetectorMode_Image.description = ""
		self.sysDetector.addMode(self.mdDetectorMode_Image)

		self.mdDetectorMode_FastImage.id = idcounter
		idcounter += 1
		self.mdDetectorMode_FastImage.ident = "DetectorMode_FastImage"
		self.mdDetectorMode_FastImage.description = ""
		self.sysDetector.addMode(self.mdDetectorMode_FastImage)

		self.mdInstrumentMode_Photometry.id = idcounter
		idcounter += 1
		self.mdInstrumentMode_Photometry.ident = "InstrumentMode_Photometry"
		self.mdInstrumentMode_Photometry.description = ""
		self.sysInstrument.addMode(self.mdInstrumentMode_Photometry)

		self.mdInstrumentMode_SlicerSpec.id = idcounter
		idcounter += 1
		self.mdInstrumentMode_SlicerSpec.ident = "InstrumentMode_SlicerSpec"
		self.mdInstrumentMode_SlicerSpec.description = ""
		self.sysInstrument.addMode(self.mdInstrumentMode_SlicerSpec)

		self.mdInstrumentMode_FastPhotometry.id = idcounter
		idcounter += 1
		self.mdInstrumentMode_FastPhotometry.ident = "InstrumentMode_FastPhotometry"
		self.mdInstrumentMode_FastPhotometry.description = ""
		self.sysInstrument.addMode(self.mdInstrumentMode_FastPhotometry)

		self.mdFilterMode_Classic.id = idcounter
		idcounter += 1
		self.mdFilterMode_Classic.ident = "FilterMode_Classic"
		self.mdFilterMode_Classic.description = ""
		self.sysFilter.addMode(self.mdFilterMode_Classic)

		self.mdFilterMode_TFBlue.id = idcounter
		idcounter += 1
		self.mdFilterMode_TFBlue.ident = "FilterMode_TFBlue"
		self.mdFilterMode_TFBlue.description = ""
		self.sysFilter.addMode(self.mdFilterMode_TFBlue)

		self.mdFilterMode_TFRed.id = idcounter
		idcounter += 1
		self.mdFilterMode_TFRed.ident = "FilterMode_TFRed"
		self.mdFilterMode_TFRed.description = ""
		self.sysFilter.addMode(self.mdFilterMode_TFRed)

		self.vlClassicFilters_HAlpha.id = idcounter
		idcounter += 1
		self.vlClassicFilters_HAlpha.ident = "ClassicFilters_HAlpha"
		self.vlClassicFilters_HAlpha.description = ""
		self.prClassicFilters.addValue(self.vlClassicFilters_HAlpha)

		self.vlClassicFilters_Fe1.id = idcounter
		idcounter += 1
		self.vlClassicFilters_Fe1.ident = "ClassicFilters_Fe1"
		self.vlClassicFilters_Fe1.description = ""
		self.prClassicFilters.addValue(self.vlClassicFilters_Fe1)

		self.mdClassicFiltersMode_Standard.id = idcounter
		idcounter += 1
		self.mdClassicFiltersMode_Standard.ident = "ClassicFiltersMode_Standard"
		self.mdClassicFiltersMode_Standard.description = ""
		self.prClassicFilters.addMode(self.mdClassicFiltersMode_Standard)

		self.mdClassicFiltersMode_Blue.id = idcounter
		idcounter += 1
		self.mdClassicFiltersMode_Blue.ident = "ClassicFiltersMode_Blue"
		self.mdClassicFiltersMode_Blue.description = ""
		self.prClassicFilters.addMode(self.mdClassicFiltersMode_Blue)

		self.mdClassicFiltersMode_Red.id = idcounter
		idcounter += 1
		self.mdClassicFiltersMode_Red.ident = "ClassicFiltersMode_Red"
		self.mdClassicFiltersMode_Red.description = ""
		self.prClassicFilters.addMode(self.mdClassicFiltersMode_Red)

		self.vlClassicFilters_userFilter.id = idcounter
		idcounter += 1
		self.vlClassicFilters_userFilter.ident = "ClassicFilters_userFilter"
		self.vlClassicFilters_userFilter.description = ""
		self.prClassicFilters.addValue(self.vlClassicFilters_userFilter)

		self.mdClassicFiltersMode_User.id = idcounter
		idcounter += 1
		self.mdClassicFiltersMode_User.ident = "ClassicFiltersMode_User"
		self.mdClassicFiltersMode_User.description = ""
		self.prClassicFilters.addMode(self.mdClassicFiltersMode_User)

		self.mdInstrumentMode_LSSlit.id = idcounter
		idcounter += 1
		self.mdInstrumentMode_LSSlit.ident = "InstrumentMode_LSSlit"
		self.mdInstrumentMode_LSSlit.description = ""
		self.sysInstrument.addMode(self.mdInstrumentMode_LSSlit)

		self.mdSlicerMode_Disabled.id = idcounter
		idcounter += 1
		self.mdSlicerMode_Disabled.ident = "SlicerMode_Disabled"
		self.mdSlicerMode_Disabled.description = ""
		self.sysSlicer.addMode(self.mdSlicerMode_Disabled)

		self.mdSlicerMode_Enabled.id = idcounter
		idcounter += 1
		self.mdSlicerMode_Enabled.ident = "SlicerMode_Enabled"
		self.mdSlicerMode_Enabled.description = ""
		self.sysSlicer.addMode(self.mdSlicerMode_Enabled)

		self.vlDoblador_0.id = idcounter
		idcounter += 1
		self.vlDoblador_0.ident = "Doblador_0"
		self.vlDoblador_0.description = ""
		self.prDoblador.addValue(self.vlDoblador_0)

		self.vlDoblador_90.id = idcounter
		idcounter += 1
		self.vlDoblador_90.ident = "Doblador_90"
		self.vlDoblador_90.description = ""
		self.prDoblador.addValue(self.vlDoblador_90)

		self.mdDobladorMode_Slicer.id = idcounter
		idcounter += 1
		self.mdDobladorMode_Slicer.ident = "DobladorMode_Slicer"
		self.mdDobladorMode_Slicer.description = ""
		self.prDoblador.addMode(self.mdDobladorMode_Slicer)

		self.mdDobladorMode_NoSlicer.id = idcounter
		idcounter += 1
		self.mdDobladorMode_NoSlicer.ident = "DobladorMode_NoSlicer"
		self.mdDobladorMode_NoSlicer.description = ""
		self.prDoblador.addMode(self.mdDobladorMode_NoSlicer)

		self.mdInstrumentMode_Bias.id = idcounter
		idcounter += 1
		self.mdInstrumentMode_Bias.ident = "InstrumentMode_Bias"
		self.mdInstrumentMode_Bias.description = ""
		self.sysInstrument.addMode(self.mdInstrumentMode_Bias)

		self.mdInstrumentMode_Flat.id = idcounter
		idcounter += 1
		self.mdInstrumentMode_Flat.ident = "InstrumentMode_Flat"
		self.mdInstrumentMode_Flat.description = ""
		self.sysInstrument.addMode(self.mdInstrumentMode_Flat)

		self.mdOperatorMode_Ciencia.id = idcounter
		idcounter += 1
		self.mdOperatorMode_Ciencia.ident = "OperatorMode_Ciencia"
		self.mdOperatorMode_Ciencia.description = ""
		self.sysOperator.addMode(self.mdOperatorMode_Ciencia)

		self.mdOperatorMode_Calibracion.id = idcounter
		idcounter += 1
		self.mdOperatorMode_Calibracion.ident = "OperatorMode_Calibracion"
		self.mdOperatorMode_Calibracion.description = ""
		self.sysOperator.addMode(self.mdOperatorMode_Calibracion)

		self.mdEngineerMode_Operator.id = idcounter
		idcounter += 1
		self.mdEngineerMode_Operator.ident = "EngineerMode_Operator"
		self.mdEngineerMode_Operator.description = ""
		self.sysEngineer.addMode(self.mdEngineerMode_Operator)

		self.mdEngineerMode_Engineering.id = idcounter
		idcounter += 1
		self.mdEngineerMode_Engineering.ident = "EngineerMode_Engineering"
		self.mdEngineerMode_Engineering.description = "Engineer engineering mode"
		self.sysEngineer.addMode(self.mdEngineerMode_Engineering)

		self.mdOperatorMode_Engineering.id = idcounter
		idcounter += 1
		self.mdOperatorMode_Engineering.ident = "OperatorMode_Engineering"
		self.mdOperatorMode_Engineering.description = "Operator engineering mode"
		self.sysOperator.addMode(self.mdOperatorMode_Engineering)

		self.mdInstrumentMode_Engineering.id = idcounter
		idcounter += 1
		self.mdInstrumentMode_Engineering.ident = "InstrumentMode_Engineering"
		self.mdInstrumentMode_Engineering.description = "Instrument engineering mode"
		self.sysInstrument.addMode(self.mdInstrumentMode_Engineering)

		self.mdDetectorMode_Engineering.id = idcounter
		idcounter += 1
		self.mdDetectorMode_Engineering.ident = "DetectorMode_Engineering"
		self.mdDetectorMode_Engineering.description = "Detector engineering mode"
		self.sysDetector.addMode(self.mdDetectorMode_Engineering)

		self.mdFilterMode_Engineering.id = idcounter
		idcounter += 1
		self.mdFilterMode_Engineering.ident = "FilterMode_Engineering"
		self.mdFilterMode_Engineering.description = "Filter engineering mode"
		self.sysFilter.addMode(self.mdFilterMode_Engineering)

		self.mdSlicerMode_Engineering.id = idcounter
		idcounter += 1
		self.mdSlicerMode_Engineering.ident = "SlicerMode_Engineering"
		self.mdSlicerMode_Engineering.description = "Slicer engineering mode"
		self.sysSlicer.addMode(self.mdSlicerMode_Engineering)
		# Marcamos OperatorMode_Ciencia como elegible para EngineerMode_Operator
		self.mdEngineerMode_Operator.addSubMode(self.mdOperatorMode_Ciencia)
		# Marcamos OperatorMode_Calibracion como elegible para EngineerMode_Operator
		self.mdEngineerMode_Operator.addSubMode(self.mdOperatorMode_Calibracion)
		# Marcamos OperatorMode_Ciencia como elegible para EngineerMode_Engineering
		self.mdEngineerMode_Engineering.addSubMode(self.mdOperatorMode_Ciencia)
		# Marcamos OperatorMode_Calibracion como elegible para EngineerMode_Engineering
		self.mdEngineerMode_Engineering.addSubMode(self.mdOperatorMode_Calibracion)
		# Marcamos OperatorMode_Engineering como elegible para EngineerMode_Engineering
		self.mdEngineerMode_Engineering.addSubMode(self.mdOperatorMode_Engineering)
		# Marcamos InstrumentMode_LSSlit como elegible para OperatorMode_Ciencia
		self.mdOperatorMode_Ciencia.addSubMode(self.mdInstrumentMode_LSSlit)
		# Marcamos InstrumentMode_FastPhotometry como elegible para OperatorMode_Ciencia
		self.mdOperatorMode_Ciencia.addSubMode(self.mdInstrumentMode_FastPhotometry)
		# Marcamos InstrumentMode_SlicerSpec como elegible para OperatorMode_Ciencia
		self.mdOperatorMode_Ciencia.addSubMode(self.mdInstrumentMode_SlicerSpec)
		# Marcamos InstrumentMode_Photometry como elegible para OperatorMode_Ciencia
		self.mdOperatorMode_Ciencia.addSubMode(self.mdInstrumentMode_Photometry)
		# Marcamos InstrumentMode_Bias como elegible para OperatorMode_Calibracion
		self.mdOperatorMode_Calibracion.addSubMode(self.mdInstrumentMode_Bias)
		# Marcamos InstrumentMode_Flat como elegible para OperatorMode_Calibracion
		self.mdOperatorMode_Calibracion.addSubMode(self.mdInstrumentMode_Flat)
		# Marcamos InstrumentMode_Photometry como elegible para OperatorMode_Engineering
		self.mdOperatorMode_Engineering.addSubMode(self.mdInstrumentMode_Photometry)
		# Marcamos InstrumentMode_SlicerSpec como elegible para OperatorMode_Engineering
		self.mdOperatorMode_Engineering.addSubMode(self.mdInstrumentMode_SlicerSpec)
		# Marcamos InstrumentMode_FastPhotometry como elegible para OperatorMode_Engineering
		self.mdOperatorMode_Engineering.addSubMode(self.mdInstrumentMode_FastPhotometry)
		# Marcamos InstrumentMode_LSSlit como elegible para OperatorMode_Engineering
		self.mdOperatorMode_Engineering.addSubMode(self.mdInstrumentMode_LSSlit)
		# Marcamos InstrumentMode_Bias como elegible para OperatorMode_Engineering
		self.mdOperatorMode_Engineering.addSubMode(self.mdInstrumentMode_Bias)
		# Marcamos InstrumentMode_Flat como elegible para OperatorMode_Engineering
		self.mdOperatorMode_Engineering.addSubMode(self.mdInstrumentMode_Flat)
		# Marcamos InstrumentMode_Engineering como elegible para OperatorMode_Engineering
		self.mdOperatorMode_Engineering.addSubMode(self.mdInstrumentMode_Engineering)
		# Marcamos MasksMode_Passthrough como elegible para InstrumentMode_Photometry
		self.mdInstrumentMode_Photometry.addSubMode(self.mdMasksMode_Passthrough)
		# Marcamos MasksMode_FastImg como elegible para InstrumentMode_FastPhotometry
		self.mdInstrumentMode_FastPhotometry.addSubMode(self.mdMasksMode_FastImg)
		# Marcamos MasksMode_Spectroscopy como elegible para InstrumentMode_LSSlit
		self.mdInstrumentMode_LSSlit.addSubMode(self.mdMasksMode_Spectroscopy)
		# Marcamos MasksMode_Passthrough como elegible para InstrumentMode_Bias
		self.mdInstrumentMode_Bias.addSubMode(self.mdMasksMode_Passthrough)
		# Marcamos MasksMode_Passthrough como elegible para InstrumentMode_Flat
		self.mdInstrumentMode_Flat.addSubMode(self.mdMasksMode_Passthrough)
		# Marcamos MasksMode_Spectroscopy como elegible para InstrumentMode_Engineering
		self.mdInstrumentMode_Engineering.addSubMode(self.mdMasksMode_Spectroscopy)
		# Marcamos MasksMode_FastImg como elegible para InstrumentMode_Engineering
		self.mdInstrumentMode_Engineering.addSubMode(self.mdMasksMode_FastImg)
		# Marcamos MasksMode_Slicer como elegible para InstrumentMode_Engineering
		self.mdInstrumentMode_Engineering.addSubMode(self.mdMasksMode_Slicer)
		# Marcamos MasksMode_Passthrough como elegible para InstrumentMode_Engineering
		self.mdInstrumentMode_Engineering.addSubMode(self.mdMasksMode_Passthrough)
		# Marcamos Masks_0_6 como elegible para MasksMode_Spectroscopy
		self.mdMasksMode_Spectroscopy.addValue(self.vlMasks_0_6)
		# Marcamos Masks_2_0 como elegible para MasksMode_Spectroscopy
		self.mdMasksMode_Spectroscopy.addValue(self.vlMasks_2_0)
		# Marcamos Masks_1_0 como elegible para MasksMode_Spectroscopy
		self.mdMasksMode_Spectroscopy.addValue(self.vlMasks_1_0)
		# Marcamos Masks_Half_field como elegible para MasksMode_FastImg
		self.mdMasksMode_FastImg.addValue(self.vlMasks_Half_field)
		# Marcamos Masks_SlicerMask como elegible para MasksMode_Slicer
		self.mdMasksMode_Slicer.addValue(self.vlMasks_SlicerMask)
		# Marcamos DispersionMode_Normal como elegible para InstrumentMode_SlicerSpec
		self.mdInstrumentMode_SlicerSpec.addSubMode(self.mdDispersionMode_Normal)
		# Marcamos DispersionMode_Normal como elegible para InstrumentMode_LSSlit
		self.mdInstrumentMode_LSSlit.addSubMode(self.mdDispersionMode_Normal)
		# Marcamos DispersionMode_Normal como elegible para InstrumentMode_Engineering
		self.mdInstrumentMode_Engineering.addSubMode(self.mdDispersionMode_Normal)
		# Marcamos Dispersion_R500 como elegible para DispersionMode_Normal
		self.mdDispersionMode_Normal.addValue(self.vlDispersion_R500)
		# Marcamos Dispersion_R1000 como elegible para DispersionMode_Normal
		self.mdDispersionMode_Normal.addValue(self.vlDispersion_R1000)
		# Marcamos Dispersion_R2000 como elegible para DispersionMode_Normal
		self.mdDispersionMode_Normal.addValue(self.vlDispersion_R2000)
		# Marcamos DetectorMode_Image como elegible para InstrumentMode_Photometry
		self.mdInstrumentMode_Photometry.addSubMode(self.mdDetectorMode_Image)
		# Marcamos DetectorMode_Normal como elegible para InstrumentMode_SlicerSpec
		self.mdInstrumentMode_SlicerSpec.addSubMode(self.mdDetectorMode_Normal)
		# Marcamos DetectorMode_FastImage como elegible para InstrumentMode_FastPhotometry
		self.mdInstrumentMode_FastPhotometry.addSubMode(self.mdDetectorMode_FastImage)
		# Marcamos DetectorMode_Normal como elegible para InstrumentMode_LSSlit
		self.mdInstrumentMode_LSSlit.addSubMode(self.mdDetectorMode_Normal)
		# Marcamos DetectorMode_Image como elegible para InstrumentMode_Bias
		self.mdInstrumentMode_Bias.addSubMode(self.mdDetectorMode_Image)
		# Marcamos DetectorMode_Normal como elegible para InstrumentMode_Flat
		self.mdInstrumentMode_Flat.addSubMode(self.mdDetectorMode_Normal)
		# Marcamos DetectorMode_Normal como elegible para InstrumentMode_Engineering
		self.mdInstrumentMode_Engineering.addSubMode(self.mdDetectorMode_Normal)
		# Marcamos DetectorMode_Image como elegible para InstrumentMode_Engineering
		self.mdInstrumentMode_Engineering.addSubMode(self.mdDetectorMode_Image)
		# Marcamos DetectorMode_FastImage como elegible para InstrumentMode_Engineering
		self.mdInstrumentMode_Engineering.addSubMode(self.mdDetectorMode_FastImage)
		# Marcamos DetectorMode_Engineering como elegible para InstrumentMode_Engineering
		self.mdInstrumentMode_Engineering.addSubMode(self.mdDetectorMode_Engineering)
		# Marcamos expTimeMode_Normal como elegible para DetectorMode_Normal
		self.mdDetectorMode_Normal.addSubMode(self.mdexpTimeMode_Normal)
		# Marcamos expTimeMode_Normal como elegible para DetectorMode_Image
		self.mdDetectorMode_Image.addSubMode(self.mdexpTimeMode_Normal)
		# Marcamos expTimeMode_Fast como elegible para DetectorMode_FastImage
		self.mdDetectorMode_FastImage.addSubMode(self.mdexpTimeMode_Fast)
		# Marcamos expTimeMode_Normal como elegible para DetectorMode_Engineering
		self.mdDetectorMode_Engineering.addSubMode(self.mdexpTimeMode_Normal)
		# Marcamos expTimeMode_Fast como elegible para DetectorMode_Engineering
		self.mdDetectorMode_Engineering.addSubMode(self.mdexpTimeMode_Fast)
		# Marcamos expTime_NormalRange como elegible para expTimeMode_Normal
		self.mdexpTimeMode_Normal.addValue(self.vlexpTime_NormalRange)
		# Marcamos expTime_FastRange como elegible para expTimeMode_Fast
		self.mdexpTimeMode_Fast.addValue(self.vlexpTime_FastRange)
		# Marcamos BinningMode_Normal como elegible para DetectorMode_Normal
		self.mdDetectorMode_Normal.addSubMode(self.mdBinningMode_Normal)
		# Marcamos BinningMode_Square como elegible para DetectorMode_Image
		self.mdDetectorMode_Image.addSubMode(self.mdBinningMode_Square)
		# Marcamos BinningMode_Fast como elegible para DetectorMode_FastImage
		self.mdDetectorMode_FastImage.addSubMode(self.mdBinningMode_Fast)
		# Marcamos BinningMode_Normal como elegible para DetectorMode_Engineering
		self.mdDetectorMode_Engineering.addSubMode(self.mdBinningMode_Normal)
		# Marcamos BinningMode_Square como elegible para DetectorMode_Engineering
		self.mdDetectorMode_Engineering.addSubMode(self.mdBinningMode_Square)
		# Marcamos BinningMode_Fast como elegible para DetectorMode_Engineering
		self.mdDetectorMode_Engineering.addSubMode(self.mdBinningMode_Fast)
		# Marcamos Binning_1x1 como elegible para BinningMode_Normal
		self.mdBinningMode_Normal.addValue(self.vlBinning_1x1)
		# Marcamos Binning_2x1 como elegible para BinningMode_Normal
		self.mdBinningMode_Normal.addValue(self.vlBinning_2x1)
		# Marcamos Binning_1x2 como elegible para BinningMode_Normal
		self.mdBinningMode_Normal.addValue(self.vlBinning_1x2)
		# Marcamos Binning_2x2 como elegible para BinningMode_Normal
		self.mdBinningMode_Normal.addValue(self.vlBinning_2x2)
		# Marcamos Binning_1x1 como elegible para BinningMode_Square
		self.mdBinningMode_Square.addValue(self.vlBinning_1x1)
		# Marcamos Binning_2x2 como elegible para BinningMode_Square
		self.mdBinningMode_Square.addValue(self.vlBinning_2x2)
		# Marcamos Binning_2x2 como elegible para BinningMode_Fast
		self.mdBinningMode_Fast.addValue(self.vlBinning_2x2)
		# Marcamos FilterMode_TFRed como elegible para InstrumentMode_Photometry
		self.mdInstrumentMode_Photometry.addSubMode(self.mdFilterMode_TFRed)
		# Marcamos FilterMode_TFBlue como elegible para InstrumentMode_Photometry
		self.mdInstrumentMode_Photometry.addSubMode(self.mdFilterMode_TFBlue)
		# Marcamos FilterMode_Classic como elegible para InstrumentMode_Photometry
		self.mdInstrumentMode_Photometry.addSubMode(self.mdFilterMode_Classic)
		# Marcamos FilterMode_Classic como elegible para InstrumentMode_SlicerSpec
		self.mdInstrumentMode_SlicerSpec.addSubMode(self.mdFilterMode_Classic)
		# Marcamos FilterMode_TFRed como elegible para InstrumentMode_SlicerSpec
		self.mdInstrumentMode_SlicerSpec.addSubMode(self.mdFilterMode_TFRed)
		# Marcamos FilterMode_TFBlue como elegible para InstrumentMode_SlicerSpec
		self.mdInstrumentMode_SlicerSpec.addSubMode(self.mdFilterMode_TFBlue)
		# Marcamos FilterMode_Classic como elegible para InstrumentMode_FastPhotometry
		self.mdInstrumentMode_FastPhotometry.addSubMode(self.mdFilterMode_Classic)
		# Marcamos FilterMode_Classic como elegible para InstrumentMode_LSSlit
		self.mdInstrumentMode_LSSlit.addSubMode(self.mdFilterMode_Classic)
		# Marcamos FilterMode_TFRed como elegible para InstrumentMode_LSSlit
		self.mdInstrumentMode_LSSlit.addSubMode(self.mdFilterMode_TFRed)
		# Marcamos FilterMode_TFBlue como elegible para InstrumentMode_LSSlit
		self.mdInstrumentMode_LSSlit.addSubMode(self.mdFilterMode_TFBlue)
		# Marcamos FilterMode_Classic como elegible para InstrumentMode_Engineering
		self.mdInstrumentMode_Engineering.addSubMode(self.mdFilterMode_Classic)
		# Marcamos FilterMode_TFBlue como elegible para InstrumentMode_Engineering
		self.mdInstrumentMode_Engineering.addSubMode(self.mdFilterMode_TFBlue)
		# Marcamos FilterMode_TFRed como elegible para InstrumentMode_Engineering
		self.mdInstrumentMode_Engineering.addSubMode(self.mdFilterMode_TFRed)
		# Marcamos FilterMode_Engineering como elegible para InstrumentMode_Engineering
		self.mdInstrumentMode_Engineering.addSubMode(self.mdFilterMode_Engineering)
		# Marcamos ClassicFiltersMode_Standard como elegible para FilterMode_Classic
		self.mdFilterMode_Classic.addSubMode(self.mdClassicFiltersMode_Standard)
		# Marcamos ClassicFiltersMode_User como elegible para FilterMode_Classic
		self.mdFilterMode_Classic.addSubMode(self.mdClassicFiltersMode_User)
		# Marcamos ClassicFiltersMode_Blue como elegible para FilterMode_TFBlue
		self.mdFilterMode_TFBlue.addSubMode(self.mdClassicFiltersMode_Blue)
		# Marcamos ClassicFiltersMode_Red como elegible para FilterMode_TFRed
		self.mdFilterMode_TFRed.addSubMode(self.mdClassicFiltersMode_Red)
		# Marcamos ClassicFiltersMode_Standard como elegible para FilterMode_Engineering
		self.mdFilterMode_Engineering.addSubMode(self.mdClassicFiltersMode_Standard)
		# Marcamos ClassicFiltersMode_Blue como elegible para FilterMode_Engineering
		self.mdFilterMode_Engineering.addSubMode(self.mdClassicFiltersMode_Blue)
		# Marcamos ClassicFiltersMode_Red como elegible para FilterMode_Engineering
		self.mdFilterMode_Engineering.addSubMode(self.mdClassicFiltersMode_Red)
		# Marcamos ClassicFiltersMode_User como elegible para FilterMode_Engineering
		self.mdFilterMode_Engineering.addSubMode(self.mdClassicFiltersMode_User)
		# Marcamos ClassicFilters_HAlpha como elegible para ClassicFiltersMode_Standard
		self.mdClassicFiltersMode_Standard.addValue(self.vlClassicFilters_HAlpha)
		# Marcamos ClassicFilters_Fe1 como elegible para ClassicFiltersMode_Standard
		self.mdClassicFiltersMode_Standard.addValue(self.vlClassicFilters_Fe1)
		# Marcamos ClassicFilters_Fe1 como elegible para ClassicFiltersMode_Blue
		self.mdClassicFiltersMode_Blue.addValue(self.vlClassicFilters_Fe1)
		# Marcamos ClassicFilters_HAlpha como elegible para ClassicFiltersMode_Red
		self.mdClassicFiltersMode_Red.addValue(self.vlClassicFilters_HAlpha)
		# Marcamos ClassicFilters_userFilter como elegible para ClassicFiltersMode_User
		self.mdClassicFiltersMode_User.addValue(self.vlClassicFilters_userFilter)
		# Marcamos SlicerMode_Enabled como elegible para InstrumentMode_SlicerSpec
		self.mdInstrumentMode_SlicerSpec.addSubMode(self.mdSlicerMode_Enabled)
		# Marcamos SlicerMode_Disabled como elegible para InstrumentMode_LSSlit
		self.mdInstrumentMode_LSSlit.addSubMode(self.mdSlicerMode_Disabled)
		# Marcamos SlicerMode_Disabled como elegible para InstrumentMode_Engineering
		self.mdInstrumentMode_Engineering.addSubMode(self.mdSlicerMode_Disabled)
		# Marcamos SlicerMode_Enabled como elegible para InstrumentMode_Engineering
		self.mdInstrumentMode_Engineering.addSubMode(self.mdSlicerMode_Enabled)
		# Marcamos SlicerMode_Engineering como elegible para InstrumentMode_Engineering
		self.mdInstrumentMode_Engineering.addSubMode(self.mdSlicerMode_Engineering)
		# Marcamos DobladorMode_NoSlicer como elegible para SlicerMode_Disabled
		self.mdSlicerMode_Disabled.addSubMode(self.mdDobladorMode_NoSlicer)
		# Marcamos DobladorMode_Slicer como elegible para SlicerMode_Enabled
		self.mdSlicerMode_Enabled.addSubMode(self.mdDobladorMode_Slicer)
		# Marcamos DobladorMode_Slicer como elegible para SlicerMode_Engineering
		self.mdSlicerMode_Engineering.addSubMode(self.mdDobladorMode_Slicer)
		# Marcamos DobladorMode_NoSlicer como elegible para SlicerMode_Engineering
		self.mdSlicerMode_Engineering.addSubMode(self.mdDobladorMode_NoSlicer)
		# Marcamos Doblador_0 como elegible para DobladorMode_Slicer
		self.mdDobladorMode_Slicer.addValue(self.vlDoblador_0)
		# Marcamos Doblador_90 como elegible para DobladorMode_NoSlicer
		self.mdDobladorMode_NoSlicer.addValue(self.vlDoblador_90)

	#----------------------------------------------------------------------
	#  Specific methods
	#----------------------------------------------------------------------


	## EngineerMode 
	def get_EngineerMode(self)-> PORISMode:
		return self.sysEngineer.selectedMode

	def set_EngineerMode(self, mode: PORISMode)-> PORISMode :
		return self.sysEngineer.setMode(mode)


	## OperatorMode 
	def get_OperatorMode(self)-> PORISMode:
		return self.sysOperator.selectedMode

	def set_OperatorMode(self, mode: PORISMode)-> PORISMode :
		return self.sysOperator.setMode(mode)


	## InstrumentMode 
	def get_InstrumentMode(self)-> PORISMode:
		return self.sysInstrument.selectedMode

	def set_InstrumentMode(self, mode: PORISMode)-> PORISMode :
		return self.sysInstrument.setMode(mode)


	## prParam Masks 

	# Masks
	def get_Masks(self)-> PORISValue :
		return self.prMasks.selectedValue

	def set_Masks(self, value: PORISValue)-> PORISValue :
		return self.prMasks.setValue(value)


	## MasksMode 
	def get_MasksMode(self)-> PORISMode:
		return self.prMasks.selectedMode

	def set_MasksMode(self, mode: PORISMode)-> PORISMode :
		return self.prMasks.setMode(mode)


	## prParam Dispersion 

	# Dispersion
	def get_Dispersion(self)-> PORISValue :
		return self.prDispersion.selectedValue

	def set_Dispersion(self, value: PORISValue)-> PORISValue :
		return self.prDispersion.setValue(value)


	## DispersionMode 
	def get_DispersionMode(self)-> PORISMode:
		return self.prDispersion.selectedMode

	def set_DispersionMode(self, mode: PORISMode)-> PORISMode :
		return self.prDispersion.setMode(mode)


	## DetectorMode 
	def get_DetectorMode(self)-> PORISMode:
		return self.sysDetector.selectedMode

	def set_DetectorMode(self, mode: PORISMode)-> PORISMode :
		return self.sysDetector.setMode(mode)


	## prParam expTime 

	# expTime
	def get_expTime(self)-> PORISValue :
		return self.prexpTime.selectedValue

	def set_expTime(self, value: PORISValue)-> PORISValue :
		return self.prexpTime.setValue(value)


	## expTimeMode 
	def get_expTimeMode(self)-> PORISMode:
		return self.prexpTime.selectedMode

	def set_expTimeMode(self, mode: PORISMode)-> PORISMode :
		return self.prexpTime.setMode(mode)


	## prParam Detector 

	# expTimeDouble  
	def get_expTimeDouble(self)-> float :
		return self.prexpTime.selectedValue.getData()

	def set_expTimeDouble(self, data: float)-> float :
		return self.prexpTime.selectedValue.setData(data)


	## prParam Detector 

	# expTimeDouble  
	def get_expTimeDouble(self)-> float :
		return self.prexpTime.selectedValue.getData()

	def set_expTimeDouble(self, data: float)-> float :
		return self.prexpTime.selectedValue.setData(data)


	## prParam Binning 

	# Binning
	def get_Binning(self)-> PORISValue :
		return self.prBinning.selectedValue

	def set_Binning(self, value: PORISValue)-> PORISValue :
		return self.prBinning.setValue(value)


	## BinningMode 
	def get_BinningMode(self)-> PORISMode:
		return self.prBinning.selectedMode

	def set_BinningMode(self, mode: PORISMode)-> PORISMode :
		return self.prBinning.setMode(mode)


	## FilterMode 
	def get_FilterMode(self)-> PORISMode:
		return self.sysFilter.selectedMode

	def set_FilterMode(self, mode: PORISMode)-> PORISMode :
		return self.sysFilter.setMode(mode)


	## prParam ClassicFilters 

	# ClassicFilters
	def get_ClassicFilters(self)-> PORISValue :
		return self.prClassicFilters.selectedValue

	def set_ClassicFilters(self, value: PORISValue)-> PORISValue :
		return self.prClassicFilters.setValue(value)


	## ClassicFiltersMode 
	def get_ClassicFiltersMode(self)-> PORISMode:
		return self.prClassicFilters.selectedMode

	def set_ClassicFiltersMode(self, mode: PORISMode)-> PORISMode :
		return self.prClassicFilters.setMode(mode)


	## prParam Filter 

	# ClassicFiltersString #
	def get_ClassicFiltersString(self)-> str :
		return self.prClassicFilters.selectedValue.getData()

	def set_ClassicFiltersString(self, data: str)-> str :
		return self.prClassicFilters.selectedValue.setData(data)


	## SlicerMode 
	def get_SlicerMode(self)-> PORISMode:
		return self.sysSlicer.selectedMode

	def set_SlicerMode(self, mode: PORISMode)-> PORISMode :
		return self.sysSlicer.setMode(mode)


	## prParam Doblador 

	# Doblador
	def get_Doblador(self)-> PORISValue :
		return self.prDoblador.selectedValue

	def set_Doblador(self, value: PORISValue)-> PORISValue :
		return self.prDoblador.setValue(value)


	## DobladorMode 
	def get_DobladorMode(self)-> PORISMode:
		return self.prDoblador.selectedMode

	def set_DobladorMode(self, mode: PORISMode)-> PORISMode :
		return self.prDoblador.setMode(mode)

