import numpy
import scipy.stats as si


def _d1(S: float, K: float, r: float, T: float, sigma: float):
    """
    Calculate d1
    """

    return (numpy.log(S/K) + (r + 0.5 * sigma ** 2) * T) / (sigma * numpy.sqrt(T))


def _d2(S: float, K: float, r: float, T: float, sigma: float):
    """
    Calculate d2
    """
    return (numpy.log(S/K) + (r - 0.5 * sigma ** 2) * T) / (sigma * numpy.sqrt(T))


def _euro_call(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """
    Find the theoretical price of a european call option

    INPUTS
    --------------------------------------------------------------------------
    S: the spot price of the underlying asset
    K: the strike price of the option
    T time to maturity
    r: annualized interest rate
    sigma: volatility of the underlyin asset
    """
    d1 = _d1(S, K, T, r, sigma)
    d2 = _d2(S, K, T, r, sigma)

    call = (S * si.norm.cdf(d1, 0., 1.) - K *
            numpy.exp(-r * T) * si.norm.cdf(d2, 0., 1.))

    return round(call, 4)


def _euro_put(S: float, K: float, r: float, T: float, sigma: float) -> float:
    """
    Find the theoretical price of a european put option

    INPUTS
    --------------------------------------------------------------------------
    S: the spot price of the underlying asset
    K: the strike price of the option
    T time to maturity
    r: annualized interest rate
    sigma: volatility of the underlyin asset
    """
    d1 = _d1(S, K, T, r, sigma)
    d2 = _d2(S, K, T, r, sigma)

    put = (K * numpy.exp(-r * T) * si.norm.cdf(-d2, 0., 1.)) - \
        (S * si.norm.cdf(-d1, 0., 1.))

    return round(put, 4)


def european_option(S: float, K: float, r: float, T: float, sigma: float, type="c") -> float:
    """
    Find the theoretical price of a european option

    INPUTS
    --------------------------------------------------------------------------
    S: the spot price of the underlying asset
    K: the strike price of the option
    T time to maturity
    r: annualized interest rate
    sigma: volatility of the underlying asset
    type (str): either 'c' or 'p' for put or call

    returns the price of a european option as float rounded to 4 decimal places. 
    """

    if S < 0 or K < 0:
        return None

    if type.lower() == "c":
        return _euro_call(S, K, T, r, sigma)
    elif type.lower() == "p":
        return _euro_put(S, K, T, r, sigma)
    else:
        return None


if __name__ == "__main__":
    print(european_option(
        S=100, K=-100, r=0.01, T=100, sigma=0.01))
