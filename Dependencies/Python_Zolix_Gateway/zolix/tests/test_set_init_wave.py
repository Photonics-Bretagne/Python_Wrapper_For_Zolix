from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.set_init_wave()
    test_common.print_result('SetInitWave(1, 0)', m)


if __name__ == '__main__':
    test()
