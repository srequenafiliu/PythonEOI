def precio_total(producto, precio, impuesto=0.21):
    print(f"{producto}: {precio*(1+impuesto)} €")

precio_total('Pan', 2, 0.05)
precio_total('Pan', 2)
precio_total(precio=2, producto='Pan')