from ruamel import yaml

from modules.bcolours import *
from collections import OrderedDict

def GetPertOrd(pertord):
    """
    Transforms the number of the perturbative order in the relative string.
    Input and output are string.
    If the input is not a string GetPertOrd() tries to convert it into the
    right format.
    """
    # Check that 'pertord' is a string, if not try to convert it.
    if type(pertord) is not str:
        print(bcolours.WARNING + "TypeError: the argument of GetPertOrd must be a string." + bcolours.ENDC)
        print(bcolours.WARNING + "Trying to convert it to a string." + bcolours.ENDC)
        pertord = str(pertord)

    # Check if the conversion succeded
    try:
        str(pertord)
    except:
        print(bcolours.FAIL + "Conversion failed. " + bcolours.ENDC)

    # Define the transition from number to name of the perturbative order
    stringord = ""
    if pertord == "1":
      stringord = "NLL"
    if pertord == "2":
      stringord = "NNLL"
    if pertord == "3":
      stringord = "N3LL"
    if pertord == "-1":
      stringord = "NLLp"
    if pertord == "-2":
      stringord = "NNLLp"
    return stringord

# def GetLatexFormula(param):
#     """
#     Function to get the formula of the chosen parameterisation chosen in latex format.
#     Returns an OrderedDict().
#     param   --- String, name of the parameterisation.
#     """
#     if param == "PV19":
#         latexformula = OrderedDict([("parameterisation","$$f_{\\rm NP}(x,\\zeta, b_T)=\\frac{\\exp\\left[ - \\frac{1}{2} g_2 \\log\\left(\\frac{\\zeta}{Q_0^2}\\right) b_T^2 \\right]}{1 + g_1^2(x) b_T^2}$$"),("g1","$$g_1(x) = N_1 \\frac{x^{\\sigma}(1-x)^{\\alpha}}{\\hat{x}^{\\sigma}(1-\\hat{x})^{\\alpha}}$$"),("Q02","$$Q_0^2 = 1\\;{\\rm GeV}^2$$"),("xhat","$$\\hat{x} = 0.1$$")])
#     else:
#         latexformula = OrderedDict([("empty", "latex formula not avaliable yet")])
#         print(bcolours.WARNING + "Latex formula for this parameterisation not yet avaliable" + bcolours.ENDC)
#
#     return latexformula

def TableOfInitialParameters(parameters):
    """
    Function to put initial parameters in the right format for the table in markdown.
    Returns headers and rows (in this order) for the table.
    parameters  --- OrderedDict (Yaml node). Parameters to put in the rows of the table.
    """
    headers = []
    rows = []
    for iter, v in enumerate(parameters):

        # unpack the OrderedDict
        headings, data = [x for x in zip(*parameters[iter].items())]

        ######## for as many tables as parameters:
        # put data and headings in the right format for the table
        # data = [data]
        # headings = [he for he in headings]
        # create one table for each parameter and put it in the markdown
        # writemarkdown.table(mdout, data, headings)

    ########### for only one table with all info:
        rows.append(data)
        headers = [he for he in headings]
    return headers, rows


def TableOfChi2(replicafolder, outfolder):
    """
    Function to put the mean chi2 of the experiments in the right format for the
    table in markdown.
    Returns headers and rows (in this order) for the table.

    replicafolder ---  Folder of the report of the mean of the good replicas.
    outfolder     ---  String, is the folder where the output of the fit is stored.
    """
    headers = ["name", "# points ", "$\chi^2_{unc}$", "$\chi^2_{\lambda^2}$","$\chi^2$"]
    rows = []
    with open(outfolder + "/" + replicafolder + "/Report.yaml", "r") as rep:
        reportrep = yaml.load(rep, Loader=yaml.RoundTripLoader)

        globalchi2     = reportrep["Global chi2"]
        totpoints      = 0
        totpchi2       = 0
        totpenaltychi2 = 0
        totuncchi2     = 0

        for expdata in reportrep["Experiments"]:
            expname = expdata["Name"]

            npoints    = len(expdata["Predictions"])
            totpoints += npoints

            pchi2     = expdata["partial chi2"]
            totpchi2 += pchi2 * npoints

            penaltychi2     = expdata["penalty chi2"]
            totpenaltychi2 += penaltychi2 * npoints

            uncchi2      = pchi2 - penaltychi2
            totuncchi2  += uncchi2 * npoints

            onerow = (expname, npoints, round(uncchi2, 6), round(penaltychi2, 6), pchi2)
            rows.append(onerow)

        TotUncChi2    = totuncchi2 / totpoints
        TotPenalty    = totpenaltychi2 / totpoints
        TotNormChi2   = totpchi2 / totpoints

        lastrow = ("Total", totpoints, round(TotUncChi2, 6) , round(TotPenalty, 6), round(TotNormChi2, 6))
        rows.append(lastrow)

    return headers, rows
