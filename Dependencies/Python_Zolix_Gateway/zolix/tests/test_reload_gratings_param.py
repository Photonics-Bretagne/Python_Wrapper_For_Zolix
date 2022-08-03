from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.reload_gratings_param()
    test_common.print_result('ReloadGratingsParam', m)


if __name__ == '__main__':
    test()
