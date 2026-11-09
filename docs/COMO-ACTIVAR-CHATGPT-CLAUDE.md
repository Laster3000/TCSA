# Cómo activar TCSA en ChatGPT y Claude

## Qué se ha instalado
- Documento maestro público idéntico al de Google Drive: [INSTRUCCIONES-MAESTRAS.md](../INSTRUCCIONES-MAESTRAS.md).
- Manifiesto [MANIFEST-INSTRUCCIONES.json](../MANIFEST-INSTRUCCIONES.json) que fija versión y SHA-256.
- Arranque corto: [BOOTSTRAP-CHATGPT-CLAUDE-R2.txt](BOOTSTRAP-CHATGPT-CLAUDE-R2.txt).
- `CLAUDE.md` para Claude Code dentro de este repositorio.
- `AGENTS.md` para agentes de desarrollo compatibles.
- `tools/verify_master.py` para validar el SHA-256 en una copia local.

## ChatGPT Projects
1. Abrir la configuración de instrucciones del proyecto y sustituir el texto anterior por el contenido de `BOOTSTRAP-CHATGPT-CLAUDE-R2.txt` (Drive: `01-INSTRUCCIONES/COPIAR-INSTRUCCIONES.txt`).
2. Habilitar acceso a GitHub y, para datos privados, a Google Drive cuando las integraciones estén disponibles; alternativamente adjuntar el maestro y los archivos de continuidad autorizados al proyecto.
3. Empezar una conversación nueva y pedir: «Valida el maestro TCSA: indica versión, SHA y si has podido leer el catálogo privado».
4. No asumir que cada turno realiza una descarga nueva sin herramienta de acceso o que las rutas en el prompt son un enlace montado.

## Claude.ai Projects
1. Pegar el mismo bootstrap breve en instrucciones del proyecto de Claude.
2. Añadir el maestro como conocimiento del proyecto o proporcionar acceso a GitHub/Drive mediante las conexiones autorizadas disponibles.
3. Pedir comprobación de versión y lectura de fuentes, igual que en ChatGPT.

## Claude Code
Trabajar desde un checkout de este repositorio. `CLAUDE.md` apunta al maestro y su manifiesto. Verificar versión antes de realizar cambios, y proporcionar conectores adecuados si se necesitan datos privados.

## Prueba local
```bash
python tools/verify_master.py --root .
```
Debe devolver PASS sobre el repositorio cuando contenga el manifiesto y el maestro exactos. Una alteración debe devolver FAILED; una ruta inexistente, BLOCKED.

## Limitaciones
- Ninguna herramienta cambia automáticamente las instrucciones del proyecto ChatGPT o Claude.ai por haber creado estos archivos.
- El repositorio GitHub es público. Los checkpoints completos y datos privados permanecen en Google Drive autorizado; la conexión a Drive no deriva del enlace público.
- La reanudación verdadera de un trabajo exige comprobar el journal, los recibos y el lease del ejecutor original; no basta con leer el maestro o un catálogo.
- El histórico permanece separado y solo aporta conocimiento consultable.
