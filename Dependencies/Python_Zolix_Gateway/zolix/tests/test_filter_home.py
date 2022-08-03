from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.filter_home()
    test_common.print_result('FilterHome', m)


if __name__ == '__main__':
    test()
