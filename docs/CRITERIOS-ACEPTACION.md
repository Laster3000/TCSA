# Criterios de aceptacion de checkpoints TCSA (PENDIENTES, NO EJECUTADOS)
1. Guardar dos proyectos y dos conversaciones sin mezclar identidades ni textos.
2. Capturar decision/causa/alternativa descartada, intento fallido, correccion real, build/test/recibo, NEXT_ACTION; recuperar de modo comprensible.
3. Dejar un segmento inaccesible: marcar UNKNOWN_GAP, nunca inventar transcripcion.
4. Fallo en mitad de escritura: puntero anterior LKG sigue recuperable; artefacto incompleto nunca COMMITTED.
5. Dos escritores concurrentes: conflicto CAS controlado, preservar ambas ramas, no perder eventos.
6. Modificacion de un byte: rechazo por SHA y recuperacion de LKG; alerta de integridad.
7. Google Drive desconectado / sincronizacion tardia: journal local sigue valido; reconciliar tras conexion sin duplicar ni sobrescribir.
8. STOP antes, durante y despues del checkpoint: parar en frontera segura, guardando ultimo estado confirmado.
9. Ejecutor con SUCCEEDED: nunca replay; timeout/UNKNOWN: consultar lease, journal y recibos.
10. Restauracion real a una ubicacion de ensayo: restaurar bytes, verificar hashes y ejecutar prueba minima; registrar recibo de RESTORE_POINT distinto del checkpoint.
11. Reanudar conversacion nueva con indice vigente, reconstruir por que/que/como/que falta, referencia a origen y estado vivo, sin usar el estado obsoleto R0.2 como vigente de AUTOFABRICADOR.
12. Demostrar readback real en Google Drive y permisos de acceso; no declarar E2E PASS solo por archivos locales o hashes registrados.

Salida de la prueba: informe por criterio con PASS/FAILED/BLOCKED, recibo original, actor, fecha, hash, enlace al journal y NEXT_ACTION. Sin estas pruebas, CONTRATO DISEÑADO y SISTEMA NO OPERATIVO.
