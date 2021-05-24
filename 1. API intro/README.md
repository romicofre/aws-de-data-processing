# AWS API

AWS API es la interfaz para comunicarse con los recursos de Amazon Web Service.
Para beneficio nuestro, existen utilidades de más alto nivel:

- AWS CLI
- AWS SDK
- AWS MANAGEMENT CONSOLE (Consola/GUI)

Probaremos la API de distintas formas, con un ejemplo muy simple de s3.

## Amazon s3 - Lista de buckets
Qué es un bucket? [Aquí](https://docs.aws.amazon.com/es_es/AmazonS3/latest/userguide/Welcome.html#BasicsBucket)


### API directamente 
Utilizando ejemplos con Postman... [Aquí](https://documenter.getpostman.com/view/10394726/SzYbxHEf?version=latest)
Pero es muy engorroso, mejor probar las siguientes soluciones!

### AWS CLI
- [Instalación](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
- [Iniciar sesión en la CLI](https://docs.aws.amazon.com/es_es/cli/latest/userguide/cli-configure-quickstart.html)
- Listar buckets de s3 con AWS CLI, ejecutando en nuestra terminal:
  **aws s3 list**


### AWS SDK
Utilizando código Python.

### AWS Management Console
Bueno, esta es la interfaz gráfica de AWS, que nos sirve para un vistazo más agradable y con varias opciones a un par de clics.




