# # Run a bunch of definitive stuff. I'm keeping this in a separate file
from main import *

# # Run chi_search 4 times: 1: int-noeff, 2:int-eff, 3:tay-noeff, 4:tay-eff

# m1 = chi_search(fname='optimization-int-noeff-1', length=50, blim=(1, 10),
#                 klim=(0.1, 100), dm_effort=False, dm_method='int',
#                 plot=True)

# m2 = chi_search(fname='optimization-int-eff-1', length=50, blim=(1, 10), klim=(0.1, 100), dm_effort=True, dm_method='int', plot=False)

# m3 = chi_search(fname='optimization-tay-noeff-1', length=50, blim=(1, 10), klim=(0.1, 100), dm_effort=False, dm_method='tay', plot=False)

# m4 = chi_search(fname='optimization-tay-eff-1', length=50, blim=(1, 10), klim=(0.1, 100), dm_effort=True, dm_method='tay', plot=False)

# m1.plot('acc', lcdm, matter)
# m1.distance_modulus(effort=False)
# m1.plot('dm', lcdm, matter)

# m2.plot('acc', lcdm, matter)
# m2.distance_modulus(effort=False)
# m2.plot('dm', lcdm, matter)

# m3.plot('acc', lcdm, matter)
# m3.distance_modulus(effort=True)
# m3.plot('dm', lcdm, matter)

# m4.plot('acc', lcdm, matter)
# m4.distance_modulus(effort=False)
# m4.plot('dm', lcdm, matter)

# Testing double optimization

# m1 = chi_search(fname='double_optimization_test', length=50, blim=(1, 10), klim=(0.1, 100), dm_effort=False, dm_method='int', plot=True)
# m1 = chi_search(fname='double_optimization_int_noeff_fine', length=50, blim=(1.4, 1.7), klim=(0.1, 4.2),
#                 dm_effort=False, dm_method='int', plot=True)

# m1.distance_modulus(effort=False)

# m1.plot('acc', lcdm, matter)
# m1.plot('dm', lcdm, matter)


# Testing q surface function
# m = q_surface(
#     length=50, blim=(1, 4), klim=(0.1, 5), qlim=(-0.75, -0.25)
# )




# Steen has asked about fixing one value (beta, for example) and then plotting
# a bunch of values of kappa and seeing what happens or trying to get close
# to a decent looking plot. Let's try that.

# Start by fixing beta and looking at different kappa
# beta = 2
# kappa = 2

# klook = (0.1, 0.2, 0.3, 0.4, 0.5)
# blook = (1, 2, 3, 4, 5)

# for i in tqdm(klook):
#     temp_mod = model(beta=beta, kappa=i, lam=0.)
#     temp_mod.norm(matter=matter)
#     plt.plot(temp_mod.a, temp_mod.a2norm, label='kappa = {}'.format(i))

# for i in tqdm(blook):
#     temp_mod = model(beta=i, kappa=kappa, lam=0.)
#     temp_mod.norm(matter=matter)
#     plt.plot(temp_mod.a, temp_mod.a2norm, label='beta = {}'.format(i))

# plt.text(x=0.01, y=-1.6, s=r'$\kappa = {}$'.format(kappa))
# plt.xlabel(r'$a$')
# plt.ylabel(r'$\ddot{a}$')
# plt.ylim([-5, 2])
# plt.legend(loc='lower left')
# plt.grid()
# plt.tick_params(axis='both', which='both', direction='in', bottom=True,
#                 top=True, left=True, right=True)
# plt.show()

# top = chi_search_a('optimization_acc', length=50, blim=(1, 10),
#                    klim=(0.1, 100))




# Test our functions
# test_model = model(beta=2, kappa=2, lam=1.)
# print('Done')
# test_model.norm(matter=matter)
# print('Done')
# test_model.distance_modulus(effort=False)
# print('Done')
# test_model.chi_value(eval_both=False)
# print('Done')
# test_model.plot('acc', lcdm, matter)
# print('Done')
# test_model.plot('dm', lcdm, matter)
# print('Done')
# test_model = chi_comp('k', [np.linspace(0, 10, 10)])
# print('Done')
# test_model = chi_search('nosave')
# print('Done')
# test_model = chi_search_a('nosave')
# print('Done')

# @timer
def main():
    """
    Main function
    """

    lcdm = model()
    matter = model(lam=0.)

    # for solver in ('RK45', 'Radau', 'BDF', 'LSODA'):
    #     fname = 'chi_search-12-6-dm-{}'.format(solver)
    #     m1 = chi_search(
    #         fname, length=50, dm_effort=True, dm_method='int',
    #         blim=(1, 4), acc=False, klim=(0.1, 100), solver=solver,
    #     )
    #     m1.distance_modulus(effort=True)
    #     m1.plot('acc')
    #     m1.plot('dm')
    #     m1.chi_value()
    #     print(m1.chi_acc, m1.chi_int, m1.chi_tay)

    if __name__ == '__main__':
        
        # solvers = ('RK45', 'RK23', 'Radau', 'LSODA', 'DOP853')
        solver = ('DOP853')
        # for solver in (solvers):
        print('Solver: {}'.format(solver))
        m = chi_search(
            'chi_search-23-6-dm-{}'.format(solver),
            length=50, blim=(1, 4), klim=(0.1, 100), acc=False,
            dm_effort=False, dm_method='int', solver=solver,
        )
        m.plot('acc')
        m.distance_modulus(effort=False)
        m.plot('dm')




        # data = read_model_data('auto-opt-19-6-dm-1.txt')
        # b1, k1 = specific_function(data, 0)

        # space = np.linspace(1, 3, 100)
        # m2 = chi_comp('k', space, method='dm', beta=b1, dm_effort=True)

        # space = np.linspace(2, 3, 100)
        # m2 = chi_comp('b', space, method='dm', kappa=k1, dm_effort=True)

        # data = read_model_data('auto-opt-19-6-dm-2.txt')
        # b, k = specific_function(data, 0)
        # space = np.linspace(10, 20, 100)
        # m2 = chi_comp('k', space, method='dm', beta=b, dm_method='tay')

        # space = np.linspace(1, 4, 100)
        # m2 = chi_comp('b', space, method='dm', kappa=k, dm_method='tay')

        # data = read_model_data('auto-opt-19-6-dm-3.txt')
        # b, k = specific_function(data, 0)

        # space = np.linspace(1, 4, 100)
        # m2 = chi_comp('k', space, method='dm', beta=b, dm_method='int')

        # space = np.linspace(1, 4, 100)
        # m2 = chi_comp('b', space, method='dm', kappa=k, dm_method='int')

        # m = chi_search(
        #     'nosave', length=50, acc=True, blim=(1, 4), klim=(1, 10), 
        # )
        # m.distance_modulus()
        # m.plot('acc')
        # m.plot('dm')
        # m.distance_modulus(effort=True)
        # m.plot('dm')
        # m.chi_value()
        # print(m.chi_acc, m.chi_int, m.chi_tay)




        # plt.figure()
        # plt.plot(m1.a, m1.a2norm, label='beta = 2')
        # plt.plot(m2.a, m2.a2norm, label='beta = 2.3')
        # plt.plot(lcdm.a, lcdm.a2norm, label='LCDM', c='k', ls='--')
        # plt.xlabel(r'$a$')
        # plt.ylabel(r'$\ddot{a}/\ddot{a}_{\mathrm{M}}$')
        # plt.ylim([-5, 2])
        # plt.tick_params(axis='both', which='both', direction='in',
        #                 bottom=True, top=True, left=True, right=True)
        # plt.legend(loc='lower left')
        # plt.grid()
        # plt.show()

        # m1 = auto_optimize(
        #     'auto-opt-20-6-acc-1', it_num=3, length=50, search_method='acc',
        #     beta_lim_init=(1, 4), kappa_lim_init=(0.1, 100),
        #     require_decreasing_chi=False, plot=True
        # )
        # m1 = chi_search(
        #     'nosave',
        #     acc = True, length=50, blim=(2.0, 4.0), klim=(1.0, 10.0),
        #     lam=0.0, dm_effort=False, dm_method='int', 
        # )
        # m1.distance_modulus()
        # m1.plot('acc')
        # m1.plot('dm')
        # m1.chi_value()
        # print(m1.b, m1.k, m1.chi_int, m1.chi_tay, m1.chi_acc)

        # m2 = auto_optimize(
        #     'auto-opt-19-6-dm-5', it_num=3, length=50, search_method='dm',
        #     beta_lim_init=(1, 4), kappa_lim_init=(0.1, 100),
        #     dm_method='tay', double_eval=False, plot=False
        # )
        # m2.distance_modulus()
        # # m2.plot('acc')
        # # m2.plot('dm')
        # m2.chi_value()
        # print(m2.b, m2.k, m2.chi_int, m2.chi_tay, m2.chi_acc)

        # m3 = auto_optimize(
        #     'auto-opt-19-6-dm-6', it_num=3, length=50, search_method='dm',
        #     beta_lim_init=(1, 4), kappa_lim_init=(0.1, 100),
        #     double_eval=True, plot=False
        # )
        # m3.distance_modulus()
        # # m3.plot('acc')
        # # m3.plot('dm')
        # m3.chi_value()
        # print(m3.b, m3.k, m3.chi_int, m3.chi_tay, m3.chi_acc)



    # chi_search(
    #     'nosave',
    #     acc = False, length=50, 
    #     blim=(2.1412774609218945, 3.211916191382842), klim=(1.53880666728999, 2.308210000934985), 
    #     lam=0.0, dm_effort=True, dm_method='int', double_eval=False, 
    #     solver='BDF'
    # )

    # chi_search(
    #     'nosave',
    #     acc = False, length=50, 
    #     blim=(1.698497190796352, 2.5477457861945276), klim=(28.692277551020414, 43.038416326530616), 
    #     lam=0.0, dm_effort=False, dm_method='tay', double_eval=False, 
    #     solver='BDF'
    # )

    # data = read_model_data('auto-opt-13-6-dm-1.txt')
    # b1, k1 = specific_function(data, 0)
    # m1 = model(beta=b1, kappa=k1, lam=0.)
    # m1.plot('acc')

    # data = read_model_data('auto-opt-13-6-dm-2.txt')
    # b2, k2 = specific_function(data, 0)
    # m2 = model(beta=b2, kappa=k2, lam=0.)
    # m2.plot('acc')

    # data = read_model_data('auto-opt-13-6-dm-3.txt')
    # b3, k3 = specific_function(data, 0)
    # m3 = model(beta=b3, kappa=k3, lam=0.)
    # m3.plot('acc')

    # chi_search('nosave')


    # m2 = chi_search(
    #     'chi_search-12-6-dm-2', length=50, dm_method='tay',
    #     blim=(1, 4), acc=False, klim=(0.1, 100), solver='RK45',
    # )
    # m2.distance_modulus(effort=True)
    # m2.plot('acc')
    # m2.plot('dm')
    # m2.chi_value()
    # print(m2.chi_acc, m2.chi_int, m2.chi_tay)

    # n03 = model(kappa=1, n=-2)
    # n01 = model(kappa=1, n=-1)
    # n0 = model(kappa=1, n=0)
    # n1 = model(kappa=1, n=1)
    # n2 = model(kappa=1, n=2)

    # plt.figure()
    # plt.plot(lcdm.a, lcdm.a2norm, label=r'$\Lambda$CDM', c='k', ls='--')
    # plt.plot(n03.a, n03.a2norm, label=r'$n = -2$')
    # plt.plot(n01.a, n01.a2norm, label=r'$n = -1$')
    # plt.plot(n0.a, n0.a2norm, label=r'$n = 0$')
    # plt.plot(n1.a, n1.a2norm, label=r'$n = 1$')
    # plt.plot(n2.a, n2.a2norm, label=r'$n = 2$')
    # plt.xlabel(r'$a$')
    # plt.ylabel(r'$\ddot{a}/\ddot{a}_{\mathrm{M}}$')
    # plt.ylim([-5, 2])
    # plt.tick_params(axis='both', which='both', direction='in',
    #                 bottom=True, top=True, left=True, right=True)
    # plt.legend(loc='lower left')
    # plt.grid()
    # plt.show()

    # klook = np.linspace(0.5, 0.6, 20)
    # klook = (0.5363157894736842, 1)

    # for i in klook:
    #     m = model(beta=2.900783794692044, kappa=i, lam=0.)
    #     print(i)
    #     plt.plot(m.a, m.a2norm, label=i)

    # plt.plot(lcdm.a, lcdm.a2norm, 'k--', label='LCDM')
    # plt.legend(fontsize=8)
    # plt.ylim(-10, 3)
    # plt.grid()
    # plt.show()

    # m1 = chi_search_a('nosave', length=40, blim=(2.8, 3.0), 
    #                   klim=(0.4, 0.6), plot=False)
    # m1.distance_modulus()
    # m1.plot('acc')
    # m1.plot('dm')

    # m1 = chi_search(
    #     'save-for-paper', length=50, acc=True
    # )
    # m1.plot('acc')
    # m1.distance_modulus()
    # m1.plot('dm')
    # m1.chi_value()
    # print(m1.b, m1.k, m1.chi_int, m1.chi_tay, m1.chi_acc)

    # m2 = chi_search(
    #     'nosave', length=20, acc=True, solver='BDF'
    # )
    # plt.figure()
    # plt.plot(m1.a, m1.a2norm, label='Radau')
    # plt.plot(m2.a, m2.a2norm, label='BDF')
    # plt.show()

    # m1 = auto_optimize(
    #     'auto-opt-acc-4-30', it_num=4, length=30, search_method='acc',
    #     beta_lim_init=(1, 10), kappa_lim_init=(0.1, 100),
    #     require_decreasing_chi=False
    # )
    # m1.distance_modulus()
    # m1.plot('dm', lcdm, matter)

    # # int no effort
    # a = auto_optimize(
    #     'auto-opt-8-acc', it_num=4, dm_effort=False, dm_method='int',
    #     double_eval=False, search_method='dm', length=10,
    # )
    # a.plot('acc')

    # # # int effort
    # a = auto_optimize(
    #     'nosave', it_num=3, dm_effort=True, dm_method='int',
    #     double_eval=False, search_method='dm', length=10
    # )
    # a.plot('acc')

    # # # tay
    # a = auto_optimize(
    #     'nosave', it_num=3, dm_effort=False, dm_method='tay',
    #     double_eval=False, search_method='dm', length=10
    # )
    # a.plot('acc')

    # # # double eval
    # a = auto_optimize(
    #     'nosave', it_num=3, dm_effort=False, dm_method='int',
    #     double_eval=True, search_method='dm', length=10
    # )
    # a.plot('acc')

    # # # acc
    # a = auto_optimize(
    #     'nosave', it_num=3, search_method='acc'
    # )
    # a.distance_modulus()
    # a.plot('dm')

    # m = model(beta=2.900783794692044, kappa=0.5473237318686281, lam=0.)
    # m.plot('acc')
    # m.distance_modulus()
    # m.plot('dm')
    # m1 = chi_search('16may-3-bdf', length=50, blim=(1, 4), klim=(0.1, 100))
    # m1.distance_modulus()
    # m1.plot('acc')
    # m1.plot('dm')

    # m2 = chi_search_a('16may-4-odeint', length=20, blim=(1, 4), klim=(1, 10))
    # m2.distance_modulus()
    # m2.plot('dm')

    # test = chi_search('nosave', dm_effort=False, dm_method='int',
    #                   double_eval=False, plot=True)
    # test2 = model(beta=test.b, kappa=test.k, lam=0.)
    # test.distance_modulus()
    # test.chi_value()
    # test.plot('dm', lcdm, matter)

    # test2.norm(matter=matter)
    # test2.distance_modulus()
    # test2.plot('dm', lcdm, matter)
    # test2.chi_value()

    # print(test.chi_int, test2.chi_int)
    # test.plot('acc', lcdm, matter)
    # test.distance_modulus(effort=False)
    # test.plot('dm', lcdm, matter)
    # test.chi_value()
    # print(test.b, test.k, test.chi_int)
    # test.plot('dm', lcdm, matter)

    # m1 = auto_optimize('auto-opt-acc-lsoda-6-acc', it_num=3, length=50,
    #                    search_method='acc',
    #                    beta_lim_init=(1, 4), kappa_lim_init=(0.1, 10),
    #                    require_decreasing_chi=False)
    # m1.distance_modulus()
    # m1.plot('acc')
    # m1.plot('dm')

    # m2 = auto_optimize('auto-opt-acc-lsoda-6-dm', it_num=3, length=50,
    #                    search_method='dm',
    #                    beta_lim_init=(1, 4), kappa_lim_init=(0.1, 10),
    #                    require_decreasing_chi=False)
    # m2.distance_modulus()
    # m2.plot('acc')
    # m2.plot('dm')

    # m1 = auto_optimize(fname='auto-opt-dbl-bdf-7', it_num=4, length=50,
    #                    search_method='dm', double_eval=True)
    # m1.distance_modulus()
    # m1.plot('acc')
    # m1.plot('dm')
    # print(m1.b, m1.k, m1.chi_int, m1.chi_tay, m1.chi_acc)

    # Look at multiple k values
    # beta = 2.900783794692044
    # # kappa = 0.5473237318686281

    # klook = np.linspace(0.5, 0.6, 20)
    # # blook = (1, 2, 3, 4, 5)

    # for i in tqdm(klook):
    #     temp_mod = model(beta=beta, kappa=i, lam=0.)
    #     plt.plot(temp_mod.a, temp_mod.a2norm, label='kappa = {}'.format(i))

    # # # for i in tqdm(blook):
    # # #     temp_mod = model(beta=i, kappa=kappa, lam=0.)
    # # #     plt.plot(temp_mod.a, temp_mod.a2norm, label='beta = {}'.format(i))

    # plt.plot(lcdm.a, lcdm.a2norm, label='LCDM', c='k', ls='--')
    # plt.text(x=0.01, y=-1.6, s=r'$\beta = {}$'.format(beta))
    # plt.xlabel(r'$a$')
    # plt.ylabel(r'$\ddot{a}$')
    # plt.ylim([-5, 2])
    # plt.legend(loc='lower left', fontsize=8)
    # plt.grid()
    # plt.tick_params(axis='both', which='both', direction='in', bottom=True,
    #                 top=True, left=True, right=True)
    # plt.show()

    # Read model data
    # data = read_model_data('test_again.txt')
    # b1, k1 = specific_function(data, 2)
    # m1 = model(beta=b1, kappa=k1, lam=0.)
    # m1.plot('acc', lcdm, matter)



    # Chi comp search
    # space = np.linspace(0.5, 0.6, 1000)
    # m1 = chi_comp('k', space, beta=2.900783794692044, lam=0., method='acc')
    # m1.distance_modulus()
    # m1.plot('acc')
    # m1.plot('dm')

    # m = chi_search_a(
    #     'nosave', length=20, blim=(1.7541915731156146, 2.6312873596734216), 
    #     klim=(2.124624580842688, 3.1869368712640322), 
    # )
    # m.plot('acc')
    # m.plot('dm')

main()