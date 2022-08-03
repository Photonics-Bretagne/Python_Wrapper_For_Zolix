from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.set_grating_param()
    test_common.print_result('SetGratingParam(1, 1, 1)', m)


if __name__ == '__main__':
    test()
