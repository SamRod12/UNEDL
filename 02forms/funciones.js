function validarDatosGET(){
    var verificar = true;
    if (!document.frmUsrdataGet.txtNombre.value){
        alert("El campo Nombre es requerido.");
        document.frmUsrdataGet.txtNombre.focus();
        verificar = false;
    }
    else if(!document.frmUsrdataGet.txtEmail.value){
        alert("El campo Email es requerido.");
        document.frmUsrdataGet.txtEmail.focus();
        verificar = false;
    }
    else if(!document.frmUsrdataGet.rdGenero[0].checked && !document.frmUsrdataGet.rdGenero[1].checked  && !document.frmUsrdataGet.rdGenero[2].checked){
        alert("El campo Genero es requerido.");
        document.frmUsrdataGet.rdGenero[0].focus();
        verificar = false;
    }

    if(verificar){
        document.frmUsrdataGet.submit();
    }
    else{
        event.preventDefault();
    }
}

function validarDatosPOST(){
    var verificar = true;
    if (!document.frmUsrdataPost.txtNombre.value){
        alert("El campo Nombre es requerido.");
        document.frmUsrdataPost.txtNombre.focus();
        verificar = false;
    }
    else if(!document.frmUsrdataPost.txtEmail.value){
        alert("El campo Email es requerido.");
        document.frmUsrdataPost.txtEmail.focus();
        verificar = false;
    }
    else if(!document.frmUsrdataPost.rdGenero[0].checked && !document.frmUsrdataPost.rdGenero[1].checked){
        alert("El campo Genero es requerido.");
        document.frmUsrdataPost.rdGenero[0].focus();
        verificar = false;
    }

    if(verificar){
        document.frmUsrdataPost.submit();
    }
    else{
        event.preventDefault();
    }
}

window.onload= function(){
    document.getElementById("enviar_get").onclick = validarDatosGET;
    document.getElementById("enviar_post").onclick = validarDatosPOST;
}
