# AGENTS.md — TCSA instrucciones para agentes
Antes de trabajar, cargar [INSTRUCCIONES-MAESTRAS.md](INSTRUCCIONES-MAESTRAS.md), verificar [MANIFEST-INSTRUCCIONES.json](MANIFEST-INSTRUCCIONES.json) SHA-256 `665e64410bb65dadd91f7d18e3adbb70deddd04c126df173e9c28285135ee982` (v1.3.0) y aplicar sus restricciones.

TCSA es infraestructura de continuidad, no ejecutor de producción. GitHub es público: no subir datos privados, secretos, transcripciones ni históricos. Continuidad privada en TCSA3000 (MCP `tcsa3000`; Drive es su espejo) y estado vivo del ejecutor original solo por conectores autorizados. Proyectos, conversaciones y operaciones mantienen IDs independientes. Sin acceso al maestro o a los datos, declarar límites en lugar de inventarlos.

CIERRE R2 proporcional obligatorio: C0 sin escritura; C1 registro breve único (tcsa3000_cierre) y confirmación remota del espejo; C2/C3 solo si el riesgo lo exige. No regenerar todos los checkpoints. Ver [docs/CHECKPOINTS.md](docs/CHECKPOINTS.md).
