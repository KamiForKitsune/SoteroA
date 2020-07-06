document.querySelectorAll(".btn-añadir-a-lista").forEach((item) => {
  item.addEventListener("click", addLiLista);
});

document
  .querySelector("#ppr")
  .getElementsByTagName("input")[0]
  .addEventListener("click", habilitarSeccOpcionalEmbarazo);

document
  .querySelector("#pter")
  .getElementsByTagName("input")[0]
  .addEventListener("click", habilitarSeccOpcionalEmbarazo);

document
  .querySelector("#cesareas-previas")
  .addEventListener("click", habilitarSeccOpcionalEmbarazo);
document
  .querySelector("#embarazos-gemelares")
  .addEventListener("click", habilitarSeccOpcionalEmbarazo);

function addLiLista(e) {
  // Selecciona la lista de patologias asociada a el boton clickeado
  let listaPatologias = e.target.parentElement.parentElement.getElementsByTagName(
    "ul"
  );
  if (listaPatologias.length > 0) {
    listaPatologias = listaPatologias[0];
  }

  // Selecciona la patologia elegida en el selecotr
  let patologiasFamiliares = e.target.parentElement.getElementsByTagName(
    "select"
  )[0];
  const patSelection =
    patologiasFamiliares.options[patologiasFamiliares.selectedIndex].value;

  // Crea el nuevo elemto 'li'
  const li = document.createElement("li");
  li.classList = "lista-interactiva__lista__li";
  li.innerHTML =
    patSelection + '<a href="#" class="btn btn-rojo btn-eliminar-pat">x</a>';
  li.addEventListener("click", eliminarLiLista);

  // Revisa si una patologia con el mismo nombre ya existe en la lista
  let patExiste = 0;
  if (Array.from(listaPatologias.children).length > 0) {
    for (let pat of Array.from(listaPatologias.children)) {
      if (pat.childNodes[0].nodeValue === patSelection) {
        patExiste = 1;
      }
    }
  }

  // Añade patologia a la lista, solo si aun no esta en ella
  if (patSelection != "Ninguna" && patExiste === 0) {
    listaPatologias.appendChild(li);
  }

  e.preventDefault();
}

function eliminarLiLista(e) {
  if (Array.from(e.target.classList).includes("btn-eliminar-pat")) {
    e.target.parentElement.remove();
  }

  e.preventDefault();
}

function addPatFam(e) {
  // Selecciona la lista de las patologias
  const listaPatologias = document.querySelector(".lista-pat-familiar");

  // Selecciona la patologia elegida en el selecotr
  const patologiasFamiliares = document.querySelector("#patoFam");
  const patSelection =
    patologiasFamiliares.options[patologiasFamiliares.selectedIndex].value;

  // Crea el nuevo elemto 'li'
  const li = document.createElement("li");
  li.classList = "li-pat-familiar";
  li.innerHTML = patSelection + '<a href="#" class="btn eliminar-pat">x</a>';

  // Revisa si una patologia con el mismo nombre ya existe en la lista
  let patExiste = 0;
  if (Array.from(listaPatologias.children).length > 0) {
    for (let pat of Array.from(listaPatologias.children)) {
      if (pat.childNodes[0].nodeValue === patSelection) {
        patExiste = 1;
      }
    }
  }

  // Añade patologia a la lista, solo si aun no esta en ella
  if (patSelection != "Ninguna" && patExiste === 0) {
    listaPatologias.appendChild(li);
  }

  e.preventDefault();
}

function habilitarSeccOpcionalEmbarazo(e) {
  // Inputs que activan la seccion opcional
  const ppr = document.querySelector("#ppr").getElementsByTagName("input")[0];
  const pter = document.querySelector("#pter").getElementsByTagName("input")[0];

  // Seccion opcional
  const seccionOpcional = document.querySelector(
    ".ficha-a__antecedentes-obstetricos__form__item--embarazo-ectopico--seccion-opcional"
  );

  // Seccion causas
  const seccionCausas = document.querySelector(
    ".ficha-a__antecedentes-obstetricos__form__item--embarazo-ectopico--seccion-opcional__causa"
  );

  // Inputs que activan la seccion de causas
  const cesareasPrevias = document.querySelector("#cesareas-previas");
  const embarazosGemelares = document.querySelector("#embarazos-gemelares");

  // Selecciona todos los inputs dentro de la seccion opcional
  let seccionOpcionalInputs = [];
  let seccionOpcionalCausasInputs = [];

  for (const i of seccionOpcional.children) {
    for (const x of i.children) {
      if (x.tagName == "INPUT") {
        seccionOpcionalInputs.push(x);
      }
    }
  }
  for (const i of document.querySelector(
    ".ficha-a__antecedentes-obstetricos__form__item--embarazo-ectopico--seccion-opcional__causa"
  ).children) {
    for (const x of i.children) {
      if (x.tagName == "INPUT") {
        seccionOpcionalCausasInputs.push(x);
      }
    }
  }

  let activarSeccionOpcional;

  if (ppr.checked || pter.checked) {
    activarSeccionOpcional = true;
  } else {
    activarSeccionOpcional = false;
  }

  let activarCausas;

  if (cesareasPrevias.checked || embarazosGemelares.checked) {
    activarCausas = true;
  } else {
    activarCausas = false;
  }

  if (activarSeccionOpcional) {
    for (const i of seccionOpcionalInputs) {
      i.disabled = false;
    }
    if (activarCausas) {
      for (const i of seccionOpcionalCausasInputs) {
        i.disabled = false;
      }
      seccionCausas.classList.remove(
        "ficha-a__antecedentes-obstetricos__form__item--embarazo-ectopico--seccion-opcional--inactive"
      );
    } else {
      for (const i of seccionOpcionalCausasInputs) {
        i.disabled = true;
      }
      seccionCausas.classList.add(
        "ficha-a__antecedentes-obstetricos__form__item--embarazo-ectopico--seccion-opcional--inactive"
      );
    }

    seccionOpcional.classList.remove(
      "ficha-a__antecedentes-obstetricos__form__item--embarazo-ectopico--seccion-opcional--inactive"
    );
  } else {
    seccionOpcional.fontColor;
    for (const i of seccionOpcionalInputs) {
      i.disabled = true;
    }
    for (const i of seccionOpcionalCausasInputs) {
      i.disabled = true;
    }

    seccionOpcional.classList.add(
      "ficha-a__antecedentes-obstetricos__form__item--embarazo-ectopico--seccion-opcional--inactive"
    );
  }
}

function runTimeFunctions() {
  habilitarSeccOpcionalEmbarazo();
}

runTimeFunctions();
