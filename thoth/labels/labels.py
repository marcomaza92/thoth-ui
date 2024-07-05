"""Labels: This is the module where all the static text live"""

header = {
    "title": "Thoth",
    "subtitle": "Group 5",
}

introduction = {
    "title": "Introducción",
    "naming": "Thoth es el dios de la sabiduría, la ciencia, la magia y las artes,\
    entre otros vínculos que tiene (por ejemplo, con la luna)",
    "explanation_i": "Elegimos este nombre porque en el camino de exploración y\
    prueba y error, incorporamos sabiduría a través de la ",
    "explanation_ii": " y el conocimiento de los demás",
}

branching = {
    "title": "Branching",
    "content_i": "Tomamos la decisión de hacer un Branching con dos ramas: una de \
    desarrollo (Develop) y otra de producción (Main) debido a que \
    planteamos el caso en el que fuéramos desarrolladores de un equipo \
    para una empresa chica. Entonces, nos pareció la mejor idea usar dos \
    entornos de trabajo para reducir costos y porque veíamos que era \
    innecesario que fuera más complejo. Decidimos combinar GitFlow y \
    GitLab Flow por las siguientes razones: poder separar en ramas de \
    Desarrollo y Produccion, y ademas nos da la opcion de poder utilizar \
    otras ramas como Feature para el desarrollo de nuevas caracteristicas, \
    Release y Hotfix para correciones rapidas y controlar las versiones del codigo, \
    ya que el uso de ramas dedicadas nos da un historial mas organizado.",
    "content_ii": "Y para realizar los commits de las Branches decidimos utilizar \
    Conventional Commits para mejorar la automatizacion y claridad \
    debido a que utiliza distintios tipos como:",
    "list_i": [
        "Feat= agrega funcionalidades parciales o completas",
        "Fix= arregla errores que impiden el correcto funcionamiento de una feature",
        "Docs= modifica archivos de documentación o archivos de código \
    que requieran documentación",
    ],
}

commits = {
    "title": "Commits",
    "content_i": "Conventional Commit",
    "list_i": [
        "scope: message",
        "feat: add new container for the Branching information",
        "fix: update app setup in README.md",
        "chore: remove unused packages",
    ],
}

analysis = {
    "title": "Análisis de Código",
    "content_i": "En esta ocasión decidimos implementar un linter y un formateador \
    para incluir tareas en el stage de test del pipeline y así normalizar \
    el estilo del código.",
    "content_ii": "Para el linter decidimos usar pylint que sigue la convención PEP 8. \
    Luego, para formatear parte de ese código, utilizamos Black que está \
    basado en autopep8 (que sigue la convencieon PEP 8) con la diferencia que \
    es más opinionado, lo cual facilita el convention over configuration.",
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
        "Inclusión de pipelines de análisis de código y build de la aplicación"
        "Uso de thread para mejor organización de los cambios requeridos",
    ],
    "link_i": "https://gitlab.com/marcomaza92/thoth/-/merge_requests/2",
}

ci_cd = {
  "title": "CI/CD",
  "content_i":
    "En la etapa de CI/CD, tratamos de hacer un flujo simple pero \
    completo, o al menos que cubra de manera ilustrativa los 3 stages más comunes \
    que son:",
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
