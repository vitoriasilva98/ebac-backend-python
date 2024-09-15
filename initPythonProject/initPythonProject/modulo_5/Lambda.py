# Lambda
extrair_provedor_email = lambda email: email.split(sep='@')[-1]

email='maria.lucia@gmail.com'
print(email)

provedor_email = extrair_provedor_email(email)
print(provedor_email)


