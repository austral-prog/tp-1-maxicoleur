def price():
    """
    Ejercicio 8 - Cálculo de Precio Final

    Dado un precio base, calcular e imprimir:
    1. El monto del impuesto (21%)
    2. El subtotal (precio base + impuesto)
    3. El monto de la propina (10% del subtotal)
    4. El precio final (subtotal + propina)
    """
    precio_base = 100
    impuesto=0.21


    el_monto_del_impuesto=precio_base*impuesto
    el_subtotal=precio_base+(precio_base*impuesto)
    el_monto_de_la_propina=(el_subtotal*0.1)
    el_precio_final=el_subtotal+el_monto_de_la_propina

    print(el_monto_del_impuesto)
    print(el_subtotal)
    print(el_monto_de_la_propina)
    print(el_precio_final)
