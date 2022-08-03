from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.get_slit_width()
    test_common.print_result('GetSlitWidth(1)', m)


if __name__ == '__main__':
    test()
