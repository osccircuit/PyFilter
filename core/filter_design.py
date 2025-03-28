def freq_samp(n: int, cutoff: list, r: float=1, fs: float=None) -> None:
    """Функция расчета фильтра методом частотной выборки"""
    alpha = (n - 1) / 2
    need_freq_points = []
    m = (n / 2) - 1 if n % 2 == 0 else (n - 1) / 2
    freq_points = [point * fs / n for point in range(n)]
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
                print(f'{index} -- {point}')
    except TypeError as e:
        print(f'{e} Выход из программы')
        raise SystemExit() from e


if __name__ == '__main__':
    freq_samp(n=10, cutoff=[0, 200], fs=1000)