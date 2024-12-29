// Прокрутка вверх при переключении
document.addEventListener('DOMContentLoaded', () => {
    const letterNavButtons = document.querySelectorAll('.letter-nav');
    const poemNavButtons = document.querySelectorAll('.poem-nav'); // Для стихов, если такие кнопки есть

    // Функция для прокрутки вверх
    const scrollToTop = () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    };

    // Добавляем обработчик для писем
    letterNavButtons.forEach(button => {
        button.addEventListener('click', scrollToTop);
    });

    // Добавляем обработчик для стихов (если есть кнопки навигации)
    poemNavButtons.forEach(button => {
        button.addEventListener('click', scrollToTop);
    });
});