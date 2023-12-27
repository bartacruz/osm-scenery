import dorange
import config
import get

boxes = [
#{'east': '-73', 'north': '-43', 'south': '-44', 'west': '-74', 'xdesc': 'Islas Chile'},
#{'east': '-72', 'north': '-43', 'south': '-44', 'west': '-73', 'xdesc': 'Balmaceda Chile'},
#{'east': '-72', 'north': '-44', 'south': '-45', 'west': '-73', 'xdesc': 'Puerto Cisnes Chile'},
#{'east': '-72', 'north': '-45', 'south': '-46', 'west': '-73', 'xdesc': 'Puerto Aysén Chile'},
#{'east': '-71', 'north': '-40', 'south': '-41', 'west': '-72', 'xdesc': 'Nahuel Huapi - La Angostura '}, 
#{'east': '-71', 'north': '-40', 'south': '-42', 'west': '-72', 'xdesc': 'Bariloche'}, 
#{'east': '-66', 'north': '-33', 'south': '-34', 'west': '-67', 'xdesc': 'RN7 - San Luis'},
#{'east': '-64', 'north': '-31', 'south': '-32', 'west': '-65', 'xdesc': 'CBA - Capiitaal'},
#{'east': '-64', 'north': '-33', 'south': '-34', 'west': '-65', 'xdesc': 'CBA - Rio 4'},
#{'east': '-64', 'north': '-32', 'south': '-33', 'west': '-65', 'xdesc': 'CBA - Rio 3'},
#{'east': '-63', 'north': '-31', 'south': '-32', 'west': '-64', 'xdesc': 'CBA - Villa del Rosario'},
#{'east': '-63', 'north': '-33', 'south': '-34', 'west': '-64', 'xdesc': 'CBA - Juarez Celman'},
#{'east': '-63', 'north': '-32', 'south': '-33', 'west': '-64', 'xdesc': 'CBA - Villa Maria'},
#{'east': '-62', 'north': '-31', 'south': '-32', 'west': '-63', 'xdesc': 'CBA - Este'},
#{'east': '-62', 'north': '-32', 'south': '-33', 'west': '-63', 'xdesc': 'CBA - Marcos Juarez'},
#{'east': '-62', 'north': '-33', 'south': '-34', 'west': '-63', 'xdesc': 'CBA - SE'},
#{'east': '-61', 'north': '-31', 'south': '-32', 'west': '-62', 'xdesc': 'CBA - Santa Fe medio'},
#{'east': '-61', 'north': '-32', 'south': '-33', 'west': '-62', 'xdesc': 'Rosario Oeste'},
#{'east': '-61', 'north': '-33', 'south': '-34', 'west': '-62', 'xdesc': 'Venado Tuerto'},
#{'east': '-60', 'north': '-31', 'south': '-32', 'west': '-61', 'xdesc': 'Santa Fe - Rosario'}, 
#{'east': '-60', 'north': '-32', 'south': '-33', 'west': '-61', 'xdesc': 'Rosario Norte'}, # SAAR
#{'east': '-60', 'north': '-33', 'south': '-34', 'west': '-61', 'xdesc': 'Rosario Sur'},
#{'east': '-59', 'north': '-34', 'south': '-35', 'west': '-60', 'xdesc': 'Delta'},
#{'east': '-59', 'north': '-33', 'south': '-34', 'west': '-60', 'xdesc': 'San Pedro'},
#{'east': '-59', 'north': '-35', 'south': '-36', 'west': '-60', 'xdesc': 'Chivilcoy'},
#{'east': '-58', 'north': '-33', 'south': '-34', 'west': '-59', 'xdesc': "Areco's"},
{'east': '-58', 'north': '-34', 'south': '-35', 'west': '-59', 'xdesc': 'Buenos Aires'},
#{'east': '-58', 'north': '-35', 'south': '-36', 'west': '-59', 'xdesc': 'Chascomus'},
#{'east': '-58', 'north': '-36', 'south': '-37', 'west': '-59', 'xdesc': 'Rauch'},
#{'east': '-58', 'north': '-37', 'south': '-38', 'west': '-59', 'xdesc': 'Balcarce'},
#{'east': '-57', 'north': '-35', 'south': '-36', 'west': '-58', 'xdesc': 'San Borombon'},
#{'east': '-57', 'north': '-34', 'south': '-35', 'west': '-58', 'xdesc': 'La Plata'},
#{'east': '-57', 'north': '-36', 'south': '-37', 'west': '-58', 'xdesc': 'Dolores'},
#{'east': '-57', 'north': '-37', 'south': '-38', 'west': '-58', 'xdesc': 'Mar Azul'},
#{'east': '-57', 'north': '-38', 'south': '-39', 'west': '-58', 'xdesc': 'Mar Del Plata'},
#{'east': '-56', 'north': '-34', 'south': '-35', 'west': '-57', 'xdesc': 'Montevideo'},
#{'east': '-54', 'north': '-34', 'south': '-35', 'west': '-55', 'xdesc': 'Punta del Este'},
#{'east': '-53', 'north': '-34', 'south': '-35', 'west': '-54', 'xdesc': 'Cabo Polonio'},
#{'east': '-53', 'north': '-33', 'south': '-34', 'west': '-54', 'xdesc': 'El Chuy'},
#{'east': '-56', 'north': '-36', 'south': '-37', 'west': '-57', 'xdesc': 'Ruta 11 Atlantica'},
#{'east': '-56', 'north': '-37', 'south': '-38', 'west': '-57', 'xdesc': 'Villa Gesell'},
#{'east': '-67', 'north': '-54', 'south': '-55', 'west': '-68', 'xdesc': 'Ushuaia Este'},
#{'east': '-60', 'north': '-36', 'south': '-37', 'west': '-61', 'xdesc': 'Tapalqué'},
]
if __name__ == "__main__":
    #config.download_enabled=False
    for box in boxes:
        dorange.make_box(box)
