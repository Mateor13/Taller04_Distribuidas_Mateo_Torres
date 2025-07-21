# Taller MapReduce - Análisis de Registros de Usuario

## **Nombre:** Mateo Aldair Torres Lara

Este proyecto implementa un algoritmo MapReduce para analizar registros de usuarios y contar aquellos que se registraron fuera del horario laboral (antes de las 8:00 AM o después de las 6:00 PM).

## Formato de Datos de Entrada

Los archivos deben contener líneas con el siguiente formato:
```
YYYY-MM-DD HH:MM:SS usuario:nombre_usuario
```

Ejemplo:
```
2025-07-20 07:15:02 usuario:ana
2025-07-20 18:30:10 usuario:daniel
2025-07-20 22:15:00 usuario:ana
```
## Lógica del Algoritmo

### Mapper (mapper.py)

1. **Parseo**: Extrae fecha, hora y usuario de cada línea
2. **Filtrado**: Solo procesa registros antes de 8:00 AM o después de 6:00 PM
3. **Agrupación**: Agrupa por usuario usando `Counter`
4. **Salida**: Genera archivo `.out` con formato `usuario count [timestamps]`

### Reducer (reducer.py)

1. **Lectura**: Procesa todos los archivos `.out` del directorio `splits/`
2. **Consolidación**: Combina resultados de múltiples mappers
3. **Deduplicación**: Elimina timestamps duplicados por usuario
4. **Salida**: Genera `reporte.txt` con el resumen final

## Ejemplo de Salida

```
ana 2 [2025-07-20_07:15:02,2025-07-20_22:15:00]
daniel 1 [2025-07-20_18:30:10]
```

Formato: `usuario numero_de_registros [lista_de_fechas_horas]`
