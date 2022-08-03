from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.initialize()
    test_common.print_result('Initialize', m)


if __name__ == '__main__':
    test()
