from database import get_db

def realizar_pedido(usuario):
    db = get_db()
    salmones = list(db.salmon.find({}))

    pedido = []
    print("\n--- Realizar Pedido ---")
    for i, s in enumerate(salmones, 1):
        print(f"{i}. {s['tipo']} - ${s['precio_venta']} por kg (Stock: {s['stock']})")

    for _ in range(3):
        opcion = input("\nSeleccione tipo de salmón (1-3 o ENTER para terminar): ")
        if not opcion:
            break
        tipo_index = int(opcion) - 1
        kilos = float(input(f"¿Cuántos kilos de {salmones[tipo_index]['tipo']}? "))
        salmon = salmones[tipo_index]

        if kilos > salmon['stock']:
            print("No hay suficiente stock.")
            continue

        pedido.append({
            "tipo": salmon["tipo"],
            "kilos": kilos,
            "precio_venta": salmon["precio_venta"],
            "costo": salmon["costo"]
        })

        # Actualizar stock
        db.salmon.update_one(
            {"tipo": salmon["tipo"]},
            {"$inc": {"stock": -kilos}}
        )

    if pedido:
        db.pedidos.insert_one({
            "usuario": usuario["username"],
            "items": pedido
        })
        print("Pedido registrado con éxito.")
    else:
        print("No se realizó el pedido.")
