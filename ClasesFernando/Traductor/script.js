function getTranslation() {
    let texto = document.formulario.texto.value;
    let entrada = document.formulario.entrada.value;
    let salida = document.formulario.salida.value;
    fetch(`http://127.0.0.1:5000/${entrada}/${salida}/${texto}`)
    .then(data => data.text())
    .then(data => showTranslation(data))
}

function showTranslation(data) {
    if (!data) {
        Swal.fire({
            icon: 'warning',
            title: 'Error',
            text: 'Texto no válido'
        });
    }
    else document.getElementById("traduccion").innerHTML += `<b>Traducción:</b> ${data}<br>`;
}

function validate() {
    let form = document.formulario;
    form.addEventListener('submit', event => {
        if (form.checkValidity()) getTranslation();
        event.preventDefault();
        event.stopPropagation();
        form.classList.add('was-validated');
    }, false);
};

validate()