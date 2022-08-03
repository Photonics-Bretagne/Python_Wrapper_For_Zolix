from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.get_slit_type()
    test_common.print_result('GetSlitType', m)


if __name__ == '__main__':
    test()
