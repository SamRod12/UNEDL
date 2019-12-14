<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>PHP con HTML</title>
        <meta name="description" content="Ejemplo de archivo PHP con HTML">

    </head>
    <body>
        <?php
            function pintartitulo($texto){
                $titulo = "<h3>" . $texto . "</h3>";
                return $titulo;
            }
        ?>
        <div id="wrapper">
            <div id=cotainer>
                <div id="colizq">
                    <?php
                       echo pintartitulo("esta es la columna izquierda con php.");
                    ?>
                    <h4>titulo fuera de php</h4>
                </div>
                <div class="clearer"></div>
            </div>
            <div id="footer">
                footer
            </div>
        </div>
    </body>
</html>