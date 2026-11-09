# TCSA - Protocolo de checkpoints R1 (CANDIDATO, NO IMPLEMENTADO)
Fecha: 2026-11-09. Alcance: AUTOFABRICADOR y proyectos separados. No importa autoridad, procesos ni historicos sistema anterior.

## Principio
El checkpoint es una fotografia estructurada, firmemente vinculada a la evidencia del estado recuperable. No es una transcripcion completa ni un RESTORE_POINT ni la fuente del estado vivo por si solo. El journal original y los recibos prevalecen sobre una instantanea obsoleta. Un checkpoint sin readback y referencias a fuentes verificables es provisional.

## Clases separadas
A) PROJECT_CHECKPOINT: por projectId. Objetivo y por que, decisiones y motivos, alternativas descartadas, arquitectura, requisitos, dependencias, rutas, repos, revision/LKG y candidato, estado M1-M6, trabajo hecho, pruebas, bloqueos, errores, soluciones probadas, NEXT_ACTION y referencias a operaciones y evidencias originales.
B) CONVERSATION_CHECKPOINT: por conversationId nativo, o alias LOCAL explicitamente declarado. Solo mensajes/resultados literalmente accesibles, su procedencia y segmentos SHA; distinguir LITERAL, CITA, RESUMEN, RECONSTRUCCION, UNKNOWN_GAP. Nunca mezclar conversaciones ni prometer FULL sin API.
C) EXECUTOR_CHECKPOINT: por executorId/jobId/operationId, estado de ejecucion, journal offsets, lease y fencing token, intentos, ultimo evento confirmado, recibos y artefactos. No sustituye una lectura EN VIVO del ejecutor original.
D) RECOVERY_POINT: copia real de bytes, manifiesto SHA-256 y procedimiento de restauracion, preservada en almacenamiento de rescate fuera del dominio de fallo, con ensayo de restore y recibo propio. No confundir con los tres checkpoints de estado.
E) GLOBAL_CATALOG_POINTER: indice ligero con ultimo checkpoint COMMITTED por proyecto/conversacion/ejecutor, revisiones y referencias; nunca contiene un resumen unico que reemplace los anteriores.

## Campos minimos comunes
schemaVersion, checkpointId, type, projectId, conversationId si aplica, executorId/jobId si aplica, objectiveId, functionalId si aplica, releaseId, operationId, revisionId, createdAtUtc, sourceRefs, sourceHashesSha256, previousCheckpointId, previousCheckpointSha256, payloadSha256, lineage, snapshotStatus (PREPARING|COMMITTED|SUPERSEDED|INVALID), verifiedAtUtc, writerId, evidenceRefs, unknownGaps, nextAction.

## Protocolo de guardado (a implementar y probar)
1. Capturar segmentos materiales al producirse, con rol, secuencia, origen y SHA, sin inventar contenido no accesible.
2. Leer ultimo COMMITTED; confirmar CAS por version/etag o puntero de generacion esperado y lease valido. Sin CAS no reemplazar el puntero.
3. Escribir nueva instantanea INMUTABLE, manifest + hashes; generar bytes completos antes de cambiar referencias.
4. Releer bytes, recomputar SHA-256 y comprobar schema, enlaces, chain y existencia de referencias.
5. Promocionar el nuevo puntero COMMITTED mediante CAS; si hay conflicto, preservar ambas ramas, reconciliar desde evidencias y reintentar con nueva generacion.
6. Replicar a Drive cuando sincronizacion confirmada; Drive no ofrece mutex ni journal transaccional fiable. La ejecucion viva y colas mantienen journal local durable y recuperable.
7. Conservar ultimo LKG, antecedentes y copia de rescate. No podar historico automaticamente.

## Cuando capturar
Al finalizar un cambio material; decision de arquitectura; trabajo delegado y recibo original; prueba/fracaso y correccion; cambio de fase; STOP, pausa o handoff; cierre; antes/despues de efectos protegidos; riesgo de truncamiento. No usar heartbeats o polling como razon documental por defecto.

## Reanudacion obligatoria
Leer LEEME-PRIMERO -> catalogo -> ultimo PROJECT_CHECKPOINT COMMITTED -> CONVERSATION_CHECKPOINT correcto -> manifest/decision/evidencias -> journal/lease/estado VIVO del ejecutor original -> confrontar contradicciones y UNKNOWN -> NEXT_ACTION. NO repetir SUCCEEDED. Para UNKNOWN, buscar original journal/recibo/readback antes de cualquier replay.

## Normas de seguridad
Checkpoints privados por defecto, cifrado en reposo cuando disponible, sin claves/secretos, rutas con acceso minimo y export publico saneado. No importar ni atribuir autoridad del TCSA de sistema anterior. Todo dato historico conserva origen y etiquetas de confianza.
