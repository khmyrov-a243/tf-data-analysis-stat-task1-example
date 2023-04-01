import pandas as pd
import numpy as np
from scipy.stats import lognorm


chat_id = 973327975 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # оценка параметров логнормального распределения
    s, loc, scale = lognorm.fit(x, floc=0)
    # оценка коэффициента a
    a = np.log(np.mean(x) - 419) - 0.5 * s**2
    return a
