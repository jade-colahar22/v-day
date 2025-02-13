document.addEventListener('DOMContentLoaded', () => {
    const nextPageButton = document.querySelector('.next-page');  // Button with the 'Next' class
    const loveDiv = document.getElementById('love');  // The "love" entrance animation
    const hiddenContent = document.getElementById('hidden-content');  // The hidden content to show after clicking "Next"
    const music = document.getElementById('background-music');  // Access the audio element
  
    // Function to show hidden content, hide entrance content, and change background color
    function showHiddenContent() {
      loveDiv.style.display = 'none';  // Hides the entrance animation
      nextPageButton.style.display = 'none';  // Hides the "Next" button
      hiddenContent.style.display = 'block';  // Makes the hidden content visible
      document.body.style.backgroundColor = "rgba(255, 182, 193, 0.5)";  // Soft pink with 50% opacity
      music.play();  // Plays the music when the button is clicked or Enter key is pressed
    }
  
    // Event listener for the "Next" button click
    if (nextPageButton) {
      nextPageButton.addEventListener('click', showHiddenContent);
    }
  
    // Event listener for the "Enter" key press
    document.addEventListener('keydown', function (event) {
      if (event.key === 'Enter') {  // Check if the "Enter" key is pressed
        showHiddenContent();
      }
    });
});
