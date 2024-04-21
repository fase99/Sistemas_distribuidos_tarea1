import grpc
from concurrent import futures
import redis
import cache_pb2
import cache_pb2_grpc
import pandas as pd

GRPC_SERVER_ADDRESS = 'localhost:50051'

REDIS_SERVER_ADDRESS = 'localhost'
REDIS_PORT = 6379

class CacheServicer(cache_pb2_grpc.CacheServicer):
    def __init__(self):

        self.redis_client = redis.StrictRedis(host=REDIS_SERVER_ADDRESS, port=REDIS_PORT, decode_responses=True)
        self.cargar_datos_en_redis('dataset_1.csv', 'dataset_2.csv')

    def cargar_datos_en_redis(self, file1, file2):

        df1 = pd.read_csv(file1)
        for index, row in df1.iterrows():
            self.redis_client.set(row['llave'], row['valor'])

        df2 = pd.read_csv(file2)
        for index, row in df2.iterrows():
            self.redis_client.set(row['llave'], row['valor'])

    def obtener_sala(self, request, context):
        llave = request.llave
        valor = self.redis_client.get(llave)
        if valor:
            return cache_pb2.Respuesta(valor=valor)
        else:
            return cache_pb2.Respuesta(valor="Sala no encontrada")

    def guardar_sala(self, request, context):
        llave = request.llave
        valor = request.valor
        self.redis_client.set(llave, valor)
        return cache_pb2.Respuesta(valor="Sala guardada exitosamente")

def iniciar_servidor():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    cache_pb2_grpc.add_CacheServicer_to_server(CacheServicer(), server)
    server.add_insecure_port(GRPC_SERVER_ADDRESS)
    server.start()
    print("Servidor gRPC iniciado en", GRPC_SERVER_ADDRESS)
    server.wait_for_termination()

if __name__ == '__main__':
    iniciar_servidor()
