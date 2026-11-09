# TCSA — continuidad y conocimiento multiproyecto

TCSA es un sistema independiente para registrar proyectos, conversaciones, ejecuciones, checkpoints, decisiones, LISTA y DESCUBRIMIENTOS. La continuidad privada reside en TCSA3000 (programa MCP portátil, https://github.com/Laster3000/tcsa3000) y Google Drive es su espejo de respaldo; este repositorio publico contiene solo contratos y herramientas publicables.

**Estado:** bootstrap y migracion en curso. No se certifica aun reanudacion E2E ni automatizacion universal. No publicar checkpoints privados, credenciales ni transcripciones.

La fuente de verdad de un estado vivo siempre se reconcilia con journal, lease y recibos del ejecutor original. Un checkpoint documental no equivale a un punto de restauracion de bytes.

## Inicio de ChatGPT y Claude

**Punto de entrada universal:** [INSTRUCCIONES-MAESTRAS.md](INSTRUCCIONES-MAESTRAS.md), con SHA-256 fijado en [MANIFEST-INSTRUCCIONES.json](MANIFEST-INSTRUCCIONES.json).

- ChatGPT Projects y Claude.ai Projects: copiar [el bootstrap breve](docs/BOOTSTRAP-CHATGPT-CLAUDE-R6.txt) a sus instrucciones y dar acceso al maestro por GitHub/Drive o adjuntarlo como conocimiento.
- Claude Code en este repositorio: [CLAUDE.md](CLAUDE.md) carga como referencia el maestro y su manifiesto.
- Otros agentes compatibles: [AGENTS.md](AGENTS.md).
- [Guía de activación](docs/COMO-ACTIVAR-CHATGPT-CLAUDE.md) y [validador local](tools/verify_master.py).

**Importante:** las rutas/URL no conceden acceso automáticamente; la lectura real y su verificación deben realizarse con herramientas disponibles. La continuidad privada no está publicada aquí.

## Cierre ligero R2
Los cambios rutinarios generan **un solo cierre C1** y una comprobación remota de Drive, no una reconstrucción documental completa. Consultas C0 no escriben; cambios importantes C2 y protegidos C3 aumentan controles. Ver [protocolo](docs/CHECKPOINTS.md) y [asistente determinista C1](tools/cierre_ligero.py) (su copia en unidad sincronizada requiere lectura API adicional; no activa un servicio autónomo).

## Política prioritaria
La IA web debe intervenir lo mínimo necesario para aportar experiencia; trabajo rutinario determinista o local. [Política P0 de eficiencia](docs/ECONOMIA-IA-P0.md). La LISTA antigua está separada de la LISTA actual y se consulta exclusivamente como historia. La migración de todo material útil aún requiere conciliación.
