function validarCampos() {

    var nombre = document.getElementById("txt-nombre").value;
    var segundonombre = document.getElementById("txt-segundo-nombre").value;
    var apellido = document.getElementById("txt-apellido").value;
    var segundoapellido = document.getElementById("txt-segundo-apellido").value;
    var comuna = document.getElementById("Comuna").value;
    var direccion = document.getElementById("direccion").value;"numero-casa-dept"
    var numerocasadept = document.getElementById("numero-casa-dept").value;
    var telefono = document.getElementById("telefono").value;
    var email = document.getElementById("email").value;

    //VALIDADOR NOMBRE
    if (nombre.trim() == "") {
        document.getElementById("txt-nombre").style.borderColor = "#FE0000";
        document.getElementById("error-nombre").style.visibility = "visible";
        var bandera = true;
    }
    else {
        document.getElementById("error-nombre").style.visibility = "hidden";
        document.getElementById("txt-nombre").style.borderColor = "#C0C0C0";
        var bandera = false;
    }

    //VALIDADOR SEGUNDO NOMBRE
    if (segundonombre.trim() == "") {
        document.getElementById("txt-segundo-nombre").style.borderColor = "#FE0000";
        document.getElementById("error-segundonombre").style.visibility = "visible";
    }
    else {
        document.getElementById("error-segundonombre").style.visibility = "hidden";
        document.getElementById("txt-segundo-nombre").style.borderColor = "#C0C0C0";
    }

    //VALIDADOR APELLIDO
    if (apellido.trim() == "") {
        document.getElementById("txt-apellido").style.borderColor = "#FE0000";
        document.getElementById("error-apellido").style.visibility = "visible";
    }
    else {
        document.getElementById("error-apellido").style.visibility = "hidden";
        document.getElementById("txt-apellido").style.borderColor = "#C0C0C0";
    }
    //VALIDADOR SEGUNDO APELLIDO
    if (segundoapellido.trim() == "") {
        document.getElementById("txt-segundo-apellido").style.borderColor = "#FE0000";
        document.getElementById("error-segundoapellido").style.visibility = "visible";
       
    }
    else {
        document.getElementById("error-segundoapellido").style.visibility = "hidden";
        document.getElementById("txt-segundo-apellido").style.borderColor = "#C0C0C0";
    }
    //VALIDADOR COMUNA
    if (comuna.trim() == "") {
        document.getElementById("Comuna").style.borderColor = "#FE0000";
        document.getElementById("error-comuna").style.visibility = "visible";
    }
    else {
        document.getElementById("error-comuna").style.visibility = "hidden";
        document.getElementById("Comuna").style.borderColor = "#C0C0C0";
    }
    //VALIDADOR DIRECCION
    if (direccion.trim() == "") {
        document.getElementById("direccion").style.borderColor = "#FE0000";
        document.getElementById("error-direccion").style.visibility = "visible";
    }
    else {
        document.getElementById("error-direccion").style.visibility = "hidden";
        document.getElementById("direccion").style.borderColor = "#C0C0C0";
    }
    //VALIDADOR NUMERO
    if (numerocasadept.trim() == "") {
        document.getElementById("numero-casa-dept").style.borderColor = "#FE0000";
        document.getElementById("error-numero").style.visibility = "visible";
    }
    else {
        document.getElementById("error-numero").style.visibility = "hidden";
        document.getElementById("numero-casa-dept").style.borderColor = "#C0C0C0";

    }
    //VALIDADOR TELEFONO
    if (telefono.trim() == "") {
        document.getElementById("telefono").style.borderColor = "#FE0000";
        document.getElementById("error-telefono").style.visibility = "visible";
    }
    else {
        document.getElementById("error-telefono").style.visibility = "hidden";
        document.getElementById("telefono").style.borderColor = "#C0C0C0";
    }
    //VALIDADOR correo
    if (email.trim() == "") {
        document.getElementById("email").style.borderColor = "#FE0000";
        document.getElementById("error-email").style.visibility = "visible";
    }
    else {
        document.getElementById("error-email").style.visibility = "hidden";
        document.getElementById("email").style.borderColor = "#C0C0C0";
    }
        
}