from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.get_filter()
    test_common.print_result('GetFilter', m)


if __name__ == '__main__':
    test()
