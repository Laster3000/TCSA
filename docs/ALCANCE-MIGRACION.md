# Migration scope / Estado verificable (2026-11-09)
## Covered in private workspace (not in this repository)
- AUTOFABRICADOR continuity source inventory: 2,354 files, SHA-256 for each archived file, 21.3 MB ZIP; CRC PASS, per-file SHA PASS, R92 checkpoint restored successfully in an isolated test folder.
- Source + small operation metadata: 1,906 files, SHA-256 verification; 1.77 MB private ZIP; generated binary-heavy folders are referenced via an additional path/size catalog, not copied.
- Historic records: 47,896 legacy file paths cataloged with metadata; 181 LISTA documents/files archived and CRC checked, WITHOUT granting legacy instructions any operational authority. Full historical binary content remains at original and backup locations and is NOT fully duplicated.
- Four projects indexed. A snapshot is not LIVE executor state. Conversation transcript completeness has not been independently proven.
## Publicly committed
- Project instruction text, checkpoint policy, catalog, MENU concept, LISTA/DESCUBRIMIENTOS descriptions and Python CLI with tests.
## Still missing for universal PASS
- Fresh-state check of original executors, session transcript coverage, real cross-chat readback, conflict tests across multiple machines, full encrypted historical storage, sustained Drive offline/online reconciliation and physical device acceptance.
- No protected service, host installation or source-system deletion was performed.

## Revisión selectiva, economía de IA y LISTA histórica (2026-11-09)
- Auditoría local clasificada por ruta/tamaño: 47.081 rutas de AUTOFABRICADOR. Esto **NO** demuestra cobertura semántica de todo lo útil ni convierte los archivos grandes en basura borrable.
- Además de 2.354 archivos de continuidad y 1.906 fuentes/operaciones ya archivados, se curaron **299 recibos y registros históricos de ejecución** de supervisor y repoexports en un archivo privado de 159.149 bytes, con ZIP CRC y SHA de cada objeto PASS. Se ensayó extracción de dos registros con SHA correcto; **no** es restauración de un supervisor vivo.
- Binarios generados, dependencias, paquetes grandes, modelos y temporales **no se migran por inercia**. Las fuentes faltantes se clasifican antes de preservar o descartar; el origen sigue intacto.
- LISTA histórica: reubicada bajo `09-HISTORICO/LISTA-ANTIGUA-MMC`, acceso únicamente bajo consulta histórica expresa. No participa en `07-LISTA`, ni en prioridades, propuestas o estados de AUTOFABRICADOR.
- Norma P0: [Política de economía IA web](ECONOMIA-IA-P0.md). Herramientas deterministas e IA local probada realizan trabajo recurrente; la IA web aporta arquitectura, diagnóstico difícil y revisión. `tools/route_work.py` es un **router asesor sin llamadas de red ni integración autónoma al ejecutor**.
- 12 pruebas unitarias PASS (7 del router y 5 de checkpoints). No se ha medido ahorro real ni realizado E2E con un modelo local ejecutando trabajos autónomos completos en esta revisión.
