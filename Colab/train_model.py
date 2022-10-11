def train():
    f = open('Proj/Colab/bhp.csv', 'r')
    c = f.readlines()

    fm = [line.split(',') for line in c]

    coef = [8.01179032e-02,  3.71694671e+00, -1.50202644e+00,  1.20968537e+02,
            2.45037670e+00, -5.29380959e+01,  1.02788383e+02, -7.03146246e+01,
            -3.89299631e+01, -1.85179731e+01, -1.81540697e+01, -4.72181903e+01,
            -4.55005897e+01, -3.59209534e+01, -5.25789908e+01, -4.21299763e+01,
            -2.79617748e+01, -2.96745769e+01, -3.37243927e+01, -4.30523354e+01,
            -4.63572753e+01, -3.53450116e+01, -5.04870285e+01, -4.31831077e+01,
            -3.37223267e+01, -3.49151967e+01, -1.91070208e+01,  4.95276158e+00,
            -4.11542129e+01, -5.20629169e+01, -2.93242196e+01, -1.62662047e+01,
            -3.25217236e+01,  8.45740507e+01, -3.40426878e+01, -6.15425453e+01,
            -6.13320691e+01, -3.06144991e+01, -3.36020349e+01, -1.34178998e+01,
            -3.20742334e+01,  2.94946931e+01, -3.20698342e-01, -4.93174749e+01,
            -4.54625244e+01, -5.58189272e+01, -3.31242244e+01,  1.19335410e+02,
            -4.54819617e+01, -3.09336005e+01, -2.33894756e+01,  1.00442670e-02,
            -3.86470982e+01, -4.55335854e+01, -4.69654900e+01, -5.92550733e+01,
            4.16783456e+00, -2.01314575e+01, -3.95753039e+01, -3.16579360e+01,
            1.94133601e+01, -4.46304187e+01, -5.07547769e+01, -1.00666974e+02,
            -8.21626819e+01, -3.70589122e+01, -3.83473956e+01,  7.36530127e+01,
            1.73991904e+00,  4.47440957e+02, -2.63046661e+01, -4.00456735e+01,
            -3.98556680e+01, -4.39754317e+01, -4.10811933e+01, -1.98223564e+01,
            -4.25522749e+01, -4.49945156e+01,  1.13061166e+01, -6.04321208e+01,
            -2.52098487e+01, -3.27200188e+01, -5.04560467e+01, -3.46298661e+01,
            4.14911485e+01, -5.03505288e+01, -4.13288114e+01,  1.82466989e+02,
            -4.72985842e+01, -5.08081202e+01, -2.69778133e+01, -4.24743531e+01,
            -4.98208074e+01,  2.12124565e+02, -2.01484665e+01, -1.56873567e+01,
            -4.37881013e+01, -4.37463971e+01, -2.10877803e+01, -1.10673969e+01,
            2.08800227e+01, -2.77036479e+01, -4.64626036e+01, -2.81671140e+01,
            -3.38687410e+01, -4.54143664e+01, -4.85714141e+01, -4.02241751e+01,
            -3.29108865e+01,  3.00173682e+01, -5.27807211e+01, -3.01971759e+01,
            -2.99093209e+01, -4.80652829e+01, -4.56522838e+01, -2.35517698e+01,
            1.11896651e+02, -2.78627212e+01, -2.55017339e+01, -1.70890644e+01,
            -3.04840180e+01, -2.92307205e+01,  1.97964985e+01, -4.63862459e+01,
            -4.20186250e+01, -4.05939894e+01, -4.58807823e+01, -2.50803926e+01,
            -3.50914681e+01, -4.15790158e+01, -3.29829554e+01, -3.12782676e+01,
            -2.53430688e+01, -4.75340592e+01, -3.80801692e+01, -3.07211985e+01,
            -3.53763742e+01, -1.22463343e+01, -2.97711770e+01, -2.77653700e+01,
            -3.08221481e+01, -3.61073264e+01, -2.87473900e+01, -3.38184071e+01,
            -3.77193513e+01, -4.64788305e+01, -4.23407549e+01, -3.32956579e+01,
            -3.03033606e+00,  5.45751659e+01, -3.73781019e+01,  2.73869042e+00,
            5.41618111e+01, -5.19119682e+01, -4.33189969e+01, -4.24165090e+01,
            -3.50757390e+01, -4.79854283e+01, -1.17526862e+01, -3.34704161e+01,
            -2.59593987e+01, -1.90333321e+01, -2.95094680e+01, -4.43623705e+01,
            -4.29802209e+01,  2.36169707e+01, -4.20001452e+01, -4.32104138e+01,
            1.19097141e+02, -3.30946210e+01, -2.90885220e+01,  1.91761915e+00,
            -7.31571043e+01, -4.56828072e+01, -4.81775237e+01, -3.28085602e+01,
            -3.76077309e+01, -6.02778215e+01, -1.28895282e+01, -3.90010899e+01,
            -3.94220924e+01, -7.15630774e+00, -3.83541576e+01, -5.04325429e+01,
            -5.33499522e+01, -2.13479396e+01, -1.94379265e+01, -3.09913413e+01,
            -9.63353632e+00, -5.13735194e+01, -2.24751685e+01, -4.98826792e+01,
            -4.00980355e+01, -3.55553331e+01, -2.53380594e+01, -1.43065784e+01,
            -3.40221252e+01, -5.05177300e+01,  1.44365570e+02, -3.51389474e+01,
            -3.07748477e+01, -3.84123015e+01, -5.62790864e+01, -2.64235563e+01,
            -5.55557724e+00,  7.18866532e+01, -4.83033387e+01, -2.56050982e+01,
            -6.28636417e+01, -2.68619766e+01,  8.24813415e+00, -4.00302357e+01,
            -4.81558302e+01, -5.75514896e-01, -4.28331526e+01, -3.88923639e+01,
            -5.33725612e+01, -4.17693616e+01, -3.14245858e+01, -3.54902082e+01,
            -2.64956404e+01, -3.32053290e+01, -2.85783826e+01, -1.40484274e+01,
            -2.34751639e+01, -6.77647838e+01, -2.12743889e+01,  6.81685726e+00,
            -4.80060709e+01, -4.19980066e+01, -4.50019789e+01, -4.71001063e+01,
            -3.66675665e+01, -1.97061542e+01, -6.96962057e+01, -3.59473456e+01,
            -3.68143320e+01, -2.76889538e+01, -3.12697084e+01, -3.51551155e+01,
            -2.88182259e+01, -5.38375904e+01, -1.32355523e+01]

    intercept = -3.1324178525028543

    pred = []
    for i in range(len(coef)):
        pred.append(0)

    return fm, pred, coef, intercept
