from zolix.tests import test_common


def test():
    test_common.zolix_gateway.set_slit_type()
    test_common.print_result('SetSlitType(1)', m)


if __name__ == '__main__':
    test()
