from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.reload_turret()
    test_common.print_result('ReloadTurret', m)


if __name__ == '__main__':
    test()
