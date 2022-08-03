from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.connect()
    test_common.print_result('Connect', m)


if __name__ == '__main__':
    test()
