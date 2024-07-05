"""Labels: This is the module where all the static text live"""

header = {
    "title": "Thoth",
    "subtitle": "Group 5",
}

introduction = {
    "title": "Introducción",
    "naming":
        "Thoth es el dios de la sabiduría, la ciencia, la magia y las artes,\
        entre otros vínculos que tiene (por ejemplo, con la luna).",
    "explanation_i":
        "Elegimos este nombre porque en el camino de exploración y\
        prueba y error, incorporamos sabiduría a través de la ",
    "explanation_ii":
        " y el conocimiento de los demás.",
    "usage_i": 
        "Este proyecto funciona como rolling-documentación, \
        donde registramos las cosas que vamos agregando y experimentando."
}

branching = {
    "title": "Branching",
    "content_i":
        "Tomamos la decisión de hacer un modelo de branching con tres ramas: \
        una de desarrollo (develop), una de QA (staging) y otra de producción \
        (main) en base al caso de ser un equipo pequeño pero multidisciplinario.",
    "content_ii":
        "Extendimos el modelo mencionado (basado en GitLab Flow) \
        mediante branches para casos específicos teniendo como base GitFlow. \
        De esta forma podemos utilizar ramas como feature para el desarrollo \
        de nuevas caracteristicas, fix y hotfix para correciones rapidas y tags \
        para controlar las versiones del codigo",
    "content_iii":
        "Para el modelo de branching, utilizamos un derivado de Conventional Commits \
        que se puede resumir en los siguientes tipos:",
    "list_i": [
        "fix: arregla errores que impiden el correcto funcionamiento de una feature",
        "feat: agrega funcionalidades parciales o completas",
        "chore: modifica código relacionado con dependencias, paquetes y/o \
            configuraciones del proyecto",
        "docs: modifica archivos de documentación o archivos de código \
            que requieran documentación",
        "refactor: modifica gran parte de features o todas, o la estructura, \
            tecnologías o ambas del proyecto",
        "style: modifica el formateo del código"
    ],
}

commits = {
    "title": "Commits",
    "content_i": 
        "Los commits son parte vital del flujo de trabajo de un proyecto ya que nos \
        dan contexto, historial y puntos de referencia para poder entender \
        donde podrían haber conflictos, donde una nueva funcionalidad fue integrada \
        y más.",
    "content_ii":
        "Por ello, decidimos usar como referencia principal la metodología de \
        Conventional Commits, que nos brinda una forma normalizada de escribir \
        mensajes con contexto y tipos. La configuración utilizada es la misma \
        que utilizamos en el modelo de branching.",    
    "content_iii":
        "Otra cosa a tener en cuenta es el tono en el que escribimos los mensajes. \
        Para ello usamos el modo imperativo que nos ayuda a remarcar la acción \
        que estamos solicitando en la merge request (MR). Acá dejamos unos \
        unos ejemplos:",
    "list_i": [
        "feat: add new container for the Branching information",
        "fix: update app setup in README.md",
        "chore: remove unused packages",
    ],

}

analysis = {
    "title": "Análisis de Código",
    "content_i":
        "En esta ocasión decidimos implementar un linter y un formateador \
        para incluir tareas en el stage de test del pipeline y así normalizar \
        el estilo del código.",
    "content_ii": 
        "Para el linter decidimos usar pylint que sigue la convención PEP 8. \
        Luego, para formatear parte de ese código, utilizamos Black que está \
        basado en autopep8 (que sigue la convencieon PEP 8) con la diferencia de \
        que es más opinionado, lo cual facilita el convention over configuration.",
    "image_i": "/analysis_i.png"
}

code_review = {
    "title": "Code Review",
    "content_i": "Para que el código tenga una validación manual y con criterio, \
        implementamos un proceso de Code Review para nuestras MR (Merge Requests).",
    "content_ii": "Entre los puntos clave del manejo de MRs y code review, \
        podemos mencionar los siguientes:",
    "list_i": [
        "Inclusión de un MR Template para homogenizar la estructura de las mismas",
        "Al menos un approval de un peer",
        "Inclusión de pipelines de análisis de código y build de la aplicación",
        "Uso de thread para mejor organización de los cambios requeridos",
    ],
    "link_i": {
      "text": "Ejemplo de Merge Request",
      "url": "https://gitlab.com/marcomaza92/thoth/-/merge_requests/2",
    }
}

ci_cd = {
  "title": "CI/CD",
  "content_i":
    "En la etapa de CI/CD apuntamos a hacer un flujo simple pero \
    completo, o al menos que cubra de manera ilustrativa los 3 stages más comunes, \
    los cuales son:",
  "list_i": [
    "test",
    "build",
    "deploy"
  ],
  "content_ii": "Podemos ver esto reflejado en el archivo yaml:",
  "image_i": "/ci_cd_i.png",
  "content_iii":
    "Con esto presente, en cada stage pusimos a correr ciertas tareas \
    para cada job. Podemos resumirlas de la siguiente forma:",
"list_ii": [
  "test: ejecutamos el formatter y luego el linter",
  "build: corremos un comando para obtener artifacts estáticos para deployear",
  "deploy: usando GitLab Pages, exponemos los artifacts para que sean visibles \
    de manera pública a través de una URL"
],
"image_ii": "/ci_cd_ii.png",
}

next_steps = {
  "title": "Más información",
  "content_i":
    "Interesado por saber más y ver cómo se va desarrollando las metodologías y \
    decisiones tomadas?. Acá te dejamos el repositorio para que puedas seguir \
    las actualizaciones más de cerca y con más detalle y ejemplos.",
  "link_i": {
      "text": "Repositorio",
      "url": "https://gitlab.com/marcomaza92/thoth",
    }
}
