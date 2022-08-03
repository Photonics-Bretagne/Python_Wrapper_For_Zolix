from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.refresh_current_wave()
    test_common.print_result('RefreshCurrentWave', m)


if __name__ == '__main__':
    test()
