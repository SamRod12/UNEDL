<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <script src="funciones.js" >
        
        </script>
    </head>
    <body>

        <div id="wrapper">
            <h1>Formularios - envio de datos con get y post</h1>

            <div id="container">
                <h1>Formulario con Get</h1>
                <form name="frmUsrdataGet" action="resultado.php" method="get" enctype="application/x-www-form-urlencoded">
<!--   -->
                <label name="lblNombre">Nombre: </label>
                <input type="text" name="txtNombre" value=""/>
                <br><br>
                <label name="lblEmail">E-mail: </label>
                <input type="text" name="txtEmail" value=""/>
                <br><br>
                <input type="radio" name="rdGenero" value=""/>
                    Femenino&nbsp;
                <input type="radio" name="rdGenero" value=""/>
                    Masculino&nbsp;
                <input type="radio" name="rdGenero" value=""/>
                    No quiere decir&nbsp;
                <br><br>
                <input type="submit" id="enviar_get" name="btnEnviar" value="Enviar Get" />
                </form>

                <h1>Formulario con Post</h1>
                <form name="frmUsrdataPost" action="resultado.php" method="post" enctype="application/x-www-form-urlencoded">
                <label name="lblNombre">Nombre: </label>
                <input type="text" name="txtNombre" value=""/>
                <br><br>
                <label name="lblEmail">E-mail: </label>
                <input type="text" name="txtEmail" value=""/>
                <br><br>
                <input type="radio" name="rdGenero" value="F"/>
                    Femenino&nbsp;
                <input type="radio" name="rdGenero" value="M"/>
                    Masculino&nbsp;
                <br><br>
                <input type="submit" id="enviar_post" name="btnEnviar" value="Enviar Post"  />
                <input type="submit" id="cancelar_post" name="btnCancel" value="Cancelar Post" />
                </form>
            </div>
            <br><br>
            <footer>
                <p>
                    &copy; Copyright by leo
                </p>
            </footer>
        </div>

    </body>
</html>