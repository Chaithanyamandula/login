// script.js
const form = document.getElementById('loginForm');

form.addEventListener('submit', (event) => {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Replace with your actual authentication logic
    if (username === 'chaithu' && password === 'Chaithu@02') {
        // Redirect to the dashboard or desired page
        window.location.href = 'https://github.com/Chaithanyamandula';
    } else {
        alert('Invalid username or password');
    }
});