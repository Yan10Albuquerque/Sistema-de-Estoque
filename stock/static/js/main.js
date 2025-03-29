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

    document.getElementById("updateForm").addEventListener("submit", function(event) {
        event.preventDefault();  // Evita o envio imediato
    
        let id = document.getElementById("equipament_id").value;  // Obtém o ID do input
        this.action = `/update/${id}/`; // Atualiza a ação do formulário para incluir o ID na URL
        this.submit();  // Agora envia o formulário com a URL correta
    });

    let link = document.getElementById("updateLink");  // Obtém o elemento <a>
    console.log(link);  // Verifica se o href foi atualizado corretamente
        // Atualiza a ação do formulário para incluir o ID na URL
    if (link) {
        link.href = `/delete/${id}/`;  // Atualiza o href do link
    }

    
    document.getElementById("modalOverlay").style.display = "flex";
}





