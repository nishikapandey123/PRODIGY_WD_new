const apiKey = '55f54b9a1c7b5a1e67e3cbc39c23fbac';
const baseUrl = 'https://api.openweathermap.org/data/2.5/weather';

document.addEventListener('DOMContentLoaded', () => {
  const locationInput = document.getElementById('locationInput');
  const submitButton = document.getElementById('submitButton');

  submitButton.addEventListener('click', async () => {
    const location = locationInput.value;

    // Fetch weather data using user-inputted location
    try {
      const response = await fetch(`${baseUrl}?q=${location}&appid=${apiKey}&units=metric`);
      const data = await response.json();

      // Display weather data
      displayWeatherData(data);
    } catch (error) {
      console.error('Error fetching weather data:', error);
    }
  });

  if ("geolocation" in navigator) {
    navigator.geolocation.getCurrentPosition(async position => {
      const latitude = position.coords.latitude;
      const longitude = position.coords.longitude;

      // Fetch weather data using latitude and longitude
      try {
        const response = await fetch(`${baseUrl}?lat=${latitude}&lon=${longitude}&appid=${apiKey}&units=metric`);
        const data = await response.json();

        // Display weather data
        displayWeatherData(data);
      } catch (error) {
        console.error('Error fetching weather data:', error);
      }
    });
  } else {
    console.error('Geolocation is not available');
  }
});

async function displayWeatherData(data) {
  const weatherInfo = document.querySelector('.weather-info');
  weatherInfo.innerHTML = `
    <h2>${data.name}, ${data.sys.country}</h2>
    <p>Temperature: ${data.main.temp}°C</p>
    <p>Weather: ${data.weather[0].main}</p>
    <p>Description: ${data.weather[0].description}</p>
  `;
}
