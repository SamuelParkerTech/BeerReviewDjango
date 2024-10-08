/* global bootstrap */

// JavaScript calls Age Verification Modal

// Function to get a cookie by name
function getCookie(name) {
    let cookieArr = document.cookie.split(";");

    for (let i = 0; i < cookieArr.length; i++) {
        let cookiePair = cookieArr[i].split("=");

        if (name == cookiePair[0].trim()) {
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

    if (getCookie('ageVerified')) {
        // If the ageVerified cookie exists, do nothing and exit the script
        return;
    }

    // If the cookie does not exist, proceed with showing the modal
    var myModal = new bootstrap.Modal(document.getElementById('staticBackdrop'));
    myModal.show();

    // Set cookie when the 'Yes' button is clicked
    document.getElementById('yesButton').addEventListener('click', function () {
        setCookie('ageVerified', 'true', 30); // Set cookie for 30 days
    });

    // Redirect when the 'No' button is clicked
    document.getElementById('noButton').addEventListener('click', function () {
        window.location.href = 'https://www.google.co.uk';
    });
});

// JavaScript to edit reviews UPDATE

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
            const reviewRating = e.target.closest('.card').querySelector('.rating-display').getAttribute('data-raw-rating');

            reviewText.value = reviewContent;
            reviewForm.querySelector('input[name="review_title"]').value = reviewTitle;
            reviewForm.querySelector('textarea[name="review_content"]').value = reviewContent;

            const ratingSelect = reviewForm.querySelector('select[name="rating"]');
            if (ratingSelect) {
                // Ensure the rating is set properly
                console.log('Original review rating:', reviewRating);
                
                // Convert rating to number if needed and set the value
                ratingSelect.value = parseInt(reviewRating);  // Assuming reviewRating is a string, convert to number
                console.log('Setting rating select value:', ratingSelect.value);
            } else {
                console.error('Rating select not found');
            }

            submitButton.innerText = 'Update';
            reviewForm.setAttribute('action', `edit_review/${reviewId}`);
        });
    }
});




// Javascript to Delete reviews

document.addEventListener('DOMContentLoaded', () => {
    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    const deleteButtons = document.getElementsByClassName("btn-delete");
    const deleteConfirm = document.getElementById("deleteConfirm");

    for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
            let reviewId = e.target.getAttribute("data-comment-id");
            deleteConfirm.href = `delete_review/${reviewId}`;
            deleteModal.show();
        });
    }
});

// Easter Egg Quote
console.log(" 'Six pints of bitter,' said Ford Prefect, 'and quickly please, the world's about to end.' - Douglas Adams HHGTTG");

