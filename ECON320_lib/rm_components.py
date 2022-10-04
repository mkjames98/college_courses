import numpy as np
import pandas as pd


def sample_betas(sample_x, sample_y):
    covxy = np.cov(sample_x, sample_y)[1, 0]
    print("covariance is: " + str(covxy))
    varx = sample_x.var()
    beta1_sample = covxy / varx
    beta0_sample = sample_y.mean() - (beta1_sample * sample_x.mean())
    print(f"sample b_0: {beta0_sample}")
    print(f"sample b_1: {beta1_sample}")

    return beta0_sample, beta1_sample


def predict_y(sample_x, sample_y):
    beta0_sample, beta1_sample = sample_betas(sample_x, sample_y)
    y_pred = beta1_sample * sample_x + beta0_sample
    return y_pred, beta0_sample, beta1_sample


def residuals(sample_y, sample_y_pred):
    return sample_y - sample_y_pred


def ex_sum_sq(y_pred):
    return (y_pred - y_pred.mean()) ** 2


def res_sum_sq(y_column, y_pred):
    return (y_column - y_pred) ** 2


def total_sum_sq(y_column, y_pred):
    return (y_column - y_pred.mean()) ** 2


def generate_sumsq_df(y_column, y_pred):
    sumsq_df = pd.DataFrame()
    ess_arr = ex_sum_sq(y_pred)
    rss_arr = res_sum_sq(y_column, y_pred)
    tss_arr = total_sum_sq(y_column, y_pred)

    data = list(zip(ess_arr, rss_arr, tss_arr, ess_arr + rss_arr))
    sumsq_df = pd.DataFrame(data=data, columns=["ESS", "RSS", "TSS", "ESS+RSS"])
    return sumsq_df


def sigma_hat(residuals):
    return (residuals**2).sum() / (len(residuals) - 2)


def var_se_sample_beta1(residuals, x_column):
    sig_hat2 = sigma_hat(residuals)
    tss_x = ex_sum_sq(x_column).sum()  # ess calculation is the same as xi - xmean
    tss_x_sqrt = tss_x ** (1 / 2)  # since se(sample b_1) = sigmahat2.sqrt() / tssx.sqrt
    var_sample_b1 = (sig_hat2) / tss_x
    se_sample_b1 = (sig_hat2 ** (1 / 2)) / tss_x_sqrt
    print(f"Variance of beta1 : {var_sample_b1} and Standard Error : {se_sample_b1}")
    return var_sample_b1, se_sample_b1
