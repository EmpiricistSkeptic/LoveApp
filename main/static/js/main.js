document.addEventListener("DOMContentLoaded", () => {
    const starContainer = document.querySelector('.falling-stars');

    function createStar() {
        const star = document.createElement('div');
        star.classList.add('star');

        // Случайная начальная позиция и угол
        const startX = Math.random() * 100; // Начало по горизонтали
        const endX = Math.random() - 0.5; // Сдвиг по горизонтали
        const duration = Math.random() * 3 + 2; // Длительность падения (2–5 сек)

        // Установка переменных CSS
        star.style.left = `${startX}vw`;
        star.style.setProperty('--end-x', endX); // Используем кастомную переменную CSS
        star.style.animationDuration = `${duration}s`;

        // Удаление звезды после завершения анимации
        star.addEventListener("animationend", () => {
            star.remove();
        });

        // Добавление звезды в контейнер
        starContainer.appendChild(star);
    }

    // Запускаем генерацию звезд
    setInterval(createStar, 800); // Интервал появления новых звезд
});