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

// Javascript to manipulate edit posts

document.addEventListener('DOMContentLoaded', () => {
    const editButtons = document.getElementsByClassName('btn-edit');
    const reviewText = document.getElementById('id_review_content');
    const reviewForm = document.getElementById('reviewForm');
    const submitButton = document.getElementById('submitButton');

    for (let button of editButtons) {
        button.addEventListener('click', (e) => {
            const reviewId = e.target.getAttribute('data-comment-id');
            const reviewTitle = e.target.closest('.card').querySelector('li:first-child').innerText.split(': ')[1];
            const reviewContent = e.target.closest('.card').querySelector('li:nth-child(2)').innerText.split(': ')[1];
            const reviewRating = e.target.closest('.card').querySelector('li:nth-child(4)').innerText.split(' / out of 5')[0].trim();

            reviewText.value = reviewContent;
            reviewForm.querySelector('input[name="review_title"]').value = reviewTitle;
            reviewForm.querySelector('textarea[name="review_content"]').value = reviewContent;
            
            const ratingInput = reviewForm.querySelector('input[name="rating"]');
            if (ratingInput) {
                ratingInput.value = reviewRating;
            }
            submitButton.innerText = 'Update';
            // if this is set to commentId I get a NEW review. if it is set to reviewId you get a url error when posting. 
            reviewForm.setAttribute('action', `/edit_review/${commentId}/`);
        });
    }
});

// Easter Egg Quote
console.log(" 'Six pints of bitter,' said Ford Prefect, 'and quickly please, the world's about to end.' - Douglas Adams HHGTTG");

