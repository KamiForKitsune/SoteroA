document.querySelector(".btn-fam").addEventListener("click", addPatFam);
document
  .querySelector(".lista-pat-familiar")
  .addEventListener("click", eliminarPat);

function addPatFam(e) {
  const listaPatologias = document.querySelector(".lista-pat-familiar");
  const patologiasFamiliares = document.querySelector("#patoFam");
  const patSelection =
    patologiasFamiliares.options[patologiasFamiliares.selectedIndex].value;

  const li = document.createElement("li");
  li.classList = "li-pat-familiar";
  li.innerHTML = patSelection + '<a href="#" class="btn eliminar-pat">x</a>';

  let patExiste = 0;

  if (Array.from(listaPatologias.children).length > 0) {
    for (let pat of Array.from(listaPatologias.children)) {
      if (pat.childNodes[0].nodeValue === patSelection) {
        patExiste = 1;
      }
    }
  }

  if (patSelection != "Ninguna" && patExiste === 0) {
    listaPatologias.appendChild(li);
  }

  e.preventDefault();
}

function eliminarPat(e) {
  if (Array.from(e.target.classList).includes("eliminar-pat")) {
    e.target.parentElement.remove();
  }

  e.preventDefault();
}
