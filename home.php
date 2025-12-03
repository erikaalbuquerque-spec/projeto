<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width , initial-scale=1.0">
    <title>Lista de Usuários</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<?php
include 'dados.php';
?>

<div class="container">
    <h2>Lista de Usuários Cadastrados</h2>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Nome</th>
                <th>Email</th>
            </tr>
        </thead>
        <tbody>
        <?php
        if (count($usuarios) >0) {
            // Itera sobre o array para exibir os dados na tabela foreach ($usuarios as $usuario) {
            echo "<tr>";
            echo "<td>" . htmlspecialchars($usuario['id']) . "</td>";
            echo "<td>". htmlspecialchars($usuario['nome']) . "</td>";
            echo "<td>". htmlspecialchars($usuario['email']) . "</td>";
            echo "</tr>";
        }
    } else {
        echo "<tr><td colspan='3'>Nenhum usuário encontrado.</td></tr>";
    } ?>
      </tbody>
    </table>
</div>


</body>
</html>