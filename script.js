
const form = document.getElementById('chat-form');
const input = document.getElementById('user-input');
const chatBox = document.getElementById('chat-box');

function appendMessage(sender, text) {
  const div = document.createElement('div');
  div.classList.add('message', sender);
  div.textContent = (sender === 'user' ? 'You' : 'Bot') + ': ' + text;
  chatBox.appendChild(div);
  chatBox.scrollTop = chatBox.scrollHeight;
}

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const text = input.value.trim();
  if (!text) return;
  appendMessage('user', text);
  input.value = '';
  try {
    const res = await fetch('http://localhost:8000/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: text })
    });
    const data = await res.json();
    appendMessage('bot', data.reply);
  } catch (err) {
    appendMessage('bot', 'Sorry, something went wrong.');
  }
});
