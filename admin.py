from database import get_db

def ver_reportes():
    db = get_db()
    pedidos = db.pedidos.find()
    resumen = {}

    print("\n--- Reporte de Pedidos ---")
    for p in pedidos:
        for item in p["items"]:
            tipo = item["tipo"]
            kilos = item["kilos"]
            ganancia = (item["precio_venta"] - item["costo"]) * kilos
            if tipo not in resumen:
                resumen[tipo] = {"kilos": 0, "ganancia": 0}
            resumen[tipo]["kilos"] += kilos
            resumen[tipo]["ganancia"] += ganancia

    for tipo, datos in resumen.items():
        print(f"{tipo}: {datos['kilos']} kg vendidos, Ganancia: ${datos['ganancia']}")

def editar_stock():
    db = get_db()
    salmones = list(db.salmon.find())
    print("\n--- Editar Stock ---")
    for i, s in enumerate(salmones, 1):
        print(f"{i}. {s['tipo']} - Stock actual: {s['stock']}")
    opcion = int(input("Seleccione el salmón a editar: ")) - 1
    nuevo_stock = int(input("Nuevo stock: "))
    db.salmon.update_one({"tipo": salmones[opcion]["tipo"]}, {"$set": {"stock": nuevo_stock}})
    print("Stock actualizado.")
