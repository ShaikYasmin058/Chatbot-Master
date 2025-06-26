function sendMessage() {
  const input = document.getElementById("user-input");
  const chatBox = document.getElementById("chat-box");
  const message = input.value.trim();

  if (!message) return;

  chatBox.innerHTML += `<div class="user"><b>You:</b> ${message}</div>`;
  input.value = "";

  fetch("/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: message })
  })
    .then(res => res.json())
    .then(data => {
      chatBox.innerHTML += `<div class="bot"><b>Bot:</b> ${data.reply}</div>`;
      chatBox.scrollTop = chatBox.scrollHeight;
    });
}
