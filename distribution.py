from scipy.stats import norm
from scipy.stats import expon

def normal_distribution(mu,sigma,n):
    nby2= round(n/2)
    dist= norm(mu, sigma)
    values=[val for val in range(mu-nby2, sigma+nby2)]
    probabilities= [dist.pdf(value) for value in values]
    return values, probabilities

