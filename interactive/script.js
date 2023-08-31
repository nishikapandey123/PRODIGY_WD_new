window.addEventListener('scroll', function () {
    const navigation = document.querySelector('.navigation');
    if (window.scrollY > 0) {
        navigation.style.backgroundColor = '#222';
    } else {
        navigation.style.backgroundColor = '#333';
    }
});
