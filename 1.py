# 10. Провести дисперсионный анализ для определения того, есть ли различия среднего роста среди взрослых футболистов, хоккеистов и штангистов.
# Даны значения роста в трех группах случайно выбранных спортсменов: Футболисты: 173, 175, 180, 178, 177, 185, 183, 182.
# Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180. Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170.

import numpy as np
from scipy.stats import f

# данные по росту спортсменов
football = np.array([173, 175, 180, 178, 177, 185, 183, 182])
hockey = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
weightlifting = np.array(
    [172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])

# вычисление среднего роста в каждой группе
mean_football = np.mean(football)
mean_hockey = np.mean(hockey)
mean_weightlifting = np.mean(weightlifting)

# вычисление общего среднего роста
mean_total = np.mean(np.concatenate((football, hockey, weightlifting)))

# вычисление общей суммы квадратов отклонений (SST)
SST = np.sum((football - mean_total)**2) + np.sum((hockey -
                                                   mean_total)**2) + np.sum((weightlifting - mean_total)**2)

# вычисление суммы квадратов отклонений внутри групп (SSW)
SSW = np.sum((football - mean_football)**2) + np.sum((hockey -
                                                      mean_hockey)**2) + np.sum((weightlifting - mean_weightlifting)**2)

# вычисление суммы квадратов отклонений между группами (SSB)
SSB = football.size * (mean_football - mean_total)**2 + hockey.size * (mean_hockey -
                                                                       mean_total)**2 + weightlifting.size * (mean_weightlifting - mean_total)**2

# вычисление оценки дисперсии внутри групп (MSW) и оценки дисперсии между группами (MSB)
MSW = SSW / (football.size + hockey.size + weightlifting.size - 3)
MSB = SSB / 2

# вычисление статистики F
F = MSB / MSW

# вычисление критического значения F при уровне значимости 0.05 и степенях свободы (2, 25)
F_crit = f.ppf(0.95, 2, 25)

print("F-статистика:", F)
print("Критическое значение F:", F_crit)
if F > F_crit:
    print("Отвергаем нулевую гипотезу: средний рост различается между группами спортсменов")
else:
    print("Не отвергаем нулевую гипотезу: средний рост не различается между группами спортсменов")
