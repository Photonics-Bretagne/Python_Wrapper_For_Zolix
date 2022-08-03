from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.stop()
    test_common.print_result('Stop', m)


if __name__ == '__main__':
    test()
