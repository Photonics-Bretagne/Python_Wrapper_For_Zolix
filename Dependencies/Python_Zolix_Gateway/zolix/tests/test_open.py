from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.open()
    test_common.print_result('Open', m)


if __name__ == '__main__':
    test()
