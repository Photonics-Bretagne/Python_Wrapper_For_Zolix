from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.move_to_wave(1.1)
    test_common.print_result('MoveToWave(1.1)', m)


if __name__ == '__main__':
    test()
