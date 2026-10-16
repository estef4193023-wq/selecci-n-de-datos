import sqlite3
import os

# ==========================================
# MÓDULO 1. CREACIÓN DE LA BASE DE DATOS
# ==========================================

def crear_bd():
    os.makedirs("database", exist_ok=True)

    conexion = sqlite3.connect("database/empleados.db")
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS empleado (
            num_empleado TEXT PRIMARY KEY,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            calle TEXT,
            colonia TEXT,
            puesto TEXT,
            telefono TEXT
        )
    """)

    conexion.commit()
    conexion.close()

    print("Base de datos creada correctamente.")
    print("Base de datos creada con exito")


# ==========================================
# MÓDULO 2. ALTAS DE EMPLEADOS
# ==========================================

def alta_empleado():
    conexion = sqlite3.connect("database/empleados.db")
    cursor = conexion.cursor()

    print("\n===== ALTA DE EMPLEADO =====")

    num_empleado = input("Número de empleado: ").strip()
    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()
    calle = input("Calle: ").strip()
    colonia = input("Colonia: ").strip()
    puesto = input("Puesto del empleado: ").strip()
    telefono = input("Teléfono: ").strip()

    if not num_empleado or not nombre or not apellido:
        print("Error: número de empleado, nombre y apellido son obligatorios.")
        conexion.close()
        return

    try:
        cursor.execute("""
            INSERT INTO empleado (
                num_empleado,
                nombre,
                apellido,
                calle,
                colonia,
                puesto,
                telefono
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            num_empleado,
            nombre,
            apellido,
            calle,
            colonia,
            puesto,
            telefono
        ))

        conexion.commit()
        print("Empleado registrado correctamente.")

    except sqlite3.IntegrityError:
        print("Error: el número de empleado ya existe.")

    except sqlite3.Error as error:
        print(f"Error al registrar al empleado: {error}")

    finally:
        conexion.close()


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

if __name__ == "__main__":
    crear_bd()
    alta_empleado() 