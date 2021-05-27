# -*- coding: utf-8 -*-
"""
List buckets with boto3
"""
import boto3

s3 = boto3.client('s3') # cliente de boto 3
response = s3.list_buckets() # respuesta API mediante sdk
print(response)
print(type(response)) # la respuesta es un diccionario
print(response.keys())

print('\nMis buckets:')
for bucket in response['Buckets']:
    # Imprimiendo
    print(f'  {bucket["Name"]}')