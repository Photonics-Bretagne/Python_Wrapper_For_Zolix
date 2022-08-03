from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.get_exit_side_pos()
    test_common.print_result('GetExitSidePos', m)


if __name__ == '__main__':
    test()
