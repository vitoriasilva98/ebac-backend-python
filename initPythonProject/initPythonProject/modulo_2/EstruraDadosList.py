usuario_web = [
'André Perez',
'andre.perez',
'andre123',
'andre.perez@gmail.com'
]
print(usuario_web)
print(type(usuario_web))
print("\n")

idade = 20
saldo_em_conta = 723.15
usuario_loggedin = True
usuario_web = [
'André Perez',
idade,
'andre.perez',
'andre123',
'andre.perez@gmail.com',
saldo_em_conta,
usuario_loggedin
]
print(usuario_web)
print(type(usuario_web))
print("\n")

fabricantes_mobile_china = ['xiaomi', 'huawei']
fabricantes_mobile_eua = ['apple', 'motorola']
fabricantes_mobile = fabricantes_mobile_china + fabricantes_mobile_eua
print(fabricantes_mobile_china)
print(fabricantes_mobile_eua)
print(fabricantes_mobile)
print("\n")

fabricantes_mobile_china = fabricantes_mobile[0:2]
fabricantes_mobile_eua = fabricantes_mobile[2:len(fabricantes_mobile)]
print('china: ' + str(fabricantes_mobile_china))
print('eua: ' + str(fabricantes_mobile_eua))

print(len(fabricantes_mobile))