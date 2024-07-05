header = {
  "title": "Thoth",
  "subtitle": "Group 5",
}

introduction = {
  "title": "Introducción",
  "naming":
    "Thoth es el dios de la sabiduría, la ciencia, la magia y las artes,\
    entre otros vínculos que tiene (por ejemplo, con la luna)",
  "explanationI":
    "Elegimos este nombre porque en el camino de exploración y\
    prueba y error, incorporamos sabiduría a través de la ",
  "explanationII": " y el conocimiento de los demás"
    
}

branching = {
  "title": "Branching",
  "contentI": 
    "Tomamos la decisión de hacer un Branching con dos ramas: una de \
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
  "contentII":
    "Y para realizar los commits de las Branches decidimos utilizar \
    Conventional Commits para mejorar la automatizacion y claridad \
    debido a que utiliza distintios tipos como:",
  "list": [
    "Feat= agrega funcionalidades parciales o completas",
    "Fix= arregla errores que impiden el correcto funcionamiento de una feature",
    "Docs= modifica archivos de documentación o archivos de código \
    que requieran documentación"
  ]
}

commits = {
  "title": "Commits",
  "contentI": "Conventional Commit",
  "list": [
    "scope: message",
    "feat: add new container for the Branching information",
    "fix: update app setup in README.md",
    "chore: remove unused packages"
  ]
}