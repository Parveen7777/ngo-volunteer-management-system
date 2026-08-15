// Confirm delete action
function confirmDelete(message = 'Are you sure you want to delete this record?') {
    return confirm(message);
}

// Show current date and time
function showDateTime() {
    const element = document.getElementById('datetime');
    if (element) {
        const now = new Date();
        element.innerHTML = now.toLocaleString();
    }
}

setInterval(showDateTime, 1000);

// Simple search filter
function searchTable(inputId, tableId) {
    const input = document.getElementById(inputId);
    const filter = input.value.toUpperCase();
    const table = document.getElementById(tableId);
    const rows = table.getElementsByTagName('tr');

    for (let i = 1; i < rows.length; i++) {
        const cells = rows[i].getElementsByTagName('td');
        let found = false;

        for (let j = 0; j < cells.length; j++) {
            if (cells[j].innerHTML.toUpperCase().indexOf(filter) > -1) {
                found = true;
                break;
            }
        }

        rows[i].style.display = found ? '' : 'none';
    }
}

// Form validation
function validateVolunteerForm() {
    const name = document.getElementById('name');
    const email = document.getElementById('email');

    if (name && name.value.trim() === '') {
        alert('Name is required');
        return false;
    }

    if (email && email.value.trim() === '') {
        alert('Email is required');
        return false;
    }

    return true;
}

document.addEventListener('DOMContentLoaded', function () {
    showDateTime();
});
