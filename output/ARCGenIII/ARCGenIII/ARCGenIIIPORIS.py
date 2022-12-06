from PORIS import *

class ARCGenIIIPORIS:
    def __init__(self):
        idcounter = 1
        self.sysARCGenIII = PORISSys("ARCGenIII")
        self.mdARCGenIIIMode_UNKNOWN = PORISMode("ARCGenIIIMode_UNKNOWN")
        self.root = self.sysARCGenIII
        self.sysFirmware = PORISSys("Firmware")
        self.mdFirmwareMode_UNKNOWN = PORISMode("FirmwareMode_UNKNOWN")
        self.sysVariants = PORISSys("Variants")
        self.mdVariantsMode_UNKNOWN = PORISMode("VariantsMode_UNKNOWN")
        self.sysAcquisition = PORISSys("Acquisition")
        self.mdAcquisitionMode_UNKNOWN = PORISMode("AcquisitionMode_UNKNOWN")
        self.prShuffleLines = PORISParam("ShuffleLines")
        self.mdShuffleLinesMode_UNKNOWN = PORISMode("ShuffleLinesMode_UNKNOWN")
        self.vlShuffleLines_UNKNOWN = PORISValue("ShuffleLines_UNKNOWN")
        self.prShiftNumber = PORISParam("ShiftNumber")
        self.mdShiftNumberMode_UNKNOWN = PORISMode("ShiftNumberMode_UNKNOWN")
        self.vlShiftNumber_UNKNOWN = PORISValue("ShiftNumber_UNKNOWN")
        self.sysSubarrayFeature = PORISSys("SubarrayFeature")
        self.mdSubarrayFeatureMode_UNKNOWN = PORISMode("SubarrayFeatureMode_UNKNOWN")
        self.prCols = PORISParam("Cols")
        self.mdColsMode_UNKNOWN = PORISMode("ColsMode_UNKNOWN")
        self.vlCols_UNKNOWN = PORISValue("Cols_UNKNOWN")
        self.proffsetRow = PORISParam("offsetRow")
        self.mdoffsetRowMode_UNKNOWN = PORISMode("offsetRowMode_UNKNOWN")
        self.vloffsetRow_UNKNOWN = PORISValue("offsetRow_UNKNOWN")
        self.prRows = PORISParam("Rows")
        self.mdRowsMode_UNKNOWN = PORISMode("RowsMode_UNKNOWN")
        self.vlRows_UNKNOWN = PORISValue("Rows_UNKNOWN")
        self.proffsetCol = PORISParam("offsetCol")
        self.mdoffsetColMode_UNKNOWN = PORISMode("offsetColMode_UNKNOWN")
        self.vloffsetCol_UNKNOWN = PORISValue("offsetCol_UNKNOWN")
        self.sysExposureCtrl = PORISSys("ExposureCtrl")
        self.mdExposureCtrlMode_UNKNOWN = PORISMode("ExposureCtrlMode_UNKNOWN")
        self.sysOpenShutter = PORISSys("OpenShutter")
        self.mdOpenShutterMode_UNKNOWN = PORISMode("OpenShutterMode_UNKNOWN")
        self.prExpTime = PORISParam("ExpTime")
        self.mdExpTimeMode_UNKNOWN = PORISMode("ExpTimeMode_UNKNOWN")
        self.vlExpTime_UNKNOWN = PORISValue("ExpTime_UNKNOWN")
        self.sysPixelSpeed = PORISSys("PixelSpeed")
        self.mdPixelSpeedMode_UNKNOWN = PORISMode("PixelSpeedMode_UNKNOWN")
        self.prnumOfFrames = PORISParam("numOfFrames")
        self.mdnumOfFramesMode_UNKNOWN = PORISMode("numOfFramesMode_UNKNOWN")
        self.vlnumOfFrames_UNKNOWN = PORISValue("numOfFrames_UNKNOWN")
        self.prCalibGain = PORISParam("CalibGain")
        self.mdCalibGainMode_UNKNOWN = PORISMode("CalibGainMode_UNKNOWN")
        self.vlCalibGain_UNKNOWN = PORISValue("CalibGain_UNKNOWN")
        self.sysOutputSource = PORISSys("OutputSource")
        self.mdOutputSourceMode_UNKNOWN = PORISMode("OutputSourceMode_UNKNOWN")
        self.sysRecomposition = PORISSys("Recomposition")
        self.mdRecompositionMode_UNKNOWN = PORISMode("RecompositionMode_UNKNOWN")
        self.sysDimensions = PORISSys("Dimensions")
        self.mdDimensionsMode_UNKNOWN = PORISMode("DimensionsMode_UNKNOWN")
        self.pruiRows = PORISParam("uiRows")
        self.mduiRowsMode_UNKNOWN = PORISMode("uiRowsMode_UNKNOWN")
        self.vluiRows_UNKNOWN = PORISValue("uiRows_UNKNOWN")
        self.pruiCols = PORISParam("uiCols")
        self.mduiColsMode_UNKNOWN = PORISMode("uiColsMode_UNKNOWN")
        self.vluiCols_UNKNOWN = PORISValue("uiCols_UNKNOWN")
        self.prBinning = PORISParam("Binning")
        self.mdBinningMode_UNKNOWN = PORISMode("BinningMode_UNKNOWN")
        self.vlBinning_UNKNOWN = PORISValue("Binning_UNKNOWN")
        self.mdARCGenIIIMode_Real = PORISMode("ARCGenIIIMode_Real")
        self.mdARCGenIIIMode_Emulated = PORISMode("ARCGenIIIMode_Emulated")
        self.mdFirmwareMode_tim = PORISMode("FirmwareMode_tim")
        self.mdFirmwareMode_osiris2 = PORISMode("FirmwareMode_osiris2")
        self.mdFirmwareMode_osiris3 = PORISMode("FirmwareMode_osiris3")
        self.mdFirmwareMode_osiris4 = PORISMode("FirmwareMode_osiris4")
        self.mdFirmwareMode_osiris5 = PORISMode("FirmwareMode_osiris5")
        self.mdAcquisitionMode_Normal = PORISMode("AcquisitionMode_Normal")
        self.mdAcquisitionMode_FrameTransfer = PORISMode("AcquisitionMode_FrameTransfer")
        self.mdAcquisitionMode_Shuffling = PORISMode("AcquisitionMode_Shuffling")
        self.vlShuffleLines_Full_Range = PORISValueFloat("ShuffleLines_Full_Range")
        self.mdShuffleLinesMode_Normal = PORISMode("ShuffleLinesMode_Normal")
        self.vlShiftNumber_Full_Range = PORISValueFloat("ShiftNumber_Full_Range")
        self.mdShiftNumberMode_Normal = PORISMode("ShiftNumberMode_Normal")
        self.mdSubarrayFeatureMode_Off = PORISMode("SubarrayFeatureMode_Off")
        self.mdSubarrayFeatureMode_On = PORISMode("SubarrayFeatureMode_On")
        self.mdColsMode_Normal = PORISMode("ColsMode_Normal")
        self.vlCols_Full_Range = PORISValueFloat("Cols_Full_Range")
        self.mdoffsetRowMode_Normal = PORISMode("offsetRowMode_Normal")
        self.vloffsetRow_Full_Range = PORISValueFloat("offsetRow_Full_Range")
        self.mdRowsMode_Normal = PORISMode("RowsMode_Normal")
        self.vlRows_Full_Range = PORISValueFloat("Rows_Full_Range")
        self.mdoffsetColMode_Normal = PORISMode("offsetColMode_Normal")
        self.vloffsetCol_Full_Range = PORISValueFloat("offsetCol_Full_Range")
        self.mdOpenShutterMode_On = PORISMode("OpenShutterMode_On")
        self.mdOpenShutterMode_Off = PORISMode("OpenShutterMode_Off")
        self.vlExpTime_Full_Range = PORISValueFloat("ExpTime_Full_Range")
        self.mdExpTimeMode_Normal = PORISMode("ExpTimeMode_Normal")
        self.mdExpTimeMode_FT = PORISMode("ExpTimeMode_FT")
        self.vlExpTime_FT_Range = PORISValueFloat("ExpTime_FT_Range")
        self.mdPixelSpeedMode_SLW = PORISMode("PixelSpeedMode_SLW")
        self.mdPixelSpeedMode_MED = PORISMode("PixelSpeedMode_MED")
        self.mdPixelSpeedMode_FST = PORISMode("PixelSpeedMode_FST")
        self.mdExposureCtrlMode_Normal = PORISMode("ExposureCtrlMode_Normal")
        self.mdExposureCtrlMode_FT = PORISMode("ExposureCtrlMode_FT")
        self.mdnumOfFramesMode_Multiple = PORISMode("numOfFramesMode_Multiple")
        self.vlnumOfFrames_Multiple_Range = PORISValueFloat("numOfFrames_Multiple_Range")
        self.mdnumOfFramesMode_Single = PORISMode("numOfFramesMode_Single")
        self.vlnumOfFrames_1 = PORISValue("numOfFrames_1")
        self.vlCalibGain_Normal_Range = PORISValueFloat("CalibGain_Normal_Range")
        self.mdCalibGainMode_Normal = PORISMode("CalibGainMode_Normal")
        self.mdExposureCtrlMode_NoShutter = PORISMode("ExposureCtrlMode_NoShutter")
        self.mdExposureCtrlMode_Calibration = PORISMode("ExposureCtrlMode_Calibration")
        self.mdOutputSourceMode_0x0 = PORISMode("OutputSourceMode_0x0")
        self.mdOutputSourceMode_0x1 = PORISMode("OutputSourceMode_0x1")
        self.mdOutputSourceMode_0x2 = PORISMode("OutputSourceMode_0x2")
        self.mdOutputSourceMode_0x3 = PORISMode("OutputSourceMode_0x3")
        self.mdOutputSourceMode_ALL = PORISMode("OutputSourceMode_ALL")
        self.mdOutputSourceMode_TWO = PORISMode("OutputSourceMode_TWO")
        self.mdRecompositionMode_None = PORISMode("RecompositionMode_None")
        self.mdRecompositionMode_Parallel = PORISMode("RecompositionMode_Parallel")
        self.mdRecompositionMode_Serial = PORISMode("RecompositionMode_Serial")
        self.mdRecompositionMode_QuadCCD = PORISMode("RecompositionMode_QuadCCD")
        self.mdRecompositionMode_QuadIR = PORISMode("RecompositionMode_QuadIR")
        self.mdRecompositionMode_CDSQuad = PORISMode("RecompositionMode_CDSQuad")
        self.mdRecompositionMode_HawaiiRG = PORISMode("RecompositionMode_HawaiiRG")
        self.mdAcquisitionMode_NormalWindow = PORISMode("AcquisitionMode_NormalWindow")
        self.vluiRows_Full_Range = PORISValueFloat("uiRows_Full_Range")
        self.mduiRowsMode_Normal = PORISMode("uiRowsMode_Normal")
        self.vluiRows_FTRange = PORISValueFloat("uiRows_FTRange")
        self.mduiRowsMode_Half = PORISMode("uiRowsMode_Half")
        self.vluiCols_Full_Range = PORISValueFloat("uiCols_Full_Range")
        self.mduiColsMode_Normal = PORISMode("uiColsMode_Normal")
        self.mdDimensionsMode_Normal = PORISMode("DimensionsMode_Normal")
        self.mdDimensionsMode_FT = PORISMode("DimensionsMode_FT")
        self.vlBinning_1x1 = PORISValue("Binning_1x1")
        self.vlBinning_1x2 = PORISValue("Binning_1x2")
        self.vlBinning_2x1 = PORISValue("Binning_2x1")
        self.vlBinning_2x2 = PORISValue("Binning_2x2")
        self.mdBinningMode_All = PORISMode("BinningMode_All")
        self.mdAcquisitionMode_Calibration = PORISMode("AcquisitionMode_Calibration")
        self.mdVariantsMode_Normal = PORISMode("VariantsMode_Normal")
        self.mdVariantsMode_Extended = PORISMode("VariantsMode_Extended")
        self.mdVariantsMode_Extended_2 = PORISMode("VariantsMode_Extended_2")
        self.mdARCGenIIIMode_Engineering = PORISMode("ARCGenIIIMode_Engineering")
        self.mdFirmwareMode_Engineering = PORISMode("FirmwareMode_Engineering")
        self.mdVariantsMode_Engineering = PORISMode("VariantsMode_Engineering")
        self.mdAcquisitionMode_Engineering = PORISMode("AcquisitionMode_Engineering")
        self.mdSubarrayFeatureMode_Engineering = PORISMode("SubarrayFeatureMode_Engineering")
        self.mdExposureCtrlMode_Engineering = PORISMode("ExposureCtrlMode_Engineering")
        self.mdOutputSourceMode_Engineering = PORISMode("OutputSourceMode_Engineering")
        self.mdDimensionsMode_Engineering = PORISMode("DimensionsMode_Engineering")

        self.sysARCGenIII.id = idcounter
        idcounter += 1
        self.sysARCGenIII.ident = "ARCGenIII"
        self.sysARCGenIII.description = ""

        self.mdARCGenIIIMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdARCGenIIIMode_UNKNOWN.ident = "ARCGenIIIMode_UNKNOWN"
        self.mdARCGenIIIMode_UNKNOWN.description = ""
        self.sysARCGenIII.addMode(self.mdARCGenIIIMode_UNKNOWN)

        self.sysFirmware.id = idcounter
        idcounter += 1
        self.sysFirmware.ident = "Firmware"
        self.sysFirmware.description = ""
        self.sysARCGenIII.addSubsystem(self.sysFirmware)

        self.mdFirmwareMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdFirmwareMode_UNKNOWN.ident = "FirmwareMode_UNKNOWN"
        self.mdFirmwareMode_UNKNOWN.description = ""
        self.sysFirmware.addMode(self.mdFirmwareMode_UNKNOWN)

        self.sysVariants.id = idcounter
        idcounter += 1
        self.sysVariants.ident = "Variants"
        self.sysVariants.description = ""
        self.sysFirmware.addSubsystem(self.sysVariants)

        self.mdVariantsMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdVariantsMode_UNKNOWN.ident = "VariantsMode_UNKNOWN"
        self.mdVariantsMode_UNKNOWN.description = ""
        self.sysVariants.addMode(self.mdVariantsMode_UNKNOWN)

        self.sysAcquisition.id = idcounter
        idcounter += 1
        self.sysAcquisition.ident = "Acquisition"
        self.sysAcquisition.description = ""
        self.sysVariants.addSubsystem(self.sysAcquisition)

        self.mdAcquisitionMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdAcquisitionMode_UNKNOWN.ident = "AcquisitionMode_UNKNOWN"
        self.mdAcquisitionMode_UNKNOWN.description = ""
        self.sysAcquisition.addMode(self.mdAcquisitionMode_UNKNOWN)

        self.prShuffleLines.id = idcounter
        idcounter += 1
        self.prShuffleLines.ident = "ShuffleLines"
        self.prShuffleLines.description = ""
        self.sysAcquisition.addParam(self.prShuffleLines)

        self.vlShuffleLines_UNKNOWN.id = idcounter
        idcounter += 1
        self.vlShuffleLines_UNKNOWN.ident = "ShuffleLines_UNKNOWN"
        self.vlShuffleLines_UNKNOWN.description = "Unknown value for ShuffleLines"
        self.prShuffleLines.addValue(self.vlShuffleLines_UNKNOWN)

        self.mdShuffleLinesMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdShuffleLinesMode_UNKNOWN.ident = "ShuffleLinesMode_UNKNOWN"
        self.mdShuffleLinesMode_UNKNOWN.description = "Unknown mode for ShuffleLines"
        self.prShuffleLines.addMode(self.mdShuffleLinesMode_UNKNOWN)
        self.mdShuffleLinesMode_UNKNOWN.addValue(self.vlShuffleLines_UNKNOWN)
        self.mdAcquisitionMode_UNKNOWN.addSubMode(self.mdShuffleLinesMode_UNKNOWN)

        self.prShiftNumber.id = idcounter
        idcounter += 1
        self.prShiftNumber.ident = "ShiftNumber"
        self.prShiftNumber.description = ""
        self.sysAcquisition.addParam(self.prShiftNumber)

        self.vlShiftNumber_UNKNOWN.id = idcounter
        idcounter += 1
        self.vlShiftNumber_UNKNOWN.ident = "ShiftNumber_UNKNOWN"
        self.vlShiftNumber_UNKNOWN.description = "Unknown value for ShiftNumber"
        self.prShiftNumber.addValue(self.vlShiftNumber_UNKNOWN)

        self.mdShiftNumberMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdShiftNumberMode_UNKNOWN.ident = "ShiftNumberMode_UNKNOWN"
        self.mdShiftNumberMode_UNKNOWN.description = "Unknown mode for ShiftNumber"
        self.prShiftNumber.addMode(self.mdShiftNumberMode_UNKNOWN)
        self.mdShiftNumberMode_UNKNOWN.addValue(self.vlShiftNumber_UNKNOWN)
        self.mdAcquisitionMode_UNKNOWN.addSubMode(self.mdShiftNumberMode_UNKNOWN)

        self.sysSubarrayFeature.id = idcounter
        idcounter += 1
        self.sysSubarrayFeature.ident = "SubarrayFeature"
        self.sysSubarrayFeature.description = ""
        self.sysAcquisition.addSubsystem(self.sysSubarrayFeature)

        self.mdSubarrayFeatureMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdSubarrayFeatureMode_UNKNOWN.ident = "SubarrayFeatureMode_UNKNOWN"
        self.mdSubarrayFeatureMode_UNKNOWN.description = ""
        self.sysSubarrayFeature.addMode(self.mdSubarrayFeatureMode_UNKNOWN)

        self.prCols.id = idcounter
        idcounter += 1
        self.prCols.ident = "Cols"
        self.prCols.description = ""
        self.sysSubarrayFeature.addParam(self.prCols)

        self.vlCols_UNKNOWN.id = idcounter
        idcounter += 1
        self.vlCols_UNKNOWN.ident = "Cols_UNKNOWN"
        self.vlCols_UNKNOWN.description = "Unknown value for Cols"
        self.prCols.addValue(self.vlCols_UNKNOWN)

        self.mdColsMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdColsMode_UNKNOWN.ident = "ColsMode_UNKNOWN"
        self.mdColsMode_UNKNOWN.description = "Unknown mode for Cols"
        self.prCols.addMode(self.mdColsMode_UNKNOWN)
        self.mdColsMode_UNKNOWN.addValue(self.vlCols_UNKNOWN)
        self.mdSubarrayFeatureMode_UNKNOWN.addSubMode(self.mdColsMode_UNKNOWN)

        self.proffsetRow.id = idcounter
        idcounter += 1
        self.proffsetRow.ident = "offsetRow"
        self.proffsetRow.description = ""
        self.sysSubarrayFeature.addParam(self.proffsetRow)

        self.vloffsetRow_UNKNOWN.id = idcounter
        idcounter += 1
        self.vloffsetRow_UNKNOWN.ident = "offsetRow_UNKNOWN"
        self.vloffsetRow_UNKNOWN.description = "Unknown value for offsetRow"
        self.proffsetRow.addValue(self.vloffsetRow_UNKNOWN)

        self.mdoffsetRowMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdoffsetRowMode_UNKNOWN.ident = "offsetRowMode_UNKNOWN"
        self.mdoffsetRowMode_UNKNOWN.description = "Unknown mode for offsetRow"
        self.proffsetRow.addMode(self.mdoffsetRowMode_UNKNOWN)
        self.mdoffsetRowMode_UNKNOWN.addValue(self.vloffsetRow_UNKNOWN)
        self.mdSubarrayFeatureMode_UNKNOWN.addSubMode(self.mdoffsetRowMode_UNKNOWN)

        self.prRows.id = idcounter
        idcounter += 1
        self.prRows.ident = "Rows"
        self.prRows.description = ""
        self.sysSubarrayFeature.addParam(self.prRows)

        self.vlRows_UNKNOWN.id = idcounter
        idcounter += 1
        self.vlRows_UNKNOWN.ident = "Rows_UNKNOWN"
        self.vlRows_UNKNOWN.description = "Unknown value for Rows"
        self.prRows.addValue(self.vlRows_UNKNOWN)

        self.mdRowsMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdRowsMode_UNKNOWN.ident = "RowsMode_UNKNOWN"
        self.mdRowsMode_UNKNOWN.description = "Unknown mode for Rows"
        self.prRows.addMode(self.mdRowsMode_UNKNOWN)
        self.mdRowsMode_UNKNOWN.addValue(self.vlRows_UNKNOWN)
        self.mdSubarrayFeatureMode_UNKNOWN.addSubMode(self.mdRowsMode_UNKNOWN)

        self.proffsetCol.id = idcounter
        idcounter += 1
        self.proffsetCol.ident = "offsetCol"
        self.proffsetCol.description = ""
        self.sysSubarrayFeature.addParam(self.proffsetCol)

        self.vloffsetCol_UNKNOWN.id = idcounter
        idcounter += 1
        self.vloffsetCol_UNKNOWN.ident = "offsetCol_UNKNOWN"
        self.vloffsetCol_UNKNOWN.description = "Unknown value for offsetCol"
        self.proffsetCol.addValue(self.vloffsetCol_UNKNOWN)

        self.mdoffsetColMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdoffsetColMode_UNKNOWN.ident = "offsetColMode_UNKNOWN"
        self.mdoffsetColMode_UNKNOWN.description = "Unknown mode for offsetCol"
        self.proffsetCol.addMode(self.mdoffsetColMode_UNKNOWN)
        self.mdoffsetColMode_UNKNOWN.addValue(self.vloffsetCol_UNKNOWN)
        self.mdSubarrayFeatureMode_UNKNOWN.addSubMode(self.mdoffsetColMode_UNKNOWN)

        self.sysExposureCtrl.id = idcounter
        idcounter += 1
        self.sysExposureCtrl.ident = "ExposureCtrl"
        self.sysExposureCtrl.description = ""
        self.sysAcquisition.addSubsystem(self.sysExposureCtrl)

        self.mdExposureCtrlMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdExposureCtrlMode_UNKNOWN.ident = "ExposureCtrlMode_UNKNOWN"
        self.mdExposureCtrlMode_UNKNOWN.description = ""
        self.sysExposureCtrl.addMode(self.mdExposureCtrlMode_UNKNOWN)

        self.sysOpenShutter.id = idcounter
        idcounter += 1
        self.sysOpenShutter.ident = "OpenShutter"
        self.sysOpenShutter.description = ""
        self.sysExposureCtrl.addSubsystem(self.sysOpenShutter)

        self.mdOpenShutterMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdOpenShutterMode_UNKNOWN.ident = "OpenShutterMode_UNKNOWN"
        self.mdOpenShutterMode_UNKNOWN.description = ""
        self.sysOpenShutter.addMode(self.mdOpenShutterMode_UNKNOWN)

        self.prExpTime.id = idcounter
        idcounter += 1
        self.prExpTime.ident = "ExpTime"
        self.prExpTime.description = ""
        self.sysExposureCtrl.addParam(self.prExpTime)

        self.vlExpTime_UNKNOWN.id = idcounter
        idcounter += 1
        self.vlExpTime_UNKNOWN.ident = "ExpTime_UNKNOWN"
        self.vlExpTime_UNKNOWN.description = "Unknown value for ExpTime"
        self.prExpTime.addValue(self.vlExpTime_UNKNOWN)

        self.mdExpTimeMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdExpTimeMode_UNKNOWN.ident = "ExpTimeMode_UNKNOWN"
        self.mdExpTimeMode_UNKNOWN.description = "Unknown mode for ExpTime"
        self.prExpTime.addMode(self.mdExpTimeMode_UNKNOWN)
        self.mdExpTimeMode_UNKNOWN.addValue(self.vlExpTime_UNKNOWN)
        self.mdExposureCtrlMode_UNKNOWN.addSubMode(self.mdExpTimeMode_UNKNOWN)

        self.sysPixelSpeed.id = idcounter
        idcounter += 1
        self.sysPixelSpeed.ident = "PixelSpeed"
        self.sysPixelSpeed.description = ""
        self.sysExposureCtrl.addSubsystem(self.sysPixelSpeed)

        self.mdPixelSpeedMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdPixelSpeedMode_UNKNOWN.ident = "PixelSpeedMode_UNKNOWN"
        self.mdPixelSpeedMode_UNKNOWN.description = ""
        self.sysPixelSpeed.addMode(self.mdPixelSpeedMode_UNKNOWN)

        self.prnumOfFrames.id = idcounter
        idcounter += 1
        self.prnumOfFrames.ident = "numOfFrames"
        self.prnumOfFrames.description = ""
        self.sysExposureCtrl.addParam(self.prnumOfFrames)

        self.vlnumOfFrames_UNKNOWN.id = idcounter
        idcounter += 1
        self.vlnumOfFrames_UNKNOWN.ident = "numOfFrames_UNKNOWN"
        self.vlnumOfFrames_UNKNOWN.description = "Unknown value for numOfFrames"
        self.prnumOfFrames.addValue(self.vlnumOfFrames_UNKNOWN)

        self.mdnumOfFramesMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdnumOfFramesMode_UNKNOWN.ident = "numOfFramesMode_UNKNOWN"
        self.mdnumOfFramesMode_UNKNOWN.description = "Unknown mode for numOfFrames"
        self.prnumOfFrames.addMode(self.mdnumOfFramesMode_UNKNOWN)
        self.mdnumOfFramesMode_UNKNOWN.addValue(self.vlnumOfFrames_UNKNOWN)
        self.mdExposureCtrlMode_UNKNOWN.addSubMode(self.mdnumOfFramesMode_UNKNOWN)

        self.prCalibGain.id = idcounter
        idcounter += 1
        self.prCalibGain.ident = "CalibGain"
        self.prCalibGain.description = ""
        self.sysExposureCtrl.addParam(self.prCalibGain)

        self.vlCalibGain_UNKNOWN.id = idcounter
        idcounter += 1
        self.vlCalibGain_UNKNOWN.ident = "CalibGain_UNKNOWN"
        self.vlCalibGain_UNKNOWN.description = "Unknown value for CalibGain"
        self.prCalibGain.addValue(self.vlCalibGain_UNKNOWN)

        self.mdCalibGainMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdCalibGainMode_UNKNOWN.ident = "CalibGainMode_UNKNOWN"
        self.mdCalibGainMode_UNKNOWN.description = "Unknown mode for CalibGain"
        self.prCalibGain.addMode(self.mdCalibGainMode_UNKNOWN)
        self.mdCalibGainMode_UNKNOWN.addValue(self.vlCalibGain_UNKNOWN)
        self.mdExposureCtrlMode_UNKNOWN.addSubMode(self.mdCalibGainMode_UNKNOWN)

        self.sysOutputSource.id = idcounter
        idcounter += 1
        self.sysOutputSource.ident = "OutputSource"
        self.sysOutputSource.description = ""
        self.sysAcquisition.addSubsystem(self.sysOutputSource)

        self.mdOutputSourceMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdOutputSourceMode_UNKNOWN.ident = "OutputSourceMode_UNKNOWN"
        self.mdOutputSourceMode_UNKNOWN.description = ""
        self.sysOutputSource.addMode(self.mdOutputSourceMode_UNKNOWN)

        self.sysRecomposition.id = idcounter
        idcounter += 1
        self.sysRecomposition.ident = "Recomposition"
        self.sysRecomposition.description = ""
        self.sysOutputSource.addSubsystem(self.sysRecomposition)

        self.mdRecompositionMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdRecompositionMode_UNKNOWN.ident = "RecompositionMode_UNKNOWN"
        self.mdRecompositionMode_UNKNOWN.description = ""
        self.sysRecomposition.addMode(self.mdRecompositionMode_UNKNOWN)

        self.sysDimensions.id = idcounter
        idcounter += 1
        self.sysDimensions.ident = "Dimensions"
        self.sysDimensions.description = ""
        self.sysAcquisition.addSubsystem(self.sysDimensions)

        self.mdDimensionsMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdDimensionsMode_UNKNOWN.ident = "DimensionsMode_UNKNOWN"
        self.mdDimensionsMode_UNKNOWN.description = ""
        self.sysDimensions.addMode(self.mdDimensionsMode_UNKNOWN)

        self.pruiRows.id = idcounter
        idcounter += 1
        self.pruiRows.ident = "uiRows"
        self.pruiRows.description = ""
        self.sysDimensions.addParam(self.pruiRows)

        self.vluiRows_UNKNOWN.id = idcounter
        idcounter += 1
        self.vluiRows_UNKNOWN.ident = "uiRows_UNKNOWN"
        self.vluiRows_UNKNOWN.description = "Unknown value for uiRows"
        self.pruiRows.addValue(self.vluiRows_UNKNOWN)

        self.mduiRowsMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mduiRowsMode_UNKNOWN.ident = "uiRowsMode_UNKNOWN"
        self.mduiRowsMode_UNKNOWN.description = "Unknown mode for uiRows"
        self.pruiRows.addMode(self.mduiRowsMode_UNKNOWN)
        self.mduiRowsMode_UNKNOWN.addValue(self.vluiRows_UNKNOWN)
        self.mdDimensionsMode_UNKNOWN.addSubMode(self.mduiRowsMode_UNKNOWN)

        self.pruiCols.id = idcounter
        idcounter += 1
        self.pruiCols.ident = "uiCols"
        self.pruiCols.description = ""
        self.sysDimensions.addParam(self.pruiCols)

        self.vluiCols_UNKNOWN.id = idcounter
        idcounter += 1
        self.vluiCols_UNKNOWN.ident = "uiCols_UNKNOWN"
        self.vluiCols_UNKNOWN.description = "Unknown value for uiCols"
        self.pruiCols.addValue(self.vluiCols_UNKNOWN)

        self.mduiColsMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mduiColsMode_UNKNOWN.ident = "uiColsMode_UNKNOWN"
        self.mduiColsMode_UNKNOWN.description = "Unknown mode for uiCols"
        self.pruiCols.addMode(self.mduiColsMode_UNKNOWN)
        self.mduiColsMode_UNKNOWN.addValue(self.vluiCols_UNKNOWN)
        self.mdDimensionsMode_UNKNOWN.addSubMode(self.mduiColsMode_UNKNOWN)

        self.prBinning.id = idcounter
        idcounter += 1
        self.prBinning.ident = "Binning"
        self.prBinning.description = ""
        self.sysAcquisition.addParam(self.prBinning)

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
        self.mdAcquisitionMode_UNKNOWN.addSubMode(self.mdBinningMode_UNKNOWN)

        self.mdARCGenIIIMode_Real.id = idcounter
        idcounter += 1
        self.mdARCGenIIIMode_Real.ident = "ARCGenIIIMode_Real"
        self.mdARCGenIIIMode_Real.description = ""
        self.sysARCGenIII.addMode(self.mdARCGenIIIMode_Real)

        self.mdARCGenIIIMode_Emulated.id = idcounter
        idcounter += 1
        self.mdARCGenIIIMode_Emulated.ident = "ARCGenIIIMode_Emulated"
        self.mdARCGenIIIMode_Emulated.description = ""
        self.sysARCGenIII.addMode(self.mdARCGenIIIMode_Emulated)

        self.mdFirmwareMode_tim.id = idcounter
        idcounter += 1
        self.mdFirmwareMode_tim.ident = "FirmwareMode_tim"
        self.mdFirmwareMode_tim.description = ""
        self.sysFirmware.addMode(self.mdFirmwareMode_tim)

        self.mdFirmwareMode_osiris2.id = idcounter
        idcounter += 1
        self.mdFirmwareMode_osiris2.ident = "FirmwareMode_osiris2"
        self.mdFirmwareMode_osiris2.description = ""
        self.sysFirmware.addMode(self.mdFirmwareMode_osiris2)

        self.mdFirmwareMode_osiris3.id = idcounter
        idcounter += 1
        self.mdFirmwareMode_osiris3.ident = "FirmwareMode_osiris3"
        self.mdFirmwareMode_osiris3.description = ""
        self.sysFirmware.addMode(self.mdFirmwareMode_osiris3)

        self.mdFirmwareMode_osiris4.id = idcounter
        idcounter += 1
        self.mdFirmwareMode_osiris4.ident = "FirmwareMode_osiris4"
        self.mdFirmwareMode_osiris4.description = ""
        self.sysFirmware.addMode(self.mdFirmwareMode_osiris4)

        self.mdFirmwareMode_osiris5.id = idcounter
        idcounter += 1
        self.mdFirmwareMode_osiris5.ident = "FirmwareMode_osiris5"
        self.mdFirmwareMode_osiris5.description = ""
        self.sysFirmware.addMode(self.mdFirmwareMode_osiris5)

        self.mdAcquisitionMode_Normal.id = idcounter
        idcounter += 1
        self.mdAcquisitionMode_Normal.ident = "AcquisitionMode_Normal"
        self.mdAcquisitionMode_Normal.description = ""
        self.sysAcquisition.addMode(self.mdAcquisitionMode_Normal)

        self.mdAcquisitionMode_FrameTransfer.id = idcounter
        idcounter += 1
        self.mdAcquisitionMode_FrameTransfer.ident = "AcquisitionMode_FrameTransfer"
        self.mdAcquisitionMode_FrameTransfer.description = ""
        self.sysAcquisition.addMode(self.mdAcquisitionMode_FrameTransfer)

        self.mdAcquisitionMode_Shuffling.id = idcounter
        idcounter += 1
        self.mdAcquisitionMode_Shuffling.ident = "AcquisitionMode_Shuffling"
        self.mdAcquisitionMode_Shuffling.description = ""
        self.sysAcquisition.addMode(self.mdAcquisitionMode_Shuffling)

        self.vlShuffleLines_Full_Range.id = idcounter
        idcounter += 1
        self.vlShuffleLines_Full_Range.ident = "ShuffleLines_Full_Range"
        self.vlShuffleLines_Full_Range.description = ""
        self.vlShuffleLines_Full_Range.min = 0
        self.vlShuffleLines_Full_Range.default_data = 200
        self.vlShuffleLines_Full_Range.max = 1000
        self.prShuffleLines.addValue(self.vlShuffleLines_Full_Range)

        self.mdShuffleLinesMode_Normal.id = idcounter
        idcounter += 1
        self.mdShuffleLinesMode_Normal.ident = "ShuffleLinesMode_Normal"
        self.mdShuffleLinesMode_Normal.description = ""
        self.prShuffleLines.addMode(self.mdShuffleLinesMode_Normal)

        self.vlShiftNumber_Full_Range.id = idcounter
        idcounter += 1
        self.vlShiftNumber_Full_Range.ident = "ShiftNumber_Full_Range"
        self.vlShiftNumber_Full_Range.description = ""
        self.vlShiftNumber_Full_Range.min = 0
        self.vlShiftNumber_Full_Range.default_data = 5
        self.vlShiftNumber_Full_Range.max = 1000
        self.prShiftNumber.addValue(self.vlShiftNumber_Full_Range)

        self.mdShiftNumberMode_Normal.id = idcounter
        idcounter += 1
        self.mdShiftNumberMode_Normal.ident = "ShiftNumberMode_Normal"
        self.mdShiftNumberMode_Normal.description = ""
        self.prShiftNumber.addMode(self.mdShiftNumberMode_Normal)

        self.mdSubarrayFeatureMode_Off.id = idcounter
        idcounter += 1
        self.mdSubarrayFeatureMode_Off.ident = "SubarrayFeatureMode_Off"
        self.mdSubarrayFeatureMode_Off.description = ""
        self.sysSubarrayFeature.addMode(self.mdSubarrayFeatureMode_Off)

        self.mdSubarrayFeatureMode_On.id = idcounter
        idcounter += 1
        self.mdSubarrayFeatureMode_On.ident = "SubarrayFeatureMode_On"
        self.mdSubarrayFeatureMode_On.description = ""
        self.sysSubarrayFeature.addMode(self.mdSubarrayFeatureMode_On)

        self.mdColsMode_Normal.id = idcounter
        idcounter += 1
        self.mdColsMode_Normal.ident = "ColsMode_Normal"
        self.mdColsMode_Normal.description = ""
        self.prCols.addMode(self.mdColsMode_Normal)

        self.vlCols_Full_Range.id = idcounter
        idcounter += 1
        self.vlCols_Full_Range.ident = "Cols_Full_Range"
        self.vlCols_Full_Range.description = ""
        self.vlCols_Full_Range.min = 0
        self.vlCols_Full_Range.default_data = 2048
        self.vlCols_Full_Range.max = 4098
        self.prCols.addValue(self.vlCols_Full_Range)

        self.mdoffsetRowMode_Normal.id = idcounter
        idcounter += 1
        self.mdoffsetRowMode_Normal.ident = "offsetRowMode_Normal"
        self.mdoffsetRowMode_Normal.description = ""
        self.proffsetRow.addMode(self.mdoffsetRowMode_Normal)

        self.vloffsetRow_Full_Range.id = idcounter
        idcounter += 1
        self.vloffsetRow_Full_Range.ident = "offsetRow_Full_Range"
        self.vloffsetRow_Full_Range.description = ""
        self.vloffsetRow_Full_Range.min = 0
        self.vloffsetRow_Full_Range.default_data = 2048
        self.vloffsetRow_Full_Range.max = 4098
        self.proffsetRow.addValue(self.vloffsetRow_Full_Range)

        self.mdRowsMode_Normal.id = idcounter
        idcounter += 1
        self.mdRowsMode_Normal.ident = "RowsMode_Normal"
        self.mdRowsMode_Normal.description = ""
        self.prRows.addMode(self.mdRowsMode_Normal)

        self.vlRows_Full_Range.id = idcounter
        idcounter += 1
        self.vlRows_Full_Range.ident = "Rows_Full_Range"
        self.vlRows_Full_Range.description = ""
        self.vlRows_Full_Range.min = 0
        self.vlRows_Full_Range.default_data = 2048
        self.vlRows_Full_Range.max = 4098
        self.prRows.addValue(self.vlRows_Full_Range)

        self.mdoffsetColMode_Normal.id = idcounter
        idcounter += 1
        self.mdoffsetColMode_Normal.ident = "offsetColMode_Normal"
        self.mdoffsetColMode_Normal.description = ""
        self.proffsetCol.addMode(self.mdoffsetColMode_Normal)

        self.vloffsetCol_Full_Range.id = idcounter
        idcounter += 1
        self.vloffsetCol_Full_Range.ident = "offsetCol_Full_Range"
        self.vloffsetCol_Full_Range.description = ""
        self.vloffsetCol_Full_Range.min = 0
        self.vloffsetCol_Full_Range.default_data = 2048
        self.vloffsetCol_Full_Range.max = 4098
        self.proffsetCol.addValue(self.vloffsetCol_Full_Range)

        self.mdOpenShutterMode_On.id = idcounter
        idcounter += 1
        self.mdOpenShutterMode_On.ident = "OpenShutterMode_On"
        self.mdOpenShutterMode_On.description = ""
        self.sysOpenShutter.addMode(self.mdOpenShutterMode_On)

        self.mdOpenShutterMode_Off.id = idcounter
        idcounter += 1
        self.mdOpenShutterMode_Off.ident = "OpenShutterMode_Off"
        self.mdOpenShutterMode_Off.description = ""
        self.sysOpenShutter.addMode(self.mdOpenShutterMode_Off)

        self.vlExpTime_Full_Range.id = idcounter
        idcounter += 1
        self.vlExpTime_Full_Range.ident = "ExpTime_Full_Range"
        self.vlExpTime_Full_Range.description = ""
        self.vlExpTime_Full_Range.min = 0
        self.vlExpTime_Full_Range.default_data = 1
        self.vlExpTime_Full_Range.max = 4294967.295
        self.prExpTime.addValue(self.vlExpTime_Full_Range)

        self.mdExpTimeMode_Normal.id = idcounter
        idcounter += 1
        self.mdExpTimeMode_Normal.ident = "ExpTimeMode_Normal"
        self.mdExpTimeMode_Normal.description = ""
        self.prExpTime.addMode(self.mdExpTimeMode_Normal)

        self.mdExpTimeMode_FT.id = idcounter
        idcounter += 1
        self.mdExpTimeMode_FT.ident = "ExpTimeMode_FT"
        self.mdExpTimeMode_FT.description = ""
        self.prExpTime.addMode(self.mdExpTimeMode_FT)

        self.vlExpTime_FT_Range.id = idcounter
        idcounter += 1
        self.vlExpTime_FT_Range.ident = "ExpTime_FT_Range"
        self.vlExpTime_FT_Range.description = ""
        self.vlExpTime_FT_Range.min = 0
        self.vlExpTime_FT_Range.default_data = 0
        self.vlExpTime_FT_Range.max = 360
        self.prExpTime.addValue(self.vlExpTime_FT_Range)

        self.mdPixelSpeedMode_SLW.id = idcounter
        idcounter += 1
        self.mdPixelSpeedMode_SLW.ident = "PixelSpeedMode_SLW"
        self.mdPixelSpeedMode_SLW.description = ""
        self.sysPixelSpeed.addMode(self.mdPixelSpeedMode_SLW)

        self.mdPixelSpeedMode_MED.id = idcounter
        idcounter += 1
        self.mdPixelSpeedMode_MED.ident = "PixelSpeedMode_MED"
        self.mdPixelSpeedMode_MED.description = ""
        self.sysPixelSpeed.addMode(self.mdPixelSpeedMode_MED)

        self.mdPixelSpeedMode_FST.id = idcounter
        idcounter += 1
        self.mdPixelSpeedMode_FST.ident = "PixelSpeedMode_FST"
        self.mdPixelSpeedMode_FST.description = ""
        self.sysPixelSpeed.addMode(self.mdPixelSpeedMode_FST)

        self.mdExposureCtrlMode_Normal.id = idcounter
        idcounter += 1
        self.mdExposureCtrlMode_Normal.ident = "ExposureCtrlMode_Normal"
        self.mdExposureCtrlMode_Normal.description = ""
        self.sysExposureCtrl.addMode(self.mdExposureCtrlMode_Normal)

        self.mdExposureCtrlMode_FT.id = idcounter
        idcounter += 1
        self.mdExposureCtrlMode_FT.ident = "ExposureCtrlMode_FT"
        self.mdExposureCtrlMode_FT.description = ""
        self.sysExposureCtrl.addMode(self.mdExposureCtrlMode_FT)

        self.mdnumOfFramesMode_Multiple.id = idcounter
        idcounter += 1
        self.mdnumOfFramesMode_Multiple.ident = "numOfFramesMode_Multiple"
        self.mdnumOfFramesMode_Multiple.description = ""
        self.prnumOfFrames.addMode(self.mdnumOfFramesMode_Multiple)

        self.vlnumOfFrames_Multiple_Range.id = idcounter
        idcounter += 1
        self.vlnumOfFrames_Multiple_Range.ident = "numOfFrames_Multiple_Range"
        self.vlnumOfFrames_Multiple_Range.description = ""
        self.vlnumOfFrames_Multiple_Range.min = 2
        self.vlnumOfFrames_Multiple_Range.default_data = 10
        self.vlnumOfFrames_Multiple_Range.max = 4294967295
        self.prnumOfFrames.addValue(self.vlnumOfFrames_Multiple_Range)

        self.mdnumOfFramesMode_Single.id = idcounter
        idcounter += 1
        self.mdnumOfFramesMode_Single.ident = "numOfFramesMode_Single"
        self.mdnumOfFramesMode_Single.description = ""
        self.prnumOfFrames.addMode(self.mdnumOfFramesMode_Single)

        self.vlnumOfFrames_1.id = idcounter
        idcounter += 1
        self.vlnumOfFrames_1.ident = "numOfFrames_1"
        self.vlnumOfFrames_1.description = ""
        self.prnumOfFrames.addValue(self.vlnumOfFrames_1)

        self.vlCalibGain_Normal_Range.id = idcounter
        idcounter += 1
        self.vlCalibGain_Normal_Range.ident = "CalibGain_Normal_Range"
        self.vlCalibGain_Normal_Range.description = ""
        self.vlCalibGain_Normal_Range.min = 0
        self.vlCalibGain_Normal_Range.default_data = 2
        self.vlCalibGain_Normal_Range.max = 15
        self.prCalibGain.addValue(self.vlCalibGain_Normal_Range)

        self.mdCalibGainMode_Normal.id = idcounter
        idcounter += 1
        self.mdCalibGainMode_Normal.ident = "CalibGainMode_Normal"
        self.mdCalibGainMode_Normal.description = ""
        self.prCalibGain.addMode(self.mdCalibGainMode_Normal)

        self.mdExposureCtrlMode_NoShutter.id = idcounter
        idcounter += 1
        self.mdExposureCtrlMode_NoShutter.ident = "ExposureCtrlMode_NoShutter"
        self.mdExposureCtrlMode_NoShutter.description = ""
        self.sysExposureCtrl.addMode(self.mdExposureCtrlMode_NoShutter)

        self.mdExposureCtrlMode_Calibration.id = idcounter
        idcounter += 1
        self.mdExposureCtrlMode_Calibration.ident = "ExposureCtrlMode_Calibration"
        self.mdExposureCtrlMode_Calibration.description = ""
        self.sysExposureCtrl.addMode(self.mdExposureCtrlMode_Calibration)

        self.mdOutputSourceMode_0x0.id = idcounter
        idcounter += 1
        self.mdOutputSourceMode_0x0.ident = "OutputSourceMode_0x0"
        self.mdOutputSourceMode_0x0.description = ""
        self.sysOutputSource.addMode(self.mdOutputSourceMode_0x0)

        self.mdOutputSourceMode_0x1.id = idcounter
        idcounter += 1
        self.mdOutputSourceMode_0x1.ident = "OutputSourceMode_0x1"
        self.mdOutputSourceMode_0x1.description = ""
        self.sysOutputSource.addMode(self.mdOutputSourceMode_0x1)

        self.mdOutputSourceMode_0x2.id = idcounter
        idcounter += 1
        self.mdOutputSourceMode_0x2.ident = "OutputSourceMode_0x2"
        self.mdOutputSourceMode_0x2.description = ""
        self.sysOutputSource.addMode(self.mdOutputSourceMode_0x2)

        self.mdOutputSourceMode_0x3.id = idcounter
        idcounter += 1
        self.mdOutputSourceMode_0x3.ident = "OutputSourceMode_0x3"
        self.mdOutputSourceMode_0x3.description = ""
        self.sysOutputSource.addMode(self.mdOutputSourceMode_0x3)

        self.mdOutputSourceMode_ALL.id = idcounter
        idcounter += 1
        self.mdOutputSourceMode_ALL.ident = "OutputSourceMode_ALL"
        self.mdOutputSourceMode_ALL.description = ""
        self.sysOutputSource.addMode(self.mdOutputSourceMode_ALL)

        self.mdOutputSourceMode_TWO.id = idcounter
        idcounter += 1
        self.mdOutputSourceMode_TWO.ident = "OutputSourceMode_TWO"
        self.mdOutputSourceMode_TWO.description = ""
        self.sysOutputSource.addMode(self.mdOutputSourceMode_TWO)

        self.mdRecompositionMode_None.id = idcounter
        idcounter += 1
        self.mdRecompositionMode_None.ident = "RecompositionMode_None"
        self.mdRecompositionMode_None.description = ""
        self.sysRecomposition.addMode(self.mdRecompositionMode_None)

        self.mdRecompositionMode_Parallel.id = idcounter
        idcounter += 1
        self.mdRecompositionMode_Parallel.ident = "RecompositionMode_Parallel"
        self.mdRecompositionMode_Parallel.description = ""
        self.sysRecomposition.addMode(self.mdRecompositionMode_Parallel)

        self.mdRecompositionMode_Serial.id = idcounter
        idcounter += 1
        self.mdRecompositionMode_Serial.ident = "RecompositionMode_Serial"
        self.mdRecompositionMode_Serial.description = ""
        self.sysRecomposition.addMode(self.mdRecompositionMode_Serial)

        self.mdRecompositionMode_QuadCCD.id = idcounter
        idcounter += 1
        self.mdRecompositionMode_QuadCCD.ident = "RecompositionMode_QuadCCD"
        self.mdRecompositionMode_QuadCCD.description = ""
        self.sysRecomposition.addMode(self.mdRecompositionMode_QuadCCD)

        self.mdRecompositionMode_QuadIR.id = idcounter
        idcounter += 1
        self.mdRecompositionMode_QuadIR.ident = "RecompositionMode_QuadIR"
        self.mdRecompositionMode_QuadIR.description = ""
        self.sysRecomposition.addMode(self.mdRecompositionMode_QuadIR)

        self.mdRecompositionMode_CDSQuad.id = idcounter
        idcounter += 1
        self.mdRecompositionMode_CDSQuad.ident = "RecompositionMode_CDSQuad"
        self.mdRecompositionMode_CDSQuad.description = ""
        self.sysRecomposition.addMode(self.mdRecompositionMode_CDSQuad)

        self.mdRecompositionMode_HawaiiRG.id = idcounter
        idcounter += 1
        self.mdRecompositionMode_HawaiiRG.ident = "RecompositionMode_HawaiiRG"
        self.mdRecompositionMode_HawaiiRG.description = ""
        self.sysRecomposition.addMode(self.mdRecompositionMode_HawaiiRG)

        self.mdAcquisitionMode_NormalWindow.id = idcounter
        idcounter += 1
        self.mdAcquisitionMode_NormalWindow.ident = "AcquisitionMode_NormalWindow"
        self.mdAcquisitionMode_NormalWindow.description = ""
        self.sysAcquisition.addMode(self.mdAcquisitionMode_NormalWindow)

        self.vluiRows_Full_Range.id = idcounter
        idcounter += 1
        self.vluiRows_Full_Range.ident = "uiRows_Full_Range"
        self.vluiRows_Full_Range.description = ""
        self.vluiRows_Full_Range.min = 0
        self.vluiRows_Full_Range.default_data = 4112
        self.vluiRows_Full_Range.max = 4112
        self.pruiRows.addValue(self.vluiRows_Full_Range)

        self.mduiRowsMode_Normal.id = idcounter
        idcounter += 1
        self.mduiRowsMode_Normal.ident = "uiRowsMode_Normal"
        self.mduiRowsMode_Normal.description = ""
        self.pruiRows.addMode(self.mduiRowsMode_Normal)

        self.vluiRows_FTRange.id = idcounter
        idcounter += 1
        self.vluiRows_FTRange.ident = "uiRows_FTRange"
        self.vluiRows_FTRange.description = ""
        self.vluiRows_FTRange.min = 0
        self.vluiRows_FTRange.default_data = 2056
        self.vluiRows_FTRange.max = 2056
        self.pruiRows.addValue(self.vluiRows_FTRange)

        self.mduiRowsMode_Half.id = idcounter
        idcounter += 1
        self.mduiRowsMode_Half.ident = "uiRowsMode_Half"
        self.mduiRowsMode_Half.description = ""
        self.pruiRows.addMode(self.mduiRowsMode_Half)

        self.vluiCols_Full_Range.id = idcounter
        idcounter += 1
        self.vluiCols_Full_Range.ident = "uiCols_Full_Range"
        self.vluiCols_Full_Range.description = ""
        self.vluiCols_Full_Range.min = 0
        self.vluiCols_Full_Range.default_data = 4096
        self.vluiCols_Full_Range.max = 4096
        self.pruiCols.addValue(self.vluiCols_Full_Range)

        self.mduiColsMode_Normal.id = idcounter
        idcounter += 1
        self.mduiColsMode_Normal.ident = "uiColsMode_Normal"
        self.mduiColsMode_Normal.description = ""
        self.pruiCols.addMode(self.mduiColsMode_Normal)

        self.mdDimensionsMode_Normal.id = idcounter
        idcounter += 1
        self.mdDimensionsMode_Normal.ident = "DimensionsMode_Normal"
        self.mdDimensionsMode_Normal.description = ""
        self.sysDimensions.addMode(self.mdDimensionsMode_Normal)

        self.mdDimensionsMode_FT.id = idcounter
        idcounter += 1
        self.mdDimensionsMode_FT.ident = "DimensionsMode_FT"
        self.mdDimensionsMode_FT.description = ""
        self.sysDimensions.addMode(self.mdDimensionsMode_FT)

        self.vlBinning_1x1.id = idcounter
        idcounter += 1
        self.vlBinning_1x1.ident = "Binning_1x1"
        self.vlBinning_1x1.description = ""
        self.prBinning.addValue(self.vlBinning_1x1)

        self.vlBinning_1x2.id = idcounter
        idcounter += 1
        self.vlBinning_1x2.ident = "Binning_1x2"
        self.vlBinning_1x2.description = ""
        self.prBinning.addValue(self.vlBinning_1x2)

        self.vlBinning_2x1.id = idcounter
        idcounter += 1
        self.vlBinning_2x1.ident = "Binning_2x1"
        self.vlBinning_2x1.description = ""
        self.prBinning.addValue(self.vlBinning_2x1)

        self.vlBinning_2x2.id = idcounter
        idcounter += 1
        self.vlBinning_2x2.ident = "Binning_2x2"
        self.vlBinning_2x2.description = ""
        self.prBinning.addValue(self.vlBinning_2x2)

        self.mdBinningMode_All.id = idcounter
        idcounter += 1
        self.mdBinningMode_All.ident = "BinningMode_All"
        self.mdBinningMode_All.description = ""
        self.prBinning.addMode(self.mdBinningMode_All)

        self.mdAcquisitionMode_Calibration.id = idcounter
        idcounter += 1
        self.mdAcquisitionMode_Calibration.ident = "AcquisitionMode_Calibration"
        self.mdAcquisitionMode_Calibration.description = ""
        self.sysAcquisition.addMode(self.mdAcquisitionMode_Calibration)

        self.mdVariantsMode_Normal.id = idcounter
        idcounter += 1
        self.mdVariantsMode_Normal.ident = "VariantsMode_Normal"
        self.mdVariantsMode_Normal.description = ""
        self.sysVariants.addMode(self.mdVariantsMode_Normal)

        self.mdVariantsMode_Extended.id = idcounter
        idcounter += 1
        self.mdVariantsMode_Extended.ident = "VariantsMode_Extended"
        self.mdVariantsMode_Extended.description = ""
        self.sysVariants.addMode(self.mdVariantsMode_Extended)

        self.mdVariantsMode_Extended_2.id = idcounter
        idcounter += 1
        self.mdVariantsMode_Extended_2.ident = "VariantsMode_Extended_2"
        self.mdVariantsMode_Extended_2.description = ""
        self.sysVariants.addMode(self.mdVariantsMode_Extended_2)

        self.mdARCGenIIIMode_Engineering.id = idcounter
        idcounter += 1
        self.mdARCGenIIIMode_Engineering.ident = "ARCGenIIIMode_Engineering"
        self.mdARCGenIIIMode_Engineering.description = "ARCGenIII engineering mode"
        self.sysARCGenIII.addMode(self.mdARCGenIIIMode_Engineering)

        self.mdFirmwareMode_Engineering.id = idcounter
        idcounter += 1
        self.mdFirmwareMode_Engineering.ident = "FirmwareMode_Engineering"
        self.mdFirmwareMode_Engineering.description = "Firmware engineering mode"
        self.sysFirmware.addMode(self.mdFirmwareMode_Engineering)

        self.mdVariantsMode_Engineering.id = idcounter
        idcounter += 1
        self.mdVariantsMode_Engineering.ident = "VariantsMode_Engineering"
        self.mdVariantsMode_Engineering.description = "Variants engineering mode"
        self.sysVariants.addMode(self.mdVariantsMode_Engineering)

        self.mdAcquisitionMode_Engineering.id = idcounter
        idcounter += 1
        self.mdAcquisitionMode_Engineering.ident = "AcquisitionMode_Engineering"
        self.mdAcquisitionMode_Engineering.description = "Acquisition engineering mode"
        self.sysAcquisition.addMode(self.mdAcquisitionMode_Engineering)

        self.mdSubarrayFeatureMode_Engineering.id = idcounter
        idcounter += 1
        self.mdSubarrayFeatureMode_Engineering.ident = "SubarrayFeatureMode_Engineering"
        self.mdSubarrayFeatureMode_Engineering.description = "SubarrayFeature engineering mode"
        self.sysSubarrayFeature.addMode(self.mdSubarrayFeatureMode_Engineering)

        self.mdExposureCtrlMode_Engineering.id = idcounter
        idcounter += 1
        self.mdExposureCtrlMode_Engineering.ident = "ExposureCtrlMode_Engineering"
        self.mdExposureCtrlMode_Engineering.description = "ExposureCtrl engineering mode"
        self.sysExposureCtrl.addMode(self.mdExposureCtrlMode_Engineering)

        self.mdOutputSourceMode_Engineering.id = idcounter
        idcounter += 1
        self.mdOutputSourceMode_Engineering.ident = "OutputSourceMode_Engineering"
        self.mdOutputSourceMode_Engineering.description = "OutputSource engineering mode"
        self.sysOutputSource.addMode(self.mdOutputSourceMode_Engineering)

        self.mdDimensionsMode_Engineering.id = idcounter
        idcounter += 1
        self.mdDimensionsMode_Engineering.ident = "DimensionsMode_Engineering"
        self.mdDimensionsMode_Engineering.description = "Dimensions engineering mode"
        self.sysDimensions.addMode(self.mdDimensionsMode_Engineering)
        # Marcamos FirmwareMode_tim como elegible para ARCGenIIIMode_Real
        self.mdARCGenIIIMode_Real.addSubMode(self.mdFirmwareMode_tim)
        # Marcamos FirmwareMode_osiris2 como elegible para ARCGenIIIMode_Real
        self.mdARCGenIIIMode_Real.addSubMode(self.mdFirmwareMode_osiris2)
        # Marcamos FirmwareMode_osiris3 como elegible para ARCGenIIIMode_Real
        self.mdARCGenIIIMode_Real.addSubMode(self.mdFirmwareMode_osiris3)
        # Marcamos FirmwareMode_osiris4 como elegible para ARCGenIIIMode_Real
        self.mdARCGenIIIMode_Real.addSubMode(self.mdFirmwareMode_osiris4)
        # Marcamos FirmwareMode_osiris5 como elegible para ARCGenIIIMode_Real
        self.mdARCGenIIIMode_Real.addSubMode(self.mdFirmwareMode_osiris5)
        # Marcamos FirmwareMode_tim como elegible para ARCGenIIIMode_Emulated
        self.mdARCGenIIIMode_Emulated.addSubMode(self.mdFirmwareMode_tim)
        # Marcamos FirmwareMode_osiris2 como elegible para ARCGenIIIMode_Emulated
        self.mdARCGenIIIMode_Emulated.addSubMode(self.mdFirmwareMode_osiris2)
        # Marcamos FirmwareMode_osiris3 como elegible para ARCGenIIIMode_Emulated
        self.mdARCGenIIIMode_Emulated.addSubMode(self.mdFirmwareMode_osiris3)
        # Marcamos FirmwareMode_osiris4 como elegible para ARCGenIIIMode_Emulated
        self.mdARCGenIIIMode_Emulated.addSubMode(self.mdFirmwareMode_osiris4)
        # Marcamos FirmwareMode_osiris5 como elegible para ARCGenIIIMode_Emulated
        self.mdARCGenIIIMode_Emulated.addSubMode(self.mdFirmwareMode_osiris5)
        # Marcamos FirmwareMode_tim como elegible para ARCGenIIIMode_Engineering
        self.mdARCGenIIIMode_Engineering.addSubMode(self.mdFirmwareMode_tim)
        # Marcamos FirmwareMode_osiris2 como elegible para ARCGenIIIMode_Engineering
        self.mdARCGenIIIMode_Engineering.addSubMode(self.mdFirmwareMode_osiris2)
        # Marcamos FirmwareMode_osiris3 como elegible para ARCGenIIIMode_Engineering
        self.mdARCGenIIIMode_Engineering.addSubMode(self.mdFirmwareMode_osiris3)
        # Marcamos FirmwareMode_osiris4 como elegible para ARCGenIIIMode_Engineering
        self.mdARCGenIIIMode_Engineering.addSubMode(self.mdFirmwareMode_osiris4)
        # Marcamos FirmwareMode_osiris5 como elegible para ARCGenIIIMode_Engineering
        self.mdARCGenIIIMode_Engineering.addSubMode(self.mdFirmwareMode_osiris5)
        # Marcamos FirmwareMode_Engineering como elegible para ARCGenIIIMode_Engineering
        self.mdARCGenIIIMode_Engineering.addSubMode(self.mdFirmwareMode_Engineering)
        # Marcamos VariantsMode_Normal como elegible para FirmwareMode_tim
        self.mdFirmwareMode_tim.addSubMode(self.mdVariantsMode_Normal)
        # Marcamos VariantsMode_Extended como elegible para FirmwareMode_osiris2
        self.mdFirmwareMode_osiris2.addSubMode(self.mdVariantsMode_Extended)
        # Marcamos VariantsMode_Extended_2 como elegible para FirmwareMode_osiris3
        self.mdFirmwareMode_osiris3.addSubMode(self.mdVariantsMode_Extended_2)
        # Marcamos VariantsMode_Extended_2 como elegible para FirmwareMode_osiris4
        self.mdFirmwareMode_osiris4.addSubMode(self.mdVariantsMode_Extended_2)
        # Marcamos VariantsMode_Extended_2 como elegible para FirmwareMode_osiris5
        self.mdFirmwareMode_osiris5.addSubMode(self.mdVariantsMode_Extended_2)
        # Marcamos VariantsMode_Normal como elegible para FirmwareMode_Engineering
        self.mdFirmwareMode_Engineering.addSubMode(self.mdVariantsMode_Normal)
        # Marcamos VariantsMode_Extended como elegible para FirmwareMode_Engineering
        self.mdFirmwareMode_Engineering.addSubMode(self.mdVariantsMode_Extended)
        # Marcamos VariantsMode_Extended_2 como elegible para FirmwareMode_Engineering
        self.mdFirmwareMode_Engineering.addSubMode(self.mdVariantsMode_Extended_2)
        # Marcamos VariantsMode_Engineering como elegible para FirmwareMode_Engineering
        self.mdFirmwareMode_Engineering.addSubMode(self.mdVariantsMode_Engineering)
        # Marcamos AcquisitionMode_Normal como elegible para VariantsMode_Normal
        self.mdVariantsMode_Normal.addSubMode(self.mdAcquisitionMode_Normal)
        # Marcamos AcquisitionMode_NormalWindow como elegible para VariantsMode_Normal
        self.mdVariantsMode_Normal.addSubMode(self.mdAcquisitionMode_NormalWindow)
        # Marcamos AcquisitionMode_Shuffling como elegible para VariantsMode_Extended
        self.mdVariantsMode_Extended.addSubMode(self.mdAcquisitionMode_Shuffling)
        # Marcamos AcquisitionMode_FrameTransfer como elegible para VariantsMode_Extended
        self.mdVariantsMode_Extended.addSubMode(self.mdAcquisitionMode_FrameTransfer)
        # Marcamos AcquisitionMode_Normal como elegible para VariantsMode_Extended
        self.mdVariantsMode_Extended.addSubMode(self.mdAcquisitionMode_Normal)
        # Marcamos AcquisitionMode_NormalWindow como elegible para VariantsMode_Extended
        self.mdVariantsMode_Extended.addSubMode(self.mdAcquisitionMode_NormalWindow)
        # Marcamos AcquisitionMode_Shuffling como elegible para VariantsMode_Extended_2
        self.mdVariantsMode_Extended_2.addSubMode(self.mdAcquisitionMode_Shuffling)
        # Marcamos AcquisitionMode_FrameTransfer como elegible para VariantsMode_Extended_2
        self.mdVariantsMode_Extended_2.addSubMode(self.mdAcquisitionMode_FrameTransfer)
        # Marcamos AcquisitionMode_Normal como elegible para VariantsMode_Extended_2
        self.mdVariantsMode_Extended_2.addSubMode(self.mdAcquisitionMode_Normal)
        # Marcamos AcquisitionMode_NormalWindow como elegible para VariantsMode_Extended_2
        self.mdVariantsMode_Extended_2.addSubMode(self.mdAcquisitionMode_NormalWindow)
        # Marcamos AcquisitionMode_Calibration como elegible para VariantsMode_Extended_2
        self.mdVariantsMode_Extended_2.addSubMode(self.mdAcquisitionMode_Calibration)
        # Marcamos AcquisitionMode_Normal como elegible para VariantsMode_Engineering
        self.mdVariantsMode_Engineering.addSubMode(self.mdAcquisitionMode_Normal)
        # Marcamos AcquisitionMode_FrameTransfer como elegible para VariantsMode_Engineering
        self.mdVariantsMode_Engineering.addSubMode(self.mdAcquisitionMode_FrameTransfer)
        # Marcamos AcquisitionMode_Shuffling como elegible para VariantsMode_Engineering
        self.mdVariantsMode_Engineering.addSubMode(self.mdAcquisitionMode_Shuffling)
        # Marcamos AcquisitionMode_NormalWindow como elegible para VariantsMode_Engineering
        self.mdVariantsMode_Engineering.addSubMode(self.mdAcquisitionMode_NormalWindow)
        # Marcamos AcquisitionMode_Calibration como elegible para VariantsMode_Engineering
        self.mdVariantsMode_Engineering.addSubMode(self.mdAcquisitionMode_Calibration)
        # Marcamos AcquisitionMode_Engineering como elegible para VariantsMode_Engineering
        self.mdVariantsMode_Engineering.addSubMode(self.mdAcquisitionMode_Engineering)
        # Marcamos ShuffleLinesMode_Normal como elegible para AcquisitionMode_Shuffling
        self.mdAcquisitionMode_Shuffling.addSubMode(self.mdShuffleLinesMode_Normal)
        # Marcamos ShuffleLinesMode_Normal como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdShuffleLinesMode_Normal)
        # Marcamos ShuffleLines_Full_Range como elegible para ShuffleLinesMode_Normal
        self.mdShuffleLinesMode_Normal.addValue(self.vlShuffleLines_Full_Range)
        # Marcamos ShiftNumberMode_Normal como elegible para AcquisitionMode_Shuffling
        self.mdAcquisitionMode_Shuffling.addSubMode(self.mdShiftNumberMode_Normal)
        # Marcamos ShiftNumberMode_Normal como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdShiftNumberMode_Normal)
        # Marcamos ShiftNumber_Full_Range como elegible para ShiftNumberMode_Normal
        self.mdShiftNumberMode_Normal.addValue(self.vlShiftNumber_Full_Range)
        # Marcamos SubarrayFeatureMode_Off como elegible para AcquisitionMode_Normal
        self.mdAcquisitionMode_Normal.addSubMode(self.mdSubarrayFeatureMode_Off)
        # Marcamos SubarrayFeatureMode_On como elegible para AcquisitionMode_NormalWindow
        self.mdAcquisitionMode_NormalWindow.addSubMode(self.mdSubarrayFeatureMode_On)
        # Marcamos SubarrayFeatureMode_Off como elegible para AcquisitionMode_Calibration
        self.mdAcquisitionMode_Calibration.addSubMode(self.mdSubarrayFeatureMode_Off)
        # Marcamos SubarrayFeatureMode_Off como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdSubarrayFeatureMode_Off)
        # Marcamos SubarrayFeatureMode_On como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdSubarrayFeatureMode_On)
        # Marcamos SubarrayFeatureMode_Engineering como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdSubarrayFeatureMode_Engineering)
        # Marcamos ColsMode_Normal como elegible para SubarrayFeatureMode_On
        self.mdSubarrayFeatureMode_On.addSubMode(self.mdColsMode_Normal)
        # Marcamos ColsMode_Normal como elegible para SubarrayFeatureMode_Engineering
        self.mdSubarrayFeatureMode_Engineering.addSubMode(self.mdColsMode_Normal)
        # Marcamos Cols_Full_Range como elegible para ColsMode_Normal
        self.mdColsMode_Normal.addValue(self.vlCols_Full_Range)
        # Marcamos offsetRowMode_Normal como elegible para SubarrayFeatureMode_On
        self.mdSubarrayFeatureMode_On.addSubMode(self.mdoffsetRowMode_Normal)
        # Marcamos offsetRowMode_Normal como elegible para SubarrayFeatureMode_Engineering
        self.mdSubarrayFeatureMode_Engineering.addSubMode(self.mdoffsetRowMode_Normal)
        # Marcamos offsetRow_Full_Range como elegible para offsetRowMode_Normal
        self.mdoffsetRowMode_Normal.addValue(self.vloffsetRow_Full_Range)
        # Marcamos RowsMode_Normal como elegible para SubarrayFeatureMode_On
        self.mdSubarrayFeatureMode_On.addSubMode(self.mdRowsMode_Normal)
        # Marcamos RowsMode_Normal como elegible para SubarrayFeatureMode_Engineering
        self.mdSubarrayFeatureMode_Engineering.addSubMode(self.mdRowsMode_Normal)
        # Marcamos Rows_Full_Range como elegible para RowsMode_Normal
        self.mdRowsMode_Normal.addValue(self.vlRows_Full_Range)
        # Marcamos offsetColMode_Normal como elegible para SubarrayFeatureMode_On
        self.mdSubarrayFeatureMode_On.addSubMode(self.mdoffsetColMode_Normal)
        # Marcamos offsetColMode_Normal como elegible para SubarrayFeatureMode_Engineering
        self.mdSubarrayFeatureMode_Engineering.addSubMode(self.mdoffsetColMode_Normal)
        # Marcamos offsetCol_Full_Range como elegible para offsetColMode_Normal
        self.mdoffsetColMode_Normal.addValue(self.vloffsetCol_Full_Range)
        # Marcamos ExposureCtrlMode_Normal como elegible para AcquisitionMode_Normal
        self.mdAcquisitionMode_Normal.addSubMode(self.mdExposureCtrlMode_Normal)
        # Marcamos ExposureCtrlMode_FT como elegible para AcquisitionMode_FrameTransfer
        self.mdAcquisitionMode_FrameTransfer.addSubMode(self.mdExposureCtrlMode_FT)
        # Marcamos ExposureCtrlMode_NoShutter como elegible para AcquisitionMode_Shuffling
        self.mdAcquisitionMode_Shuffling.addSubMode(self.mdExposureCtrlMode_NoShutter)
        # Marcamos ExposureCtrlMode_Normal como elegible para AcquisitionMode_NormalWindow
        self.mdAcquisitionMode_NormalWindow.addSubMode(self.mdExposureCtrlMode_Normal)
        # Marcamos ExposureCtrlMode_Calibration como elegible para AcquisitionMode_Calibration
        self.mdAcquisitionMode_Calibration.addSubMode(self.mdExposureCtrlMode_Calibration)
        # Marcamos ExposureCtrlMode_Normal como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdExposureCtrlMode_Normal)
        # Marcamos ExposureCtrlMode_FT como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdExposureCtrlMode_FT)
        # Marcamos ExposureCtrlMode_NoShutter como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdExposureCtrlMode_NoShutter)
        # Marcamos ExposureCtrlMode_Calibration como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdExposureCtrlMode_Calibration)
        # Marcamos ExposureCtrlMode_Engineering como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdExposureCtrlMode_Engineering)
        # Marcamos OpenShutterMode_Off como elegible para ExposureCtrlMode_Normal
        self.mdExposureCtrlMode_Normal.addSubMode(self.mdOpenShutterMode_Off)
        # Marcamos OpenShutterMode_On como elegible para ExposureCtrlMode_Normal
        self.mdExposureCtrlMode_Normal.addSubMode(self.mdOpenShutterMode_On)
        # Marcamos OpenShutterMode_Off como elegible para ExposureCtrlMode_FT
        self.mdExposureCtrlMode_FT.addSubMode(self.mdOpenShutterMode_Off)
        # Marcamos OpenShutterMode_Off como elegible para ExposureCtrlMode_NoShutter
        self.mdExposureCtrlMode_NoShutter.addSubMode(self.mdOpenShutterMode_Off)
        # Marcamos OpenShutterMode_Off como elegible para ExposureCtrlMode_Calibration
        self.mdExposureCtrlMode_Calibration.addSubMode(self.mdOpenShutterMode_Off)
        # Marcamos OpenShutterMode_On como elegible para ExposureCtrlMode_Calibration
        self.mdExposureCtrlMode_Calibration.addSubMode(self.mdOpenShutterMode_On)
        # Marcamos OpenShutterMode_On como elegible para ExposureCtrlMode_Engineering
        self.mdExposureCtrlMode_Engineering.addSubMode(self.mdOpenShutterMode_On)
        # Marcamos OpenShutterMode_Off como elegible para ExposureCtrlMode_Engineering
        self.mdExposureCtrlMode_Engineering.addSubMode(self.mdOpenShutterMode_Off)
        # Marcamos ExpTimeMode_Normal como elegible para ExposureCtrlMode_Normal
        self.mdExposureCtrlMode_Normal.addSubMode(self.mdExpTimeMode_Normal)
        # Marcamos ExpTimeMode_FT como elegible para ExposureCtrlMode_FT
        self.mdExposureCtrlMode_FT.addSubMode(self.mdExpTimeMode_FT)
        # Marcamos ExpTimeMode_Normal como elegible para ExposureCtrlMode_NoShutter
        self.mdExposureCtrlMode_NoShutter.addSubMode(self.mdExpTimeMode_Normal)
        # Marcamos ExpTimeMode_Normal como elegible para ExposureCtrlMode_Calibration
        self.mdExposureCtrlMode_Calibration.addSubMode(self.mdExpTimeMode_Normal)
        # Marcamos ExpTimeMode_Normal como elegible para ExposureCtrlMode_Engineering
        self.mdExposureCtrlMode_Engineering.addSubMode(self.mdExpTimeMode_Normal)
        # Marcamos ExpTimeMode_FT como elegible para ExposureCtrlMode_Engineering
        self.mdExposureCtrlMode_Engineering.addSubMode(self.mdExpTimeMode_FT)
        # Marcamos ExpTime_Full_Range como elegible para ExpTimeMode_Normal
        self.mdExpTimeMode_Normal.addValue(self.vlExpTime_Full_Range)
        # Marcamos ExpTime_FT_Range como elegible para ExpTimeMode_FT
        self.mdExpTimeMode_FT.addValue(self.vlExpTime_FT_Range)
        # Marcamos PixelSpeedMode_FST como elegible para ExposureCtrlMode_Normal
        self.mdExposureCtrlMode_Normal.addSubMode(self.mdPixelSpeedMode_FST)
        # Marcamos PixelSpeedMode_MED como elegible para ExposureCtrlMode_Normal
        self.mdExposureCtrlMode_Normal.addSubMode(self.mdPixelSpeedMode_MED)
        # Marcamos PixelSpeedMode_SLW como elegible para ExposureCtrlMode_Normal
        self.mdExposureCtrlMode_Normal.addSubMode(self.mdPixelSpeedMode_SLW)
        # Marcamos PixelSpeedMode_FST como elegible para ExposureCtrlMode_FT
        self.mdExposureCtrlMode_FT.addSubMode(self.mdPixelSpeedMode_FST)
        # Marcamos PixelSpeedMode_MED como elegible para ExposureCtrlMode_FT
        self.mdExposureCtrlMode_FT.addSubMode(self.mdPixelSpeedMode_MED)
        # Marcamos PixelSpeedMode_SLW como elegible para ExposureCtrlMode_FT
        self.mdExposureCtrlMode_FT.addSubMode(self.mdPixelSpeedMode_SLW)
        # Marcamos PixelSpeedMode_FST como elegible para ExposureCtrlMode_NoShutter
        self.mdExposureCtrlMode_NoShutter.addSubMode(self.mdPixelSpeedMode_FST)
        # Marcamos PixelSpeedMode_MED como elegible para ExposureCtrlMode_NoShutter
        self.mdExposureCtrlMode_NoShutter.addSubMode(self.mdPixelSpeedMode_MED)
        # Marcamos PixelSpeedMode_SLW como elegible para ExposureCtrlMode_NoShutter
        self.mdExposureCtrlMode_NoShutter.addSubMode(self.mdPixelSpeedMode_SLW)
        # Marcamos PixelSpeedMode_FST como elegible para ExposureCtrlMode_Calibration
        self.mdExposureCtrlMode_Calibration.addSubMode(self.mdPixelSpeedMode_FST)
        # Marcamos PixelSpeedMode_MED como elegible para ExposureCtrlMode_Calibration
        self.mdExposureCtrlMode_Calibration.addSubMode(self.mdPixelSpeedMode_MED)
        # Marcamos PixelSpeedMode_SLW como elegible para ExposureCtrlMode_Calibration
        self.mdExposureCtrlMode_Calibration.addSubMode(self.mdPixelSpeedMode_SLW)
        # Marcamos PixelSpeedMode_SLW como elegible para ExposureCtrlMode_Engineering
        self.mdExposureCtrlMode_Engineering.addSubMode(self.mdPixelSpeedMode_SLW)
        # Marcamos PixelSpeedMode_MED como elegible para ExposureCtrlMode_Engineering
        self.mdExposureCtrlMode_Engineering.addSubMode(self.mdPixelSpeedMode_MED)
        # Marcamos PixelSpeedMode_FST como elegible para ExposureCtrlMode_Engineering
        self.mdExposureCtrlMode_Engineering.addSubMode(self.mdPixelSpeedMode_FST)
        # Marcamos numOfFramesMode_Single como elegible para ExposureCtrlMode_Normal
        self.mdExposureCtrlMode_Normal.addSubMode(self.mdnumOfFramesMode_Single)
        # Marcamos numOfFramesMode_Multiple como elegible para ExposureCtrlMode_Normal
        self.mdExposureCtrlMode_Normal.addSubMode(self.mdnumOfFramesMode_Multiple)
        # Marcamos numOfFramesMode_Single como elegible para ExposureCtrlMode_FT
        self.mdExposureCtrlMode_FT.addSubMode(self.mdnumOfFramesMode_Single)
        # Marcamos numOfFramesMode_Multiple como elegible para ExposureCtrlMode_FT
        self.mdExposureCtrlMode_FT.addSubMode(self.mdnumOfFramesMode_Multiple)
        # Marcamos numOfFramesMode_Single como elegible para ExposureCtrlMode_NoShutter
        self.mdExposureCtrlMode_NoShutter.addSubMode(self.mdnumOfFramesMode_Single)
        # Marcamos numOfFramesMode_Multiple como elegible para ExposureCtrlMode_NoShutter
        self.mdExposureCtrlMode_NoShutter.addSubMode(self.mdnumOfFramesMode_Multiple)
        # Marcamos numOfFramesMode_Single como elegible para ExposureCtrlMode_Calibration
        self.mdExposureCtrlMode_Calibration.addSubMode(self.mdnumOfFramesMode_Single)
        # Marcamos numOfFramesMode_Multiple como elegible para ExposureCtrlMode_Calibration
        self.mdExposureCtrlMode_Calibration.addSubMode(self.mdnumOfFramesMode_Multiple)
        # Marcamos numOfFramesMode_Multiple como elegible para ExposureCtrlMode_Engineering
        self.mdExposureCtrlMode_Engineering.addSubMode(self.mdnumOfFramesMode_Multiple)
        # Marcamos numOfFramesMode_Single como elegible para ExposureCtrlMode_Engineering
        self.mdExposureCtrlMode_Engineering.addSubMode(self.mdnumOfFramesMode_Single)
        # Marcamos numOfFrames_Multiple_Range como elegible para numOfFramesMode_Multiple
        self.mdnumOfFramesMode_Multiple.addValue(self.vlnumOfFrames_Multiple_Range)
        # Marcamos numOfFrames_1 como elegible para numOfFramesMode_Single
        self.mdnumOfFramesMode_Single.addValue(self.vlnumOfFrames_1)
        # Marcamos CalibGainMode_Normal como elegible para ExposureCtrlMode_Calibration
        self.mdExposureCtrlMode_Calibration.addSubMode(self.mdCalibGainMode_Normal)
        # Marcamos CalibGainMode_Normal como elegible para ExposureCtrlMode_Engineering
        self.mdExposureCtrlMode_Engineering.addSubMode(self.mdCalibGainMode_Normal)
        # Marcamos CalibGain_Normal_Range como elegible para CalibGainMode_Normal
        self.mdCalibGainMode_Normal.addValue(self.vlCalibGain_Normal_Range)
        # Marcamos OutputSourceMode_0x0 como elegible para AcquisitionMode_Normal
        self.mdAcquisitionMode_Normal.addSubMode(self.mdOutputSourceMode_0x0)
        # Marcamos OutputSourceMode_0x1 como elegible para AcquisitionMode_Normal
        self.mdAcquisitionMode_Normal.addSubMode(self.mdOutputSourceMode_0x1)
        # Marcamos OutputSourceMode_0x2 como elegible para AcquisitionMode_Normal
        self.mdAcquisitionMode_Normal.addSubMode(self.mdOutputSourceMode_0x2)
        # Marcamos OutputSourceMode_0x3 como elegible para AcquisitionMode_Normal
        self.mdAcquisitionMode_Normal.addSubMode(self.mdOutputSourceMode_0x3)
        # Marcamos OutputSourceMode_TWO como elegible para AcquisitionMode_Normal
        self.mdAcquisitionMode_Normal.addSubMode(self.mdOutputSourceMode_TWO)
        # Marcamos OutputSourceMode_ALL como elegible para AcquisitionMode_Normal
        self.mdAcquisitionMode_Normal.addSubMode(self.mdOutputSourceMode_ALL)
        # Marcamos OutputSourceMode_TWO como elegible para AcquisitionMode_FrameTransfer
        self.mdAcquisitionMode_FrameTransfer.addSubMode(self.mdOutputSourceMode_TWO)
        # Marcamos OutputSourceMode_0x0 como elegible para AcquisitionMode_FrameTransfer
        self.mdAcquisitionMode_FrameTransfer.addSubMode(self.mdOutputSourceMode_0x0)
        # Marcamos OutputSourceMode_0x0 como elegible para AcquisitionMode_Shuffling
        self.mdAcquisitionMode_Shuffling.addSubMode(self.mdOutputSourceMode_0x0)
        # Marcamos OutputSourceMode_0x1 como elegible para AcquisitionMode_Shuffling
        self.mdAcquisitionMode_Shuffling.addSubMode(self.mdOutputSourceMode_0x1)
        # Marcamos OutputSourceMode_0x2 como elegible para AcquisitionMode_Shuffling
        self.mdAcquisitionMode_Shuffling.addSubMode(self.mdOutputSourceMode_0x2)
        # Marcamos OutputSourceMode_0x3 como elegible para AcquisitionMode_Shuffling
        self.mdAcquisitionMode_Shuffling.addSubMode(self.mdOutputSourceMode_0x3)
        # Marcamos OutputSourceMode_TWO como elegible para AcquisitionMode_Shuffling
        self.mdAcquisitionMode_Shuffling.addSubMode(self.mdOutputSourceMode_TWO)
        # Marcamos OutputSourceMode_ALL como elegible para AcquisitionMode_Shuffling
        self.mdAcquisitionMode_Shuffling.addSubMode(self.mdOutputSourceMode_ALL)
        # Marcamos OutputSourceMode_0x0 como elegible para AcquisitionMode_NormalWindow
        self.mdAcquisitionMode_NormalWindow.addSubMode(self.mdOutputSourceMode_0x0)
        # Marcamos OutputSourceMode_0x0 como elegible para AcquisitionMode_Calibration
        self.mdAcquisitionMode_Calibration.addSubMode(self.mdOutputSourceMode_0x0)
        # Marcamos OutputSourceMode_0x1 como elegible para AcquisitionMode_Calibration
        self.mdAcquisitionMode_Calibration.addSubMode(self.mdOutputSourceMode_0x1)
        # Marcamos OutputSourceMode_0x2 como elegible para AcquisitionMode_Calibration
        self.mdAcquisitionMode_Calibration.addSubMode(self.mdOutputSourceMode_0x2)
        # Marcamos OutputSourceMode_0x3 como elegible para AcquisitionMode_Calibration
        self.mdAcquisitionMode_Calibration.addSubMode(self.mdOutputSourceMode_0x3)
        # Marcamos OutputSourceMode_TWO como elegible para AcquisitionMode_Calibration
        self.mdAcquisitionMode_Calibration.addSubMode(self.mdOutputSourceMode_TWO)
        # Marcamos OutputSourceMode_ALL como elegible para AcquisitionMode_Calibration
        self.mdAcquisitionMode_Calibration.addSubMode(self.mdOutputSourceMode_ALL)
        # Marcamos OutputSourceMode_0x0 como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdOutputSourceMode_0x0)
        # Marcamos OutputSourceMode_0x1 como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdOutputSourceMode_0x1)
        # Marcamos OutputSourceMode_0x2 como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdOutputSourceMode_0x2)
        # Marcamos OutputSourceMode_0x3 como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdOutputSourceMode_0x3)
        # Marcamos OutputSourceMode_ALL como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdOutputSourceMode_ALL)
        # Marcamos OutputSourceMode_TWO como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdOutputSourceMode_TWO)
        # Marcamos OutputSourceMode_Engineering como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdOutputSourceMode_Engineering)
        # Marcamos RecompositionMode_None como elegible para OutputSourceMode_0x0
        self.mdOutputSourceMode_0x0.addSubMode(self.mdRecompositionMode_None)
        # Marcamos RecompositionMode_None como elegible para OutputSourceMode_0x1
        self.mdOutputSourceMode_0x1.addSubMode(self.mdRecompositionMode_None)
        # Marcamos RecompositionMode_None como elegible para OutputSourceMode_0x2
        self.mdOutputSourceMode_0x2.addSubMode(self.mdRecompositionMode_None)
        # Marcamos RecompositionMode_None como elegible para OutputSourceMode_0x3
        self.mdOutputSourceMode_0x3.addSubMode(self.mdRecompositionMode_None)
        # Marcamos RecompositionMode_QuadCCD como elegible para OutputSourceMode_ALL
        self.mdOutputSourceMode_ALL.addSubMode(self.mdRecompositionMode_QuadCCD)
        # Marcamos RecompositionMode_Serial como elegible para OutputSourceMode_TWO
        self.mdOutputSourceMode_TWO.addSubMode(self.mdRecompositionMode_Serial)
        # Marcamos RecompositionMode_None como elegible para OutputSourceMode_Engineering
        self.mdOutputSourceMode_Engineering.addSubMode(self.mdRecompositionMode_None)
        # Marcamos RecompositionMode_Parallel como elegible para OutputSourceMode_Engineering
        self.mdOutputSourceMode_Engineering.addSubMode(self.mdRecompositionMode_Parallel)
        # Marcamos RecompositionMode_Serial como elegible para OutputSourceMode_Engineering
        self.mdOutputSourceMode_Engineering.addSubMode(self.mdRecompositionMode_Serial)
        # Marcamos RecompositionMode_QuadCCD como elegible para OutputSourceMode_Engineering
        self.mdOutputSourceMode_Engineering.addSubMode(self.mdRecompositionMode_QuadCCD)
        # Marcamos RecompositionMode_QuadIR como elegible para OutputSourceMode_Engineering
        self.mdOutputSourceMode_Engineering.addSubMode(self.mdRecompositionMode_QuadIR)
        # Marcamos RecompositionMode_CDSQuad como elegible para OutputSourceMode_Engineering
        self.mdOutputSourceMode_Engineering.addSubMode(self.mdRecompositionMode_CDSQuad)
        # Marcamos RecompositionMode_HawaiiRG como elegible para OutputSourceMode_Engineering
        self.mdOutputSourceMode_Engineering.addSubMode(self.mdRecompositionMode_HawaiiRG)
        # Marcamos DimensionsMode_Normal como elegible para AcquisitionMode_Normal
        self.mdAcquisitionMode_Normal.addSubMode(self.mdDimensionsMode_Normal)
        # Marcamos DimensionsMode_FT como elegible para AcquisitionMode_FrameTransfer
        self.mdAcquisitionMode_FrameTransfer.addSubMode(self.mdDimensionsMode_FT)
        # Marcamos DimensionsMode_Normal como elegible para AcquisitionMode_Shuffling
        self.mdAcquisitionMode_Shuffling.addSubMode(self.mdDimensionsMode_Normal)
        # Marcamos DimensionsMode_Normal como elegible para AcquisitionMode_Calibration
        self.mdAcquisitionMode_Calibration.addSubMode(self.mdDimensionsMode_Normal)
        # Marcamos DimensionsMode_Normal como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdDimensionsMode_Normal)
        # Marcamos DimensionsMode_FT como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdDimensionsMode_FT)
        # Marcamos DimensionsMode_Engineering como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdDimensionsMode_Engineering)
        # Marcamos uiRowsMode_Normal como elegible para DimensionsMode_Normal
        self.mdDimensionsMode_Normal.addSubMode(self.mduiRowsMode_Normal)
        # Marcamos uiRowsMode_Half como elegible para DimensionsMode_FT
        self.mdDimensionsMode_FT.addSubMode(self.mduiRowsMode_Half)
        # Marcamos uiRowsMode_Normal como elegible para DimensionsMode_Engineering
        self.mdDimensionsMode_Engineering.addSubMode(self.mduiRowsMode_Normal)
        # Marcamos uiRowsMode_Half como elegible para DimensionsMode_Engineering
        self.mdDimensionsMode_Engineering.addSubMode(self.mduiRowsMode_Half)
        # Marcamos uiRows_Full_Range como elegible para uiRowsMode_Normal
        self.mduiRowsMode_Normal.addValue(self.vluiRows_Full_Range)
        # Marcamos uiRows_FTRange como elegible para uiRowsMode_Half
        self.mduiRowsMode_Half.addValue(self.vluiRows_FTRange)
        # Marcamos uiColsMode_Normal como elegible para DimensionsMode_Normal
        self.mdDimensionsMode_Normal.addSubMode(self.mduiColsMode_Normal)
        # Marcamos uiColsMode_Normal como elegible para DimensionsMode_FT
        self.mdDimensionsMode_FT.addSubMode(self.mduiColsMode_Normal)
        # Marcamos uiColsMode_Normal como elegible para DimensionsMode_Engineering
        self.mdDimensionsMode_Engineering.addSubMode(self.mduiColsMode_Normal)
        # Marcamos uiCols_Full_Range como elegible para uiColsMode_Normal
        self.mduiColsMode_Normal.addValue(self.vluiCols_Full_Range)
        # Marcamos BinningMode_All como elegible para AcquisitionMode_Normal
        self.mdAcquisitionMode_Normal.addSubMode(self.mdBinningMode_All)
        # Marcamos BinningMode_All como elegible para AcquisitionMode_FrameTransfer
        self.mdAcquisitionMode_FrameTransfer.addSubMode(self.mdBinningMode_All)
        # Marcamos BinningMode_All como elegible para AcquisitionMode_Shuffling
        self.mdAcquisitionMode_Shuffling.addSubMode(self.mdBinningMode_All)
        # Marcamos BinningMode_All como elegible para AcquisitionMode_NormalWindow
        self.mdAcquisitionMode_NormalWindow.addSubMode(self.mdBinningMode_All)
        # Marcamos BinningMode_All como elegible para AcquisitionMode_Calibration
        self.mdAcquisitionMode_Calibration.addSubMode(self.mdBinningMode_All)
        # Marcamos BinningMode_All como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdBinningMode_All)
        # Marcamos Binning_1x1 como elegible para BinningMode_All
        self.mdBinningMode_All.addValue(self.vlBinning_1x1)
        # Marcamos Binning_1x2 como elegible para BinningMode_All
        self.mdBinningMode_All.addValue(self.vlBinning_1x2)
        # Marcamos Binning_2x1 como elegible para BinningMode_All
        self.mdBinningMode_All.addValue(self.vlBinning_2x1)
        # Marcamos Binning_2x2 como elegible para BinningMode_All
        self.mdBinningMode_All.addValue(self.vlBinning_2x2)

    #----------------------------------------------------------------------
    #  Specific methods
    #----------------------------------------------------------------------


    ## ARCGenIIIMode 
    def get_ARCGenIIIMode(self)-> PORISMode:
        return self.sysARCGenIII.selectedMode

    def set_ARCGenIIIMode(self, mode: PORISMode)-> PORISMode :
        return self.sysARCGenIII.setMode(mode)


    ## FirmwareMode 
    def get_FirmwareMode(self)-> PORISMode:
        return self.sysFirmware.selectedMode

    def set_FirmwareMode(self, mode: PORISMode)-> PORISMode :
        return self.sysFirmware.setMode(mode)


    ## VariantsMode 
    def get_VariantsMode(self)-> PORISMode:
        return self.sysVariants.selectedMode

    def set_VariantsMode(self, mode: PORISMode)-> PORISMode :
        return self.sysVariants.setMode(mode)


    ## AcquisitionMode 
    def get_AcquisitionMode(self)-> PORISMode:
        return self.sysAcquisition.selectedMode

    def set_AcquisitionMode(self, mode: PORISMode)-> PORISMode :
        return self.sysAcquisition.setMode(mode)


    ## prParam ShuffleLines 

    # ShuffleLines
    def get_ShuffleLines(self)-> PORISValue :
        return self.prShuffleLines.selectedValue

    def set_ShuffleLines(self, value: PORISValue)-> PORISValue :
        return self.prShuffleLines.setValue(value)


    ## ShuffleLinesMode 
    def get_ShuffleLinesMode(self)-> PORISMode:
        return self.prShuffleLines.selectedMode

    def set_ShuffleLinesMode(self, mode: PORISMode)-> PORISMode :
        return self.prShuffleLines.setMode(mode)


    ## prParam Acquisition 

    # ShuffleLinesDouble  
    def get_ShuffleLinesDouble(self)-> float :
        return self.prShuffleLines.selectedValue.getData()

    def set_ShuffleLinesDouble(self, data: float)-> float :
        return self.prShuffleLines.selectedValue.setData(data)


    ## prParam ShiftNumber 

    # ShiftNumber
    def get_ShiftNumber(self)-> PORISValue :
        return self.prShiftNumber.selectedValue

    def set_ShiftNumber(self, value: PORISValue)-> PORISValue :
        return self.prShiftNumber.setValue(value)


    ## ShiftNumberMode 
    def get_ShiftNumberMode(self)-> PORISMode:
        return self.prShiftNumber.selectedMode

    def set_ShiftNumberMode(self, mode: PORISMode)-> PORISMode :
        return self.prShiftNumber.setMode(mode)


    ## prParam Acquisition 

    # ShiftNumberDouble  
    def get_ShiftNumberDouble(self)-> float :
        return self.prShiftNumber.selectedValue.getData()

    def set_ShiftNumberDouble(self, data: float)-> float :
        return self.prShiftNumber.selectedValue.setData(data)


    ## SubarrayFeatureMode 
    def get_SubarrayFeatureMode(self)-> PORISMode:
        return self.sysSubarrayFeature.selectedMode

    def set_SubarrayFeatureMode(self, mode: PORISMode)-> PORISMode :
        return self.sysSubarrayFeature.setMode(mode)


    ## prParam Cols 

    # Cols
    def get_Cols(self)-> PORISValue :
        return self.prCols.selectedValue

    def set_Cols(self, value: PORISValue)-> PORISValue :
        return self.prCols.setValue(value)


    ## ColsMode 
    def get_ColsMode(self)-> PORISMode:
        return self.prCols.selectedMode

    def set_ColsMode(self, mode: PORISMode)-> PORISMode :
        return self.prCols.setMode(mode)


    ## prParam SubarrayFeature 

    # ColsDouble  
    def get_ColsDouble(self)-> float :
        return self.prCols.selectedValue.getData()

    def set_ColsDouble(self, data: float)-> float :
        return self.prCols.selectedValue.setData(data)


    ## prParam offsetRow 

    # offsetRow
    def get_offsetRow(self)-> PORISValue :
        return self.proffsetRow.selectedValue

    def set_offsetRow(self, value: PORISValue)-> PORISValue :
        return self.proffsetRow.setValue(value)


    ## offsetRowMode 
    def get_offsetRowMode(self)-> PORISMode:
        return self.proffsetRow.selectedMode

    def set_offsetRowMode(self, mode: PORISMode)-> PORISMode :
        return self.proffsetRow.setMode(mode)


    ## prParam SubarrayFeature 

    # offsetRowDouble  
    def get_offsetRowDouble(self)-> float :
        return self.proffsetRow.selectedValue.getData()

    def set_offsetRowDouble(self, data: float)-> float :
        return self.proffsetRow.selectedValue.setData(data)


    ## prParam Rows 

    # Rows
    def get_Rows(self)-> PORISValue :
        return self.prRows.selectedValue

    def set_Rows(self, value: PORISValue)-> PORISValue :
        return self.prRows.setValue(value)


    ## RowsMode 
    def get_RowsMode(self)-> PORISMode:
        return self.prRows.selectedMode

    def set_RowsMode(self, mode: PORISMode)-> PORISMode :
        return self.prRows.setMode(mode)


    ## prParam SubarrayFeature 

    # RowsDouble  
    def get_RowsDouble(self)-> float :
        return self.prRows.selectedValue.getData()

    def set_RowsDouble(self, data: float)-> float :
        return self.prRows.selectedValue.setData(data)


    ## prParam offsetCol 

    # offsetCol
    def get_offsetCol(self)-> PORISValue :
        return self.proffsetCol.selectedValue

    def set_offsetCol(self, value: PORISValue)-> PORISValue :
        return self.proffsetCol.setValue(value)


    ## offsetColMode 
    def get_offsetColMode(self)-> PORISMode:
        return self.proffsetCol.selectedMode

    def set_offsetColMode(self, mode: PORISMode)-> PORISMode :
        return self.proffsetCol.setMode(mode)


    ## prParam SubarrayFeature 

    # offsetColDouble  
    def get_offsetColDouble(self)-> float :
        return self.proffsetCol.selectedValue.getData()

    def set_offsetColDouble(self, data: float)-> float :
        return self.proffsetCol.selectedValue.setData(data)


    ## ExposureCtrlMode 
    def get_ExposureCtrlMode(self)-> PORISMode:
        return self.sysExposureCtrl.selectedMode

    def set_ExposureCtrlMode(self, mode: PORISMode)-> PORISMode :
        return self.sysExposureCtrl.setMode(mode)


    ## OpenShutterMode 
    def get_OpenShutterMode(self)-> PORISMode:
        return self.sysOpenShutter.selectedMode

    def set_OpenShutterMode(self, mode: PORISMode)-> PORISMode :
        return self.sysOpenShutter.setMode(mode)


    ## prParam ExpTime 

    # ExpTime
    def get_ExpTime(self)-> PORISValue :
        return self.prExpTime.selectedValue

    def set_ExpTime(self, value: PORISValue)-> PORISValue :
        return self.prExpTime.setValue(value)


    ## ExpTimeMode 
    def get_ExpTimeMode(self)-> PORISMode:
        return self.prExpTime.selectedMode

    def set_ExpTimeMode(self, mode: PORISMode)-> PORISMode :
        return self.prExpTime.setMode(mode)


    ## prParam ExposureCtrl 

    # ExpTimeDouble  
    def get_ExpTimeDouble(self)-> float :
        return self.prExpTime.selectedValue.getData()

    def set_ExpTimeDouble(self, data: float)-> float :
        return self.prExpTime.selectedValue.setData(data)


    ## prParam ExposureCtrl 

    # ExpTimeDouble  
    def get_ExpTimeDouble(self)-> float :
        return self.prExpTime.selectedValue.getData()

    def set_ExpTimeDouble(self, data: float)-> float :
        return self.prExpTime.selectedValue.setData(data)


    ## PixelSpeedMode 
    def get_PixelSpeedMode(self)-> PORISMode:
        return self.sysPixelSpeed.selectedMode

    def set_PixelSpeedMode(self, mode: PORISMode)-> PORISMode :
        return self.sysPixelSpeed.setMode(mode)


    ## prParam numOfFrames 

    # numOfFrames
    def get_numOfFrames(self)-> PORISValue :
        return self.prnumOfFrames.selectedValue

    def set_numOfFrames(self, value: PORISValue)-> PORISValue :
        return self.prnumOfFrames.setValue(value)


    ## numOfFramesMode 
    def get_numOfFramesMode(self)-> PORISMode:
        return self.prnumOfFrames.selectedMode

    def set_numOfFramesMode(self, mode: PORISMode)-> PORISMode :
        return self.prnumOfFrames.setMode(mode)


    ## prParam ExposureCtrl 

    # numOfFramesDouble  
    def get_numOfFramesDouble(self)-> float :
        return self.prnumOfFrames.selectedValue.getData()

    def set_numOfFramesDouble(self, data: float)-> float :
        return self.prnumOfFrames.selectedValue.setData(data)


    ## prParam CalibGain 

    # CalibGain
    def get_CalibGain(self)-> PORISValue :
        return self.prCalibGain.selectedValue

    def set_CalibGain(self, value: PORISValue)-> PORISValue :
        return self.prCalibGain.setValue(value)


    ## CalibGainMode 
    def get_CalibGainMode(self)-> PORISMode:
        return self.prCalibGain.selectedMode

    def set_CalibGainMode(self, mode: PORISMode)-> PORISMode :
        return self.prCalibGain.setMode(mode)


    ## prParam ExposureCtrl 

    # CalibGainDouble  
    def get_CalibGainDouble(self)-> float :
        return self.prCalibGain.selectedValue.getData()

    def set_CalibGainDouble(self, data: float)-> float :
        return self.prCalibGain.selectedValue.setData(data)


    ## OutputSourceMode 
    def get_OutputSourceMode(self)-> PORISMode:
        return self.sysOutputSource.selectedMode

    def set_OutputSourceMode(self, mode: PORISMode)-> PORISMode :
        return self.sysOutputSource.setMode(mode)


    ## RecompositionMode 
    def get_RecompositionMode(self)-> PORISMode:
        return self.sysRecomposition.selectedMode

    def set_RecompositionMode(self, mode: PORISMode)-> PORISMode :
        return self.sysRecomposition.setMode(mode)


    ## DimensionsMode 
    def get_DimensionsMode(self)-> PORISMode:
        return self.sysDimensions.selectedMode

    def set_DimensionsMode(self, mode: PORISMode)-> PORISMode :
        return self.sysDimensions.setMode(mode)


    ## prParam uiRows 

    # uiRows
    def get_uiRows(self)-> PORISValue :
        return self.pruiRows.selectedValue

    def set_uiRows(self, value: PORISValue)-> PORISValue :
        return self.pruiRows.setValue(value)


    ## uiRowsMode 
    def get_uiRowsMode(self)-> PORISMode:
        return self.pruiRows.selectedMode

    def set_uiRowsMode(self, mode: PORISMode)-> PORISMode :
        return self.pruiRows.setMode(mode)


    ## prParam Dimensions 

    # uiRowsDouble  
    def get_uiRowsDouble(self)-> float :
        return self.pruiRows.selectedValue.getData()

    def set_uiRowsDouble(self, data: float)-> float :
        return self.pruiRows.selectedValue.setData(data)


    ## prParam Dimensions 

    # uiRowsDouble  
    def get_uiRowsDouble(self)-> float :
        return self.pruiRows.selectedValue.getData()

    def set_uiRowsDouble(self, data: float)-> float :
        return self.pruiRows.selectedValue.setData(data)


    ## prParam uiCols 

    # uiCols
    def get_uiCols(self)-> PORISValue :
        return self.pruiCols.selectedValue

    def set_uiCols(self, value: PORISValue)-> PORISValue :
        return self.pruiCols.setValue(value)


    ## uiColsMode 
    def get_uiColsMode(self)-> PORISMode:
        return self.pruiCols.selectedMode

    def set_uiColsMode(self, mode: PORISMode)-> PORISMode :
        return self.pruiCols.setMode(mode)


    ## prParam Dimensions 

    # uiColsDouble  
    def get_uiColsDouble(self)-> float :
        return self.pruiCols.selectedValue.getData()

    def set_uiColsDouble(self, data: float)-> float :
        return self.pruiCols.selectedValue.setData(data)


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


    ## Action trigger ARCGenIII_expose ##
    def execARCGenIII_expose(self, value: bool) -> bool:
        # Override this
        return True


    ## Action trigger ARCGenIII_init_expose ##
    def execARCGenIII_init_expose(self, value: bool) -> bool:
        # Override this
        return True


    ## Action trigger ARCGenIII_cfg_init_expose ##
    def execARCGenIII_cfg_init_expose(self, value: bool) -> bool:
        # Override this
        return True


    ## Action trigger ARCGenIII_abort ##
    def execARCGenIII_abort(self, value: bool) -> bool:
        # Override this
        return True

