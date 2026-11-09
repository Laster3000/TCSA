# AGENTS.md — TCSA instrucciones para agentes
Antes de trabajar, cargar [INSTRUCCIONES-MAESTRAS.md](INSTRUCCIONES-MAESTRAS.md), verificar [MANIFEST-INSTRUCCIONES.json](MANIFEST-INSTRUCCIONES.json) SHA-256 `452fe9aac6aec89a43593fe90002985f7fde522563a7b8f89ca1897b1966ea84` (v1.4.0) y aplicar sus restricciones.

TCSA es infraestructura de continuidad, no ejecutor de producción. GitHub es público: no subir datos privados, secretos, transcripciones ni históricos. Continuidad privada en TCSA3000 (MCP `tcsa3000`; respaldos: GitHub privado y Drive) y estado vivo del ejecutor original solo por conectores autorizados. Proyectos, conversaciones y operaciones mantienen IDs independientes. Sin acceso al maestro o a los datos, declarar límites en lugar de inventarlos.

CIERRE R2 proporcional obligatorio: C0 sin escritura; C1 registro breve único (tcsa3000_cierre) y confirmación remota del espejo; C2/C3 solo si el riesgo lo exige. No regenerar todos los checkpoints. Ver [docs/CHECKPOINTS.md](docs/CHECKPOINTS.md).
