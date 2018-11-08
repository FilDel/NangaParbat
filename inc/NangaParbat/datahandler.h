//
// Author: Valerio Bertone: valerio.bertone@cern.ch
//

#pragma once

#include <string>
#include <vector>
#include <utility>
#include <apfel/matrix.h>

namespace NangaParbat
{
  /**
   * @brief The "DataHandler" class is a mother class that provides a
   * common interface to all datasets. It provides methods to get
   * kinematics, central values, uncertainties, etc.
   */
  class DataHandler
  {
  public:
    /**
     * @brief The process enumerator
     */
    enum Process: int {DY, SIDIS};

    /**
     * @brief Structure containing the kinematic information of one
     * single data set.
     */
    struct Kinematics
    {
      int                      ndata;  //!< Number of data points
      double                   Vs;     //!< Center of mass energy
      std::vector<double>      qTv;    //!< Vector of qT values
      std::pair<double,double> var1b;  //!< Variable 1 integration bounds
      std::pair<double,double> var2b;  //!< Variable 1 integration bounds
      bool                     IntqT;  //!< Whether the bins in qTv are integrated over
      bool                     Intv1;  //!< Whether the bins in Q are integrated over
      bool                     Intv2;  //!< Whether the bins in y are integrated over
    };

    /**
     * @brief The default "DataHandler" constructor.
     */
    DataHandler(std::string const& name, std::string const& datafolder = "../data/");

    /**
     * @brief Function to retrive the name of the dataset object
     */
    std::string GetName() const { return _name; };

    /**
     * @brief Function that returns the process
     */
    Process GetProcess() const { return _proc; };

    /**
     * @brief Function that returns the kinematic object
     */
    Kinematics GetKinematics() const { return _kin; };

    /**
     * @brief Function that returns the mean values
     */
    std::vector<double> GetMeanValues() const { return _mean; };

    /**
     * @brief Function that returns the covariance matrix of the
     * correlated uncertainties.
     */
    apfel::matrix<double> GetCovarianceMatrix() const { return _cov; };

    /**
     * @brief Function that returns the sum in quadrature of the
     * uncorrelated uncertainties.
     */
    std::vector<double> GetUncorrelatedUnc() const { return _unc; };

  protected:
    std::string           _datafolder;  //!< Path to the data folder
    std::string           _name;        //!< Name of the dataset
    Process               _proc;        //!< The process (can be Drell-Yan or SIDIS)
    Kinematics            _kin;         //!< Kinematics block
    std::vector<double>   _mean;        //!< Vector of central values
    std::vector<double>   _unc;         //!< Vector of uncorrelated uncertainties summed in quadrature
    apfel::matrix<double> _cov;         //!< Covariance matrix
  };
}