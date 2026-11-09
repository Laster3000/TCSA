# TCSA — PROTOCOLO DE CIERRE LIGERO R2
Versión: 2.0 | Fecha: 2026-11-09 | Estado: NORMA VIGENTE DE PROPORCIONALIDAD. La automatización multiplataforma y el CAS distribuido NO están certificados.

## Objetivo
Completar el trabajo y conservar continuidad útil con el menor esfuerzo total. **Un solo cierre por cambio material**, en lugar de rehacer inventarios, descargar todos los recibos o producir tres checkpoints completos por costumbre. Esta norma sustituye los disparadores y los requisitos uniformes de cierre de R1; R1 queda como referencia histórica y para procedimientos de alto riesgo compatibles. No se debilitan las reglas de seguridad, privacidad, journal original, estados UNKNOWN ni autorización protegida.

## Niveles de cierre (elegir el mínimo suficiente)
- **C0 — Consulta:** saludo, búsqueda, explicación, lectura sin cambios, pruebas repetidas sin novedad. **Sin escritura, sin checkpoint nuevo, sin descarga masiva de Drive.** Si el usuario pide GUARDAR, aplicar C1.
- **C1 — Cambio material rutinario (predeterminado):** edición pequeña, nueva decisión, documentación, prueba útil, avance acotado. Escribir **un registro breve** (projectId, revision/operationId, qué/por qué, resultado real, pruebas pertinentes, rutas/IDs de evidencias, bloqueos y NEXT_ACTION), adjuntar **solo archivos cambiados** cuando haya que preservarlos, SHA de esos archivos y un readback local. Sin checkpoint de conversación/ejecutor ni copia integral de journal si no cambiaron. Sin regenerar un manifiesto global ni recorrer todo el catálogo. Sin declarar COMMITTED por el mero hecho de copiar a Drive.
- **C2 — Cambio importante:** arquitectura, release candidato, integración de varias piezas, prueba E2E nueva o fallo relevante. C1 + preimagen recuperable de los archivos afectados, pruebas independientes relevantes, checkpoint de proyecto y manifiesto selectivo. Checkpoint de ejecutor solo si hubo ejecución/estado nuevo; conversación solo si hubo contenido realmente material que no está ya preservado. Verificar al menos el recibo relevante en Drive con API/conector; no descargar todo el archivo.
- **C3 — Operación protegida/crítica:** migración, instalación/servicio/arranque, borrado significativo, credenciales, permisos, datos irreemplazables, retirada de origen o promoción COMMITTED compartida. Mantener planSha, autorización, journal/lease, fencing/CAS donde aplique, preimagen, copia en dominio de fallo independiente, readback y restore ensayado según riesgo. Si no hay CAS seguro, conservar candidato y declarar promoción bloqueada; **nunca simular COMMITTED**.

## Flujo determinista y rápido para C1
1. Confirmar ID de proyecto/operación y última evidencia pertinente. No releer maestro, índice o histórico ya cargados en la conversación sin indicio de cambio. Si hay efecto de ejecución, reconciliar journal/lease original antes de actuar.
2. Comprobar únicamente el cambio y las pruebas necesarias. Referenciar recibos SUCCEEDED existentes; **no reejecutarlos**. Para UNKNOWN, leer recibo/journal original antes de nuevos efectos.
3. Crear una sola nota de cierre y copiar únicamente evidencias nuevas o modificadas. Usar ruta o hash de evidencias antiguas sin duplicar sus bytes. Nunca copiar secretos al GitHub público.
4. Guardar en TCSA Drive privado cuando haya acceso, comprobar una vez el registro/subida **mediante lectura remota real** o metadatos verificables. El montaje sincronizado local por sí solo deja **PENDING_CLOUD_READBACK**. Un único readback suficiente para C1; no volver a descargar todos los archivos ni todas las conversaciones.
5. Registrar estado `SYNC_VERIFIED` cuando exista prueba remota; si falla, `PENDING_SYNC` / `VERIFICACION_PARCIAL`, conservar copia local e ID para reanudar sin duplicar. Mostrar cierre breve con NEXT_ACTION. C1 documental no requiere actualizar puntero COMMITTED.

## Reglas invariantes
- Un checkpoint es documento, no estado LIVE ni RESTORE_POINT. Journal y lease originales prevalecen cuando importan.
- No repetir SUCCEEDED; UNKNOWN exige reconciliación. La IA autora no valida sola su propio producto.
- Conservación del LKG y las identidades separadas. Los registros parciales no son transcript FULL.
- **CAS/lease y prueba de restauración se reservan a promociones compartidas, concurrentes y operaciones que lo requieran**, no a todo cambio rutinario.
- Sin escritura real y lectura verificable, nunca afirmar que Drive quedó sincronizado. Sin prueba, no declarar PASS.
- M1–M6: informar **solo hitos aplicables al alcance**; N/A no equivale a PASS. Cada cierre debe indicar BLOCKED y NEXT_ACTION si corresponden.
- GitHub TCSA es público y privado Drive es privado. Cambios de normas requieren versión, SHA-256, manifiesto, bootstrap y lectura de ambas fuentes; conservan preimagen y edición anterior.

## Automatización y medición
Usar, cuando esté disponible, herramienta determinista `tools/cierre_ligero.py` para generar **un único C1** idempotente y verificar los SHA locales; si copia a la unidad Drive sincronizada, el resultado sigue siendo `PENDING_CLOUD_READBACK` hasta que el conector confirme existencia. No afirmar que los agentes lo hacen automáticamente ni que un watcher está instalado; sin ejecución programada, el operador debe invocarlo en el cierre.
Medir de forma opcional tiempo total y número de llamadas de cierre. Si C1 consume más trabajo documental que la tarea, revisar proceso, no añadir verificación por inercia.

## Reanudación proporcional
Para responder/consultar: leer solo la cápsula y el último resumen fiable. Para ejecutar: leer checkpoint pertinente y journal/lease original, reconciliar UNKNOWN. Para restaurar/proteger: ampliar a originales, hashes, manifiestos y restore de C3. Nunca barrer todo el TCSA por defecto.
