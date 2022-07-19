def appearance(intervals):
    a = [el for el in intervals['lesson']]
    b = [el for el in intervals['pupil']]
    c = [el for el in intervals['tutor']]

    count = 0
    for ind_b in range(len(b)):
        for ind_c in range(len(c)):
            if ind_b % 2 == 0 and ind_c % 2 == 0:
                while True:
                    if b[ind_b] >= a[0] and c[ind_c] >= a[0]:
                        if b[ind_b + 1] <= a[1] and c[ind_c + 1] <= a[1]:
                            if b[ind_b + 1] >= c[ind_c] and b[ind_b + 1] <= c[ind_c + 1] and b[ind_b] <= c[ind_c]:
                                count += b[ind_b + 1] - c[ind_c]
                                break
                            elif b[ind_b] <= c[ind_c + 1] and b[ind_b + 1] >= c[ind_c + 1]:
                                count += c[ind_c + 1] - b[ind_b + 0]
                                break
                            elif b[ind_b] <= c[ind_c] and b[ind_b + 1] >= c[ind_c + 1]:
                                count += c[ind_c + 1] - c[ind_c + 0]
                                break
                            elif b[ind_b] >= c[ind_c] and b[ind_b + 1] <= c[ind_c + 1]:
                                count += b[ind_b + 1] - b[ind_b]
                                break
                            else:
                                break
                        else:
                            if b[-1] > a[1]:
                                b[-1] = a[1]
                            elif c[-1] > a[1]:
                                c[-1] = a[1]

                    else:
                        if b[0] < a[0]:
                            b[0] = a[0]
                        elif c[0] < a[0]:
                            c[0] = a[0]

    return count


if __name__ == '__main__':
    print(appearance({
        'lesson': [1594663200, 1594666800],
        'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
        'tutor': [1594663290, 1594663430, 1594663443, 1594666473]
    }))