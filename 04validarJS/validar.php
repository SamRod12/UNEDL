<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<title>Validación de Formularios</title>
	</head>

	<body>
		<div id="wrapper">

		
			<h1>Validación de Formularios</h1>

			<div id="container">
			<?php
    $nombre="leo";
	$password="12345";
	
	if(isset($_GET["hdnEnviar"]))
	{
		if($nombre==$_GET["txtNombre"] && $password==$_GET["txtPassword"])
		{
			echo "El nombre que ingresaste por GET es: " . $_GET["txtNombre"]
				. "<br /> y el password es: " . $_GET["txtPassword"] . "."
				. "<br /> El genero seleccionado es : " . $_GET["rdGenero"] . ".";
		}
		else 
		{	
		// Redirigir el flujo de la aplicación
			header("Location: formulario.php?error=si");
		}
	}
	
	if(isset($_POST["hdnEnviar"]))
	{
		if($nombre==$_POST["txtNombre"] && $password==$_POST["txtPassword"])
		{
			echo "El nombre que ingresaste por POST es: " . $_POST["txtNombre"]
				. "<br /> y el password es: " . $_POST["txtPassword"] . "."
				. "<br /> El genero seleccionado es : " . $_POST["rdGenero"] . ".";
		}
		else 
		{
		// Redirigir el flujo de la aplicación
			header("Location: formulario.php?error=si");
		}
	}
?>
			</div>

		</div>
	</body>
</html>
