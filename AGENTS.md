# AGENTS.md — TCSA instrucciones para agentes
Antes de trabajar, cargar [INSTRUCCIONES-MAESTRAS.md](INSTRUCCIONES-MAESTRAS.md), verificar [MANIFEST-INSTRUCCIONES.json](MANIFEST-INSTRUCCIONES.json) SHA-256 `8e475f11b01ba2c3bbd6e5fbe0fdaf7dcbb2f996cb5991809140079d1743a591` y aplicar sus restricciones.

TCSA es infraestructura de continuidad, no ejecutor de producción. GitHub es público: no subir datos privados, secretos, transcripciones ni históricos. Drive privado y estado vivo del ejecutor original solo por conectores autorizados. Proyectos, conversaciones y operaciones mantienen IDs independientes. Sin acceso al maestro o a los datos, declarar límites en lugar de inventarlos.

CIERRE R2 proporcional obligatorio: C0 sin escritura; C1 registro breve único y confirmación Drive; C2/C3 solo si el riesgo lo exige. No regenerar todos los checkpoints. Ver [docs/CHECKPOINTS.md](docs/CHECKPOINTS.md).
