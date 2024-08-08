// JavaScript calls a Age Verification Modal

// Function to get a cookie by name
function getCookie(name) {
    let cookieArr = document.cookie.split(";");
    
    for(let i = 0; i < cookieArr.length; i++) {
        let cookiePair = cookieArr[i].split("=");
        
        if(name == cookiePair[0].trim()) {
            return decodeURIComponent(cookiePair[1]);
        }
    }
    
    return null;
}

// Function to set a cookie
function setCookie(name, value, days) {
    let date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
    let expires = "expires=" + date.toUTCString();
    document.cookie = name + "=" + encodeURIComponent(value) + ";" + expires + ";path=/";
}

// Check if the 'ageVerified' cookie exists
document.addEventListener('DOMContentLoaded', function () {
    if (!getCookie('ageVerified')) {
        var myModal = new bootstrap.Modal(document.getElementById('staticBackdrop'));
        myModal.show();
    }

    // Set cookie when the 'Yes' button is clicked
    document.getElementById('yesButton').addEventListener('click', function () {
        setCookie('ageVerified', 'true', 30); // Set cookie for 30 days
    });

    // Redirect when the 'No' button is clicked
    document.getElementById('noButton').addEventListener('click', function () {
        window.location.href = 'https://www.google.co.uk';
    });
});

// Easter Egg Quote
console.log(" 'Six pints of bitter,' said Ford Prefect, 'and quickly please, the world's about to end.' - Douglas Adams HHGTTG");

