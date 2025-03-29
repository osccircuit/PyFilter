import math

def freq_samp(n: int, cutoff: list, r: float=1, fs: float=None) -> dict:
    """Функция расчета фильтра методом частотной выборки"""
    h_k = 1
    alpha = (n - 1) / 2
    m = (n / 2) - 1 if n % 2 == 0 else (n - 1) / 2
    freq_points = [point * fs / n for point in range(n)]
    need_freq_points = []
    members = {}
    try:
        if not isinstance(cutoff, list):
            raise TypeError(
            'Полосы среза должны быть заданы '
            'в виде списка.'
        )
        if len(cutoff) % 2 != 0:
            raise TypeError(
            'Полосы среза должны быть заданы '
            'попарно.'
        )
        for index, point in enumerate(freq_points):
            if point >= cutoff[0] and point <= cutoff[1]:
                need_freq_points.append(index)
                members[f'{index}'] = [
                    2*abs(h_k)*math.cos(2*math.pi*index*alpha/n),
                    2*r*index*math.cos(2*math.pi/n),
                    -2*r*abs(h_k)*math.cos(2*math.pi*index*(1 + alpha)/n),
                    -r**2
                ]
    except TypeError as e:
        print(f'{e} Выход из программы')
        raise SystemExit() from e
    return members


if __name__ == '__main__':
    mems = freq_samp(n=41, cutoff=[200, 300], fs=1000)
    for name, member in mems.items():
        print(f'{name} - {member}')
