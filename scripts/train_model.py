def train():
    f = open('bhp.csv', 'r')
    c = f.readlines()

    fm = [line.split(',') for line in c]

    coef = [9.41690703e-02, -3.48892500e+00, -5.95624386e+00,  1.15212903e+08,
            1.15212787e+08,  1.15212727e+08,  1.15212901e+08,  1.15212701e+08,
            1.15212740e+08,  1.15212762e+08,  1.15212765e+08,  1.15212734e+08,
            1.15212738e+08,  1.15212741e+08,  1.15212739e+08,  1.15212739e+08,
            1.15212751e+08,  1.15212752e+08,  1.15212747e+08,  1.15212737e+08,
            1.15212735e+08,  1.15212747e+08,  1.15212735e+08,  1.15212738e+08,
            1.15212746e+08,  1.15212749e+08,  1.15212768e+08,  1.15212798e+08,
            1.15212741e+08,  1.15212729e+08,  1.15212751e+08,  1.15212762e+08,
            1.15212748e+08,  1.15212861e+08,  1.15212750e+08,  1.15212722e+08,
            1.15212717e+08,  1.15212753e+08,  1.15212754e+08,  1.15212766e+08,
            1.15212750e+08,  1.15212807e+08,  1.15212774e+08,  1.15212728e+08,
            1.15212730e+08,  1.15212724e+08,  1.15212748e+08,  1.15212911e+08,
            1.15212732e+08,  1.15212750e+08,  1.15212753e+08,  1.15212782e+08,
            1.15212747e+08,  1.15212734e+08,  1.15212736e+08,  1.15212722e+08,
            1.15212790e+08,  1.15212761e+08,  1.15212742e+08,  1.15212748e+08,
            1.15212802e+08,  1.15212736e+08,  1.15212732e+08,  1.15212675e+08,
            1.15212705e+08,  1.15212741e+08,  1.15212747e+08,  1.15212849e+08,
            1.15212785e+08,  1.15213190e+08,  1.15212759e+08,  1.15212738e+08,
            1.15212740e+08,  1.15212736e+08,  1.15212741e+08,  1.15212755e+08,
            1.15212739e+08,  1.15212738e+08,  1.15212790e+08,  1.15212720e+08,
            1.15212753e+08,  1.15212749e+08,  1.15212731e+08,  1.15212747e+08,
            1.15212821e+08,  1.15212732e+08,  1.15212739e+08,  1.15212971e+08,
            1.15212739e+08,  1.15212731e+08,  1.15212756e+08,  1.15212740e+08,
            1.15212732e+08,  1.15213022e+08,  1.15212758e+08,  1.15212763e+08,
            1.15212737e+08,  1.15212737e+08,  1.15212760e+08,  1.15212769e+08,
            1.15212803e+08,  1.15212756e+08,  1.15212733e+08,  1.15212752e+08,
            1.15212747e+08,  1.15212737e+08,  1.15212731e+08,  1.15212740e+08,
            1.15212746e+08,  1.15212812e+08,  1.15212732e+08,  1.15212745e+08,
            1.15212754e+08,  1.15212750e+08,  1.15212723e+08,  1.15212754e+08,
            1.15212880e+08,  1.15212753e+08,  1.15212755e+08,  1.15212764e+08,
            1.15212749e+08,  1.15212755e+08,  1.15212803e+08,  1.15212736e+08,
            1.15212745e+08,  1.15212744e+08,  1.15212735e+08,  1.15212756e+08,
            1.15212751e+08,  1.15212742e+08,  1.15212747e+08,  1.15212753e+08,
            1.15212755e+08,  1.15212735e+08,  1.15212741e+08,  1.15212750e+08,
            1.15212748e+08,  1.15212769e+08,  1.15212751e+08,  1.15212750e+08,
            1.15212754e+08,  1.15212745e+08,  1.15212752e+08,  1.15212747e+08,
            1.15212743e+08,  1.15212733e+08,  1.15212740e+08,  1.15212744e+08,
            1.15212783e+08,  1.15212818e+08,  1.15212748e+08,  1.15212784e+08,
            1.15212827e+08,  1.15212732e+08,  1.15212735e+08,  1.15212740e+08,
            1.15212746e+08,  1.15212735e+08,  1.15212768e+08,  1.15212746e+08,
            1.15212768e+08,  1.15212760e+08,  1.15212757e+08,  1.15212735e+08,
            1.15212737e+08,  1.15212802e+08,  1.15212740e+08,  1.15212737e+08,
            1.15212885e+08,  1.15212749e+08,  1.15212752e+08,  1.15212794e+08,
            1.15212713e+08,  1.15212738e+08,  1.15212734e+08,  1.15212748e+08,
            1.15212745e+08,  1.15212715e+08,  1.15212768e+08,  1.15212743e+08,
            1.15212744e+08,  1.15212771e+08,  1.15212741e+08,  1.15212729e+08,
            1.15212732e+08,  1.15212762e+08,  1.15212760e+08,  1.15212748e+08,
            1.15212755e+08,  1.15212733e+08,  1.15212758e+08,  1.15212730e+08,
            1.15212740e+08,  1.15212742e+08,  1.15212763e+08,  1.15212777e+08,
            1.15212745e+08,  1.15212731e+08,  1.15212927e+08,  1.15212749e+08,
            1.15212748e+08,  1.15212744e+08,  1.15212726e+08,  1.15212755e+08,
            1.15212774e+08,  1.15212852e+08,  1.15212732e+08,  1.15212756e+08,
            1.15212716e+08,  1.15212751e+08,  1.15212785e+08,  1.15212734e+08,
            1.15212746e+08,  1.15212767e+08,  1.15212735e+08,  1.15212741e+08,
            1.15212729e+08,  1.15212744e+08,  1.15212751e+08,  1.15212758e+08,
            1.15212745e+08,  1.15212746e+08,  1.15212752e+08,  1.15212765e+08,
            1.15212756e+08,  1.15212706e+08,  1.15212761e+08,  1.15212795e+08,
            1.15212734e+08,  1.15212739e+08,  1.15212737e+08,  1.15212734e+08,
            1.15212747e+08,  1.15212762e+08,  1.15212721e+08,  1.15212747e+08,
            1.15212741e+08,  1.15212752e+08,  1.15212749e+08,  1.15212746e+08,
            1.15212753e+08,  1.15212727e+08,  1.15212766e+08]

    intercept = -20.1324178525028543

    pred = []
    for i in range(len(coef)):
        pred.append(0)

    fm[0][-1] = fm[0][-1].strip('\n')
    fm[0].pop(2)
    return fm, pred, coef, intercept
