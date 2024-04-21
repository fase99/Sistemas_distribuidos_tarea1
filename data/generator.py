import csv
import random


def generar_valor():
    return f"valor_{random.randint(1, 100)}"

def generar_csv(nombre_archivo, cantidad_filas):
    with open(nombre_archivo, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['llave', 'valor']) 
        
        
        for i in range(cantidad_filas):
            llave = f"llave_{i+1}"
            valor = generar_valor()
            writer.writerow([llave, valor])

if __name__ == '__main__':
    generar_csv('dataset_1.csv', 2000)
    generar_csv('dataset_2.csv', 2000)
