function showModal() {
    document.getElementById('modal').style.display = 'flex';
}

function closeModal() {
    document.getElementById('modal').style.display = 'none';
    document.getElementById('modalOverlay').style.display = 'none';
}

function openModal(id, name, description, stock, price) {
    document.getElementById("equipament_id").value = id;
    document.getElementById("name").value = name;
    document.getElementById("description").value = description;
    document.getElementById("stock").value = stock;
    document.getElementById("price").value = price;
    
    console.log(document.getElementById("updateForm").action);

    document.getElementById("updateForm").addEventListener("submit", function(event) {
        event.preventDefault();  // Evita o envio imediato
    
        let id = document.getElementById("equipament_id").value;  // Obtém o ID do input
        // Atualiza a ação do formulário para incluir o ID na URL
        this.action = `/update/${id}/`;
    
        this.submit();  // Agora envia o formulário com a URL correta
    });

    console.log(document.getElementById("updateForm").action);
    document.getElementById("modalOverlay").style.display = "flex";
}



