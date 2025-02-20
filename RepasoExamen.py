import tkinter as tk
from tkinter import ttk, messagebox

MENU = {
    "Hamburguesa": {"producto": "Hamburguesa", "precio": 5.0},
    "Papas Fritas": {"producto": "Papas Fritas", "precio": 3.0},
    "Refresco": {"producto": "Refresco", "precio": 2.0},
    "Helado": {"producto": "Helado", "precio": 4.0}
}

class Pedido:
    def __init__(self):
        self.productos_seleccionados = {}
        self.total = 0.0
    
    def agregar_producto(self, producto):
        if producto in self.productos_seleccionados:
            self.productos_seleccionados[producto] += 1
        else:
            self.productos_seleccionados[producto] = 1
        self.calcular_total()
    
    def calcular_total(self):
        self.total = sum(MENU[p]["precio"] * cantidad for p, cantidad in self.productos_seleccionados.items())
    
    def limpiar_pedido(self):
        self.productos_seleccionados.clear()
        self.total = 0.0
    
    def mostrar_resumen(self):
        if not self.productos_seleccionados:
            messagebox.showwarning("Resumen del Pedido", "No has seleccionado ningún producto.")
            return

        resumen = "\n".join(f"{MENU[producto]['producto']} x{cantidad} - ${MENU[producto]['precio'] * cantidad:.2f}" 
                            for producto, cantidad in self.productos_seleccionados.items())
        resumen += f"\n\nTotal: ${self.total:.2f}"
        messagebox.showinfo("Resumen del Pedido", resumen)
    

# Interfaz gráfica
root = tk.Tk()
root.geometry("400x300")
root.title("Sistema de Pedidos")

pedido = Pedido()

tk.Label(root, text="Seleccione los productos:", font=("Arial", 14)).pack()

vars_productos = {}
for key, item in MENU.items():
    var = tk.IntVar()
    chk = ttk.Checkbutton(root, text=f"{item['producto']} - ${item['precio']:.2f}", variable=var)
    chk.pack()
    vars_productos[key] = var  # Guardamos con la clave del menú

def agregar_al_pedido():
    for producto, var in vars_productos.items():
        if var.get():
            pedido.agregar_producto(producto)
    

def limpiar_pedido():
    pedido.limpiar_pedido()
    for var in vars_productos.values():
        var.set(0)

tk.Button(root, text="Agregar al Pedido", command=agregar_al_pedido).pack()
tk.Button(root, text="Mostrar Resumen", command=pedido.mostrar_resumen).pack()
tk.Button(root, text="Limpiar Pedido", command=limpiar_pedido).pack()

root.mainloop()
