# Especificación API

## POST /optimizar
Recibe pedidos y devuelve el orden sugerido y un resumen de ahorro.

### Ejemplo de request
```json
{
  "orders": [
    {"id": 1, "address": "Av. Providencia 125, Santiago"},
    {"id": 2, "address": "Los Olivos 475, Ñuñoa"}
  ],
  "depot": "Av. Apoquindo 3500, Las Condes",
  "vehicle_count": 1
}
```

### Ejemplo de response
```json
{
  "deposito": "Av. Apoquindo 3500, Las Condes",
  "ruta": [
    {"parada": 1, "id": 1, "direccion": "Av. Providencia 125, Santiago"}
  ],
  "resumen": {"total_km": 35, "ahorro_estimado_clp": 72400, "horas_ahorradas": 2}
}
```
