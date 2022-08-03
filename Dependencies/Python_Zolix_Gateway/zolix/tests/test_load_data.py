from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.load_data(352)
    test_common.print_result('LoadData(1)', m)


if __name__ == '__main__':
    test()
