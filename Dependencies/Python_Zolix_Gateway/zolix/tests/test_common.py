from zolix.app.zolix_gateway import ZolixGateway
from zolix.app import gateway_configuration

print('Adresse IP du serveur : ' + gateway_configuration.server_ip)
print('Port TCP du serveur : ' + str(gateway_configuration.server_port))

zolix_gateway = ZolixGateway(gateway_configuration.server_ip, gateway_configuration.server_port)
zolix_gateway.connect_to_server()


def print_assert(fonction, ecriture, lecture):
    res = 'KO !!'
    if ecriture == lecture:
        res = "OK"

    print_result(f'{fonction}({ecriture})', res)


def print_assert_two(fonction, p1, p2, m1, m2):
    res='KO !!'
    if ((p1 == m1) & (p2 == m2)):
        res = "OK"

    print_result(f'{fonction}({p1}, {p2})', res)


def print_result(fonction, retour):
    print('[RESULTAT] ' + fonction + ' : "' + str(retour) + '"')
