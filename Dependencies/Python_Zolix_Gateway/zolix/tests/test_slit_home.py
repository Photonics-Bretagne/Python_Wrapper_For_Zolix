from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.slit_home()
    test_common.print_result('SlitHome(1)', m)


if __name__ == '__main__':
    test()
