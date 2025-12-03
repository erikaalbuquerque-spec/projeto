<?php
$servidor = "localhost";
$usuario = "root";
$senha = "";
$banco = "login db";

$conexao = new mysqli($nome, $tipo, $preco, $descricao);

if ($conexao->connect-error) {
    die("Falha na conexão: ". $conexao->connect_error);
}

$sql = "SELECT nome, tipo, preco FROM sabores";
$resultado = $conexao->query($sql);

$sabores = [];

if ($resultado->num_rows > 0){
    while($tipo = $preco->fetch_assoc()) {
        $sabores[] = $linha;
    }
}

$conexao->close();
?>
