// Replace YOUR_API_KEY with your OpenWeatherMap API key
const API_KEY = "4c3b28f185e65bcdb29a65789ef5d49e";

// Get the user's current location
navigator.geolocation.getCurrentPosition((position) => {
  const lat = position.coords.latitude;
  const lon = position.coords.longitude;

  // Make a request to the OpenWeatherMap API to get the weather data for the user's location
  fetch(`https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&units=metric&appid=${API_KEY}`)
    .then((response) => response.json())
    .then((data) => {
      // Display the weather information in the "weather-info" div
      
      const weatherInfoSimple = `
        ${data.main.temp}°C ${data.weather[0].description}
      `;
      
      document.getElementById("weather-info").innerHTML = weatherInfoSimple;
    })
    .catch((error) => console.log(error));
});


// collapsible list for class in degrees

var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}


function togglePageContentLightDark() {
  var body = document.getElementById('body')
  var currentClass = body.className
  var newClass = body.className == 'dark-mode' ? 'light-mode' : 'dark-mode'
  body.className = newClass

  // Save the theme preference for 10 years.
  var endDate = new Date();
  endDate.setFullYear(endDate.getFullYear() + 10);

  document.cookie = 'theme=' + (newClass == 'light-mode' ? 'light' : 'dark') +
                    '; Expires=' + endDate + ';'
  console.log('Cookies are now: ' + document.cookie)
}


function isDarkThemeSelected() {
  return document.cookie.match(/theme=dark/i) != null
}


function setThemeFromCookie() {
  var body = document.getElementById('body')
  body.className = isDarkThemeSelected() ? 'dark-mode' : 'light-mode'
}


(function() {
  setThemeFromCookie()
})();

function logoutAlert() {
  alert("You have beend logged out!");
}