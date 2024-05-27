<?php

// Verifica se a requisição é do tipo POST
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Obtém os dados enviados no corpo da requisição POST
    $data = json_decode(file_get_contents('php://input'), true);
    
    // Aqui você pode processar os dados de acordo com a sua necessidade
    
    // Retorna os dados recebidos como resposta
    header('Content-Type: application/json');
    echo json_encode($data);
} else {
    // Se não for uma requisição POST, retorna um erro
    http_response_code(405);
    echo json_encode(array('error' => 'Método não permitido'));
}

?>
