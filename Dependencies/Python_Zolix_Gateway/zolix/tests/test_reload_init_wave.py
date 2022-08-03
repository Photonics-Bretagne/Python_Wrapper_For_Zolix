from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.reload_init_wave()
    test_common.print_result('ReloadInitWave', m)


if __name__ == '__main__':
    test()
