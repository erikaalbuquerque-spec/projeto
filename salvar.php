 <?php
$servidor = "localhost";
$usuario = "root";
$senha= "";
$banco = "login db";




$conexao = new mysqli($servidor, $usuario, $senha, $banco);




if($conexao->connect_error) {
die("Falha na conexão:". $conexao->connect_error);
}




$nome = $_POST['nome'];
$email = $_POST['email'];
$senha = $_POST['senha'];




$senha_criptografada = password_hash($senha, PASSWORD_DEFAULT);
$sql = "INSERT INTO usuarios (nome, email, senha) VALUE (?,?,?)";
$stmt = $conexao->prepare($sql);
$stmt->bind_param("sss", $nome, $email, $senha_criptografada);




if($stmt->execute()) {
echo "<h2>Cadastro realizado com sucesso!</h2>";
echo "<p>Nome:" . htmlspecialchars($nome) . "</p>";
echo "<p>Email:" . htmlspecialchars($email) . "</p>";
echo "<P><a href='index2.html'>Voltar ao formulário</a></p>";
} else {
echo "Erro ao cadastrar:". $stmt->error;
}
$stmt->close();
$conexao->close()  ;
?>




