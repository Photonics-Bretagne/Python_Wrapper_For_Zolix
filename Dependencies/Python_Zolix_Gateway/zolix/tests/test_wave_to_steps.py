from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.wave_to_steps()
    test_common.print_result('WaveToSteps(1, 0)', m)


if __name__ == '__main__':
    test()
