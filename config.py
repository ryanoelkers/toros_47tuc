""" This serves as the configuration file for the TOROS pipeline. """


class Configuration:

    # Computer for reduction
    MACHINE = ## name of your computer
    RAW_FILE_EXTENSION = '.fits'
    FILE_EXTENSION = '.fits'

    # update for different data products
    FIELD = 'FIELD_0e.001'
    RA = 6.48297237 
    DEC = -72.2141311  
    BAD_DATES = '2024-10-03'
    NSKY_STARS = 20000

    # are there additional known transients or variables you want photometry for?
    KNOWN_VARIABLES = 'Y'

    # steps to skip Y for skip, N for execute
    CLEAN_SKIP = 'N'
    MASTER_SKIP = 'N'
    DIFFERENCE_SKIP = 'N'
    PHOTOMETRY_SKIP = 'N'
    LIGHTCURVE_SKIP = 'N'
    SYSTEMATICS_SKIP = 'N'

    # how do you want to clean the image? Y for execute, N for skip
    SUBTRACT_BIAS = "Y"
    SUBTRACT_DARK = "Y"
    DIVIDE_FLAT = "Y"
    CLIP_IMAGE = "Y"
    SUBTRACT_SKY = "Y"
    PLATE_SOLVE = "Y"
    WRITE_SKY = 'N'

    # telescope information
    PIXEL_SIZE = 0.4959  #  0.496 arcsec per pixel
    NUM_PIXELS = 10560  # pixels per side
    TOROS_DEC_LIMIT = 26.66  # declination limit of the telescope in degrees
    FOV = (PIXEL_SIZE * NUM_PIXELS) / 3600.
    SEARCH_DIST = FOV * 0.8
    EXP_TIME = 300
    GAIN = 0.380  # in e-/ADU

    # get image information
    AXS_X_RW = 12000
    AXS_Y_RW = 10600
    AXS_X = 10560
    AXS_Y = 10560
    AXS = 10560
    CHP_X = 1320
    CHP_Y = 5280

    # update the differencing information, primarily the number of stars to use, and the kernel size
    KRNL = 2  # kernel size 2 * KNRL + 1
    STMP = 10  # stamp size ot use 2 * STMP + 1
    ORDR = 1  # order of the kernel to use, 0 is stationary, 1 or 2 is spatially varying
    NRSTARS = 1500  # number of stars used to solve for kernel
    BRIGHT_STARS = 20000  # the top stars to search for in kernel stars
    KERNEL_LIMIT = 0.5  # the maximum allowable offset in zeropoint in magnitudes
    AXS_LIMIT = 100  # the number of pixel close to the edge of the frame to use
    RMS_LOW_LIMIT = 0.005  # the lower limit on precision to use for the kernel stars
    RMS_UP_LIMIT = 0.02  # the upper limit on precision to use for the kernel stars

    # update sky subtraction specific information
    PIX = 220

    # a photometry configuration
    FWHM = 15.  # fwhm of the image
    THRESHOLD = 5.  # the threshold for a source above the background

    # aperture information
    APER_SIZE = 16  # circular aperture

    # aperture annulus for the sky background automatically determined from the main aperture
    ANNULI_INNER = APER_SIZE + 2
    ANNULI_OUTER = APER_SIZE + 4

    # output paths for logging, temporary files, figures etc
    WORKING_DIRECTORY = ""  ## where does your code sit?
    LOG_DIRECTORY = WORKING_DIRECTORY + 'logs/'
    CODE_DIFFERENCE_DIRECTORY = WORKING_DIRECTORY + 'difference/'

    # input paths for data etc
    DATA_DIRECTORY = ""  # where does your data sit?
    RAW_DIRECTORY = ""  # where does your raw data sit?
    CLEAN_DIRECTORY = DATA_DIRECTORY + "clean/"
    MASTER_MAIN_DIRECTORY = DATA_DIRECTORY + "master/"
    MASTER_DIRECTORY = DATA_DIRECTORY + "master/" + FIELD + "/"
    MASTER_TMP_DIRECTORY = MASTER_DIRECTORY + "tmp_master/"
    CENTROID_DIRECTORY = MASTER_DIRECTORY + "centroids/"
    CALIBRATION_DIRECTORY = DATA_DIRECTORY + "calibration/"
    BIAS_DIRECTORY = CALIBRATION_DIRECTORY + "tmp_bias/"
    FLAT_DIRECTORY = CALIBRATION_DIRECTORY + "tmp_flat/"
    DARK_DIRECTORY = CALIBRATION_DIRECTORY + "tmp_dark/"
    LIGHTCURVE_DIRECTORY = DATA_DIRECTORY + "lc/"
    LIGHTCURVE_FIELD_DIRECTORY = LIGHTCURVE_DIRECTORY + FIELD + "/"
    LIGHTCURVE_FIELD_RAW_DIRECTORY = LIGHTCURVE_DIRECTORY + FIELD + "/raw/"
    LIGHTCURVE_FIELD_DETREND_DIRECTORY = LIGHTCURVE_DIRECTORY + FIELD + "/detrend"
    DIFFERENCED_DIRECTORY = DATA_DIRECTORY + "diff/"
    FLUX_DIRECTORY = DATA_DIRECTORY + "flux/"

    # directory_list
    DIRECTORIES = [ANALYSIS_DIRECTORY, DATA_DIRECTORY, LOG_DIRECTORY, CALIBRATION_DIRECTORY, FLUX_DIRECTORY,
                   QUERIES_DIRECTORY, CLEAN_DIRECTORY, MASTER_MAIN_DIRECTORY, MASTER_DIRECTORY, MASTER_TMP_DIRECTORY,
                   LIGHTCURVE_DIRECTORY, CENTROID_DIRECTORY, RAW_DIRECTORY, BIAS_DIRECTORY, DARK_DIRECTORY,
                   FLAT_DIRECTORY, DIFFERENCED_DIRECTORY, CODE_DIFFERENCE_DIRECTORY, LIGHTCURVE_FIELD_DIRECTORY,
                   LIGHTCURVE_FIELD_RAW_DIRECTORY, LIGHTCURVE_FIELD_DETREND_DIRECTORY]
