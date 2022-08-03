from zolix.tests import test_common


def test():
    groove, blaze = test_common.zolix_gateway.get_grating_param(1)
    test_common.print_result('GetGratingParam(1)', f'groove={groove} ; blaze={blaze}')


if __name__ == '__main__':
    test()
