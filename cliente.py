import grpc
import time
import cache_pb2
import cache_pb2_grpc
import random

# Dirección y puerto en el que el servidor gRPC está escuchando las solicitudes del cliente
GRPC_SERVER_ADDRESS = 'localhost:50051'

def obtener_sala(llave):
    # Establecer la conexión con el servidor gRPC
    with grpc.insecure_channel(GRPC_SERVER_ADDRESS) as channel:
        # Crear un cliente gRPC
        stub = cache_pb2_grpc.CacheStub(channel)
        
        # Crear una solicitud para obtener una sala
        request = cache_pb2.Consulta(llave=llave)
        
        # Medir el tiempo de inicio
        start_time = time.time()
        
        # Enviar la solicitud al servidor y recibir la respuesta
        response = stub.obtener_sala(request)
        
        # Calcular el tiempo transcurrido
        end_time = time.time()
        elapsed_time = end_time - start_time
        
    
        print("Valor de la sala:", response.valor)
        print("Tiempo de respuesta del servidor:", elapsed_time, "segundos")

def guardar_sala(llave, valor):
    with grpc.insecure_channel(GRPC_SERVER_ADDRESS) as channel:
        stub = cache_pb2_grpc.CacheStub(channel)
        
        request = cache_pb2.Consulta(llave=llave, valor=valor)
        
        start_time = time.time()
        
        response = stub.guardar_sala(request)
        
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        print("Respuesta del servidor:", response.valor)
        print("Tiempo de respuesta del servidor:", elapsed_time, "segundos")


if __name__ == '__main__':
    for  i in range(20):
        llave= f"llave_{random.randint(1, 2000)}"
        obtener_sala(llave)


"""     obtener_sala("llave_1990")
    obtener_sala("llave_245")
 """