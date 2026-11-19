# Ejemplos de Scripts de Carga de Información

## Descripción general

Este directorio contiene scripts demostrativos que sirven como guía para comprender la estructura, lógica y metodología de los procesos de carga de información. Su contenido puede utilizarse como punto de partida para desarrollar nuevos scripts, adaptándolos a los requerimientos específicos de cada proceso.


## Descripción de los scripts

La siguiente tabla presenta los scripts de ejemplo incluidos en este directorio, junto con una breve descripción de su propósito y funcionalidad.

| Script | Descripción |
|---|---|
| `import_content.py` | Ejemplo de carga de información de elemntos de CV. |

> [!TIP]
>  Se recomienda hacer uso de [plone.api](https://6.docs.plone.org/plone.api/content.html) para creacion de contenido.

## Requisitos previos

Antes de ejecutar los scripts, es necesario verificar que:

- Se encuentren instaladas todas las dependencias requeridas.
- El servido SEO esta corriendo.
- Se cuente con los permisos necesarios para realizar las operaciones de carga.

## Ejecución


Ejemplo de ejecución:

```shell
bin/zeoclient_debug run scripts/import_content.py
```

## Consideraciones

- Revisar el contenido de cada script antes de ejecutarlo.
- Verificar que la información de entrada esté disponible y cumpla con el formato esperado.
- Validar los resultados una vez finalizado el proceso de carga.
- Evitar ejecuciones duplicadas, a menos que el proceso esté diseñado para soportarlas.
