from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.get_current_wave()
    test_common.print_result('GetCurrentWave', m)


if __name__ == '__main__':
    test()
