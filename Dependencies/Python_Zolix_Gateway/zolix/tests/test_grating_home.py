from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.grating_home()
    test_common.print_result('GratingHome', m)


if __name__ == '__main__':
    test()
