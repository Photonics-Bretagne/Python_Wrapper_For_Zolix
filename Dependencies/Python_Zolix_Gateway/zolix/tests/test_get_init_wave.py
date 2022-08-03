from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.get_init_wave()
    test_common.print_result('GetInitWave(1)', m)


if __name__ == '__main__':
    test()
