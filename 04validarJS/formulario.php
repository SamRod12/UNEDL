<!DOCTYPE html>
<html lang="es">
<head>
	<meta charset="utf-8">
	<title>Validación de Formularios</title>
	<script>
		function validarDatosGET() {
			//alert("Si entro a la funcion.");
			var verificar = true;		
			if(!document.frmUsrdataGet.txtNombre.value) {
				alert("El campo nombre es requerido.");
				document.frmUsrdataGet.txtNombre.focus();
				verificar = false;
			} else if(!document.frmUsrdataGet.txtPassword.value){
				alert("El campo password es requerido.");
				document.frmUsrdataGet.txtPassword.focus();
				verificar = false;
			} else if( !document.frmUsrdataGet.rdGenero[0].checked && 
					   !document.frmUsrdataGet.rdGenero[1].checked   ) 
					   {
				alert("El campo Genero es requerido.");
				document.frmUsrdataGet.rdGenero[0].focus();
				verificar = false;
			}
			
			if(verificar) {
				document.frmUsrdataGet.submit();
			}
		} // FIN de function validarDatosGET

		function validarDatosPOST() {
			//alert("Si entro a la funcion.");
			var verificar = true;			
			if(!document.frmUsrdataPost.txtNombre.value) {
				alert("El campo nombre es requerido.");
				document.frmUsrdataPost.txtNombre.focus();
				verificar = false;
			} else if(!document.frmUsrdataPost.txtPassword.value)  {
				alert("El campo password es requerido.");
				document.frmUsrdataPost.txtPassword.focus();
				verificar = false;
			} else if( !document.frmUsrdataPost.rdGenero[0].checked && 
					   !document.frmUsrdataPost.rdGenero[1].checked ){
				alert("El campo Genero es requerido.");
				document.frmUsrdataPost.rdGenero[0].focus();
				verificar = false;
			}
			
			if(verificar) {
				document.frmUsrdataPost.submit();
			}
		} // FIN de function validarDatosPOST

		
// Forma SUGERIDA para Asignar el evento onload
// Asignar función al evento onload del html
		window.onload =  function(){
document.getElementById("enviar_get").onclick = validarDatosGET;
document.getElementById("enviar_post").onclick = validarDatosPOST;
		}
	</script>
	<style>
		#error{
			color: #F00;
		}
		
		#ok{
			color: #3FB;
		}
		</style>
</head>

<body>
	<div id="wrapper">
	<?php
	
		error_reporting(E_ALL ^ E_NOTICE);
		if($_GET["error"] == "si"){
			echo "<span id = \"error\"> Ocurrio un problema. Verifica tus datos. </span}>";
		}
		else{
			echo "<span id = \"ok\"> Captura tus datos para ingresar. </span}>";
		}

	?>
		<br/> <br/>

		<header>
			<h1>04 Validación de Formularios - GET</h1>
		</header>

		<div id="container">
			
			<form name="frmUsrdataGet" action="validar.php" 
			method="get" 
			enctype="application/x-www-form-urlencoded">
			
			<label name="lblNombre">Nombre: </label>
			<input type="text" name="txtNombre" value="" />
			<br /><br />
			<label name="lblPwd">Password: </label>
			<input type="password" name="txtPassword" value="" />
			<br /><br />
			<input type="hidden" name="hdnEnviar" value="get" />
			<br /><br />
			<input type="radio" name="rdGenero" value="F" />
				Femenino&nbsp;
			<input type="radio" name="rdGenero" value="M" />
				Masculino&nbsp;
			<br /><br />
			<input type="button" id="enviar_get" name="btnEnviar" 
			    value="Enviar" />  
			<!--<input type="button" id="enviar_get" name="btnEnviar" 
			    value="Enviar" onclick="validarDatosGET();" />  
			1er forma de asignacion de un evento--> 
			</form>
			
<!-- COPIAR FORMULARIO y crear uno para POST -->


			<h1>04 Validación de Formularios - POST</h1>
			
			<form name="frmUsrdataPost" action="validar.php" method="post" 
			enctype="application/x-www-form-urlencoded">
			
			<label name="lblNombre">Nombre: </label>
			<input type="text" name="txtNombre" value="" />
			<br /><br />
			<label name="lblPwd">Password: </label>
			<input type="password" name="txtPassword" value="" />
			<br /><br />
			<input type="hidden" name="hdnEnviar" value="post" />
			<br /><br />
			<input type="radio" name="rdGenero" value="F" />Femenino&nbsp;
			<input type="radio" name="rdGenero" value="M" />Masculino&nbsp;
			<br /><br />
			<input type="button" id="enviar_post" 
			   name="btnEnviar" value="Enviar" 
			 onclick="validarDatosPOST();" />
			<!--1er forma de asignacion de un evento--> 
			</form>



		</div>		<!-- FIN div id="container" -->
		
		<footer><p> &copy; Copyright  by Leo	</p></footer>
	</div>	<!-- FIN div id="wrapper" -->
</body>

</html>