import pandas as pd
import numpy as np
from scipy.stats import lognorm


chat_id = 973327975 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
# Оценка параметров логнормального распределения
mu = np.mean(np.log(x - 419))
sigma = np.std(np.log(x - 419))

# Оценка параметра "a"
a = np.exp(mu + sigma ** 2 / 2)

return a
