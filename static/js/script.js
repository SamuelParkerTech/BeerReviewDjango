// JavaScript calls a Age Verification Modal
document.addEventListener('DOMContentLoaded', function () {
    var myModal = new bootstrap.Modal(document.getElementById('staticBackdrop'));
    myModal.show();
});

// JavaScript for handling button clicks
document.getElementById('noButton').addEventListener('click', function () {
    window.location.href = 'https://www.google.co.uk';
});



console.log("Don't Panic!");
