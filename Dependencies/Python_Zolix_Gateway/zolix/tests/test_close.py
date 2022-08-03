from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.close()
    test_common.print_result('Close', m)


if __name__ == '__main__':
    test()
