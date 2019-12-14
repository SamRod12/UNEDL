<!DOCTYPE html>
<html>
    <head>
        <title>Resultado de Formulario</title>
    </head>
    <body>

        <div id="wrapper">
        <h1>Resultado de Formulario</h1>

            <div id="container">
                <?php
                    $btn =""; $nombre="";$email="";
                    if(isset($_GET["btnEnviar"])){
                        $btn = $_GET["btnEnviar"];
                        $nombre=$_GET["txtNombre"];
                        $email=$_GET["txtEmail"];
                    }

                    if(isset($_POST["btnEnviar"])){
                        $btn = $_POST["btnEnviar"];
                        $nombre=$_POST["txtNombre"];
                        $email=$_POST["txtEmail"];
                    }

                    if($btn =='Enviar Get' || $btn == 'Enviar Post'){
                        if( !empty($nombre)){
                            echo '<p>Hola '. htmlspecialchars($nombre) . "!!!!</p>";
                        }else{
                            echo '<p><strong> No escribiste tu nombre!!!!! </strong></p>';
                        }
                    
                ?>
             <br><br>
             <p>Tu correo es: 
                 <?php
                 echo htmlspecialchars($email);
                 ?>
             </p>
             <br><br>
             <?php
                echo '<p> Presionaste el boton: <strong>'. htmlspecialchars($btn).'</strong></p>';
             ?>
            <br><br>
            <?php
                }else{
                    echo "<p>btnEnviar (GET) no fue definido </p><br>";
                    echo '<p>Presionaste el boton: <strong>Cancelar</strong></p>'; 
                }
            ?>
            <hr>
            <p style="font-famili:Arial,Helvetica,sans-serif; font-size:1.5em;">
                <a href="index.php"> Regresar a captura de datos.</a>
            </p>

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