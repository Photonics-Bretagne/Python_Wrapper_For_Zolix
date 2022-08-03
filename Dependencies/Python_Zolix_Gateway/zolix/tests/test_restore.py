from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.restore()
    test_common.print_result('Restore', m)


if __name__ == '__main__':
    test()
