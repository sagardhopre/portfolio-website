// JavaScript for interactive portfolio features

// Function to show current date and time
function displayDateTime() {
    const now = new Date();
    const options = {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
        timeZone: 'UTC'
    };
    const dateTime = now.toLocaleString('en-GB', options);
    document.getElementById('dateTime').innerText = dateTime;
}

// Call the function on page load
window.onload = displayDateTime;

// Other interactive features can be added here...