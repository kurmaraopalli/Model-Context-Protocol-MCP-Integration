const form = document.getElementById('chat-form');
const input = document.getElementById('message');
const chat = document.getElementById('chat');
const suggestions = document.getElementById('suggestions');
const sessionId = `session-${Date.now()}`;

function addMessage(text, type) {
  const div = document.createElement('div');
  div.className = `message ${type}`;
  div.textContent = text;
  chat.appendChild(div);
}

function renderSuggestions(items) {
  suggestions.innerHTML = '';
  items.forEach((item) => {
    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'suggestion-btn';
    button.textContent = item;
    button.addEventListener('click', () => sendMessage(item));
    suggestions.appendChild(button);
  });
}

async function sendMessage(message) {
  if (!message) return;

  addMessage(message, 'user');
  input.value = '';

  try {
    const response = await fetch('/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message, session_id: sessionId })
    });

    const data = await response.json();
    addMessage(data.reply, 'bot');
    renderSuggestions(data.suggestions || []);
  } catch (error) {
    addMessage('The chat backend is not reachable. The page still works as a static demo.', 'bot');
    renderSuggestions(['Try again later', 'Open the local FastAPI server']);
  }
}

form.addEventListener('submit', async (event) => {
  event.preventDefault();
  const message = input.value.trim();
  if (!message) return;
  await sendMessage(message);
});

window.addEventListener('DOMContentLoaded', () => {
  addMessage('Hello! I can help with UX guidance for checkout, support, or FAQ.', 'bot');
  renderSuggestions([
    'What does this bot do?',
    'How do I use the checkout guidance?',
    'What are the main UX principles here?'
  ]);
});
