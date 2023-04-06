import numpy as np


chat_id = 973327975 # Ваш chat ID, не меняйте название переменной


def solution(x: np.array) -> float:
    mu = np.mean(np.log(x))
    sigma = np.var(np.log(x))
    a = np.exp(mu + sigma / 2) - 419
    return a
