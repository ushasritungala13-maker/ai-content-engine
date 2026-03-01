document.getElementById('contentForm').addEventListener('submit', async function(e){
    e.preventDefault();
    
    const data = {
        tone: document.getElementById('tone').value,
        audience: document.getElementById('audience').value,
        length: document.getElementById('length').value,
        keywords: document.getElementById('keywords').value,
        contentType: document.getElementById('contentType').value
    };

    const response = await fetch('http://127.0.0.1:5000/generate', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    });

    const result = await response.json();
    document.getElementById('output').innerText = result.content;
});