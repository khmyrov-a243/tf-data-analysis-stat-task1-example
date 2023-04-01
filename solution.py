import pandas as pd
import numpy as np


chat_id = 973327975 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
n = len(x)
mu = np.mean(np.log(x)) # оценка параметра μ
sigma2 = np.var(np.log(x)) # оценка параметра σ^2
a = np.exp(mu + sigma2/2) - 419 # оценка коэффициента a
return a
