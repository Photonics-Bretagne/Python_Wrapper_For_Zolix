from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.get_turret()
    test_common.print_result('GetTurret', m)


if __name__ == '__main__':
    test()
