document.querySelectorAll(".btn-añadir-pat").forEach((item) => {
  item.addEventListener("click", addPatV2);
});

document.querySelectorAll(".lista-pat").forEach((item) => {
  item.addEventListener("click", eliminarPat);
});

function addPatV2(e) {
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
  li.classList = "li-pat";
  li.innerHTML =
    patSelection + '<a href="#" class="btn btn-rojo btn-eliminar-pat">x</a>';

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

function eliminarPat(e) {
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
