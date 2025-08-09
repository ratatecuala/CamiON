# Ejemplo inicial. Reemplazar con modelo real de OR-Tools.
from typing import Dict, Any

def optimize_routes(payload: Dict[str, Any]) -> Dict[str, Any]:
    pedidos = payload.get("orders", [])
    deposito = payload.get("depot", "Santiago Centro")
    ordenados = [{"parada": i+1, "id": o.get("id"), "direccion": o.get("address")} for i,o in enumerate(pedidos)]
    resumen = {"total_km": 35, "ahorro_estimado_clp": 72400, "horas_ahorradas": 2}
    return {"deposito": deposito, "ruta": ordenados, "resumen": resumen}
