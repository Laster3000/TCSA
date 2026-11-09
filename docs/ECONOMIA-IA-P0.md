# TCSA — ECONOMÍA DE IA WEB Y EJECUCIÓN LOCAL | POLÍTICA P0
Versión: 1.0.0 | Fecha: 2026-11-09 | Estado: NORMA DE DISEÑO Y ACEPTACIÓN; EL ENRUTAMIENTO AUTOMÁTICO AÚN NO ESTÁ CERTIFICADO.

## Objetivo prioritario
Conservar la aportación experta de ChatGPT/Claude y minimizar las llamadas y el trabajo repetitivo de IA web/remota. La IA web se reserva para arquitectura, problemas inéditos, diagnóstico de fallos persistentes, revisión crítica y decisiones de alto impacto. Los programas deterministas y los agentes locales deben llevar a cabo el trabajo recurrente de exploración, código, pruebas, reparaciones y empaquetado, donde haya capacidad demostrada. Nunca simular que existe una ejecución local o una delegación autónoma que no se ha probado.

## Enrutador por escalones
**L0 — DETERMINISTA:** inventario, SHA, búsqueda, filtrado, clasificación mecánica, builds, tests y verificación de recibos. No solicitar a un modelo lo que puede hacer una herramienta reproducible.
**L1 — IA LOCAL:** especificaciones de baja incertidumbre, edición, corrección guiada por pruebas, refactorización y documentación técnica. Usar capacidades verificadas, modelos locales compatibles, GPU cuando esté disponible y aislamiento verdadero para código generado.
**L2 — IA WEB EXPERTA:** decidir arquitectura y estrategia, revisar requisitos difíciles, desbloquear errores novedosos tras evidencia, evaluar riesgos, diseñar pruebas de aceptación y auditar resultados cuando el valor añadido lo justifique.
**L3 — SEGUNDA REVISIÓN EXTERNA:** solo si una decisión crítica permanece disputada, el riesgo lo exige o el usuario la solicita expresamente. No generar cadenas de opiniones redundantes.

## Reglas obligatorias de ahorro
1. Antes de cada tarea: recuperar decisiones/checkpoint y DESCUBRIMIENTOS por pertinencia; verificar si ya existe una solución o recibo válido. No reejecutar SUCCEEDED.
2. Distinguir tarea ejecutable determinista de tarea creativa o incierta. Subdividir trabajo en unidades verificables y mantener una sola misión clara en el ejecutor.
3. No llamar a IA web dentro de cada microoperación. Consolidar preguntas estratégicas en un informe breve con objetivo, contexto esencial, intentos anteriores, evidencias seleccionadas, opciones y decisión requerida.
4. Ejecutar pruebas unitarias y regresiones locales en lotes con filtros; enviar a experto solo fallos/contradicciones representativos con enlaces SHA a los logs originales, no volcados masivos.
5. Caché por identidad exacta de tarea+entrada SHA+modelo/versión+política+entorno relevante. Un resultado cacheado solo se reutiliza con compatibilidad probada; estados vivos nunca se resuelven por caché.
6. Si dos intentos no aportan nuevo cambio, prueba o evidencia, detener repetición y cambiar de hipótesis o solicitar revisión experta. No bucles infinitos.
7. Los presupuestos de llamadas/tokens deben ser configurables por encargo/proyecto; no inventar precios ni porcentajes. Registrar llamadas web reales, tokens cuando proveedor los indique, latencia, tokens locales disponibles, coste facturado cuando sea accesible, éxitos, bloqueos, ahorros solo si medidos.
8. No remitir información privada a proveedores externos sin alcance y autorización apropiados. Si no hay IA local o canal web permitido, declarar BLOCKED y ofrecer ruta determinista segura.
9. Conservar decisiones expertas en DESCUBRIMIENTOS y checkpoints para que una solución pagada no vuelva a comprarse en otra conversación.
10. Un error operativo determinista se corrige por scripts y tests sin pedir nuevo razonamiento web salvo cuando haya riesgo nuevo, incertidumbre material o ausencia de progreso real.

## Contrato de escalado
La IA local prepara una **cápsula de escalado** con:
- projectId / objectiveId / operationId / entorno y versiones;
- QUÉ se quiere y POR QUÉ, criterios de éxito fijados;
- estado vivo y evidencia con SHA/referencias, no resultados supuestos;
- alternativas/soluciones intentadas y razón exacta del fracaso;
- pregunta(s) que requieren juicio experto, riesgos y opciones;
- límites de confidencialidad, presupuesto y NEXT_ACTION prevista.
Al recibir respuesta, el sistema convierte el razonamiento en decisiones y tareas locales y mide su efectividad. Las respuestas expertas no son por sí solas instalaciones o pruebas aceptadas.

## Modelo de costes y aceptación
La meta es minimizar **esfuerzo/coste total para obtener un resultado correcto**, no maximizar trabajo barato que genera retrabajo. Un agente local lento o incorrecto no es necesariamente más económico.
Métricas mínimas: tareas finalizadas con aceptación independiente, llamadas a IA web por objetivo, tokens reales medidos, tiempo humano y de máquina, reincidencia de fallos, tasa de reutilización de recetas y porcentaje de reanudaciones sin pérdida cuando esté medido. Sin una línea base y observaciones reales, cualquier ahorro es DESCONOCIDO.
Pruebas exigidas: L0 sin llamadas a modelo; L1 con resultados reales y oráculos independientes; escalado L2 por necesidad con una cápsula útil; confidencialidad; errores repetidos; caché sin falsos aciertos; caída/offline; reanudación sin repetir SUCCEEDED.
