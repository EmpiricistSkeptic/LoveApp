// Функция для отображения вопросов по выбранной категории
function toggleQuestions(categoryId) {
    // Скрыть все категории
    const allCategories = document.querySelectorAll('.questions-category');
    allCategories.forEach(category => {
        category.style.display = 'none';
    });

    // Показать выбранную категорию
    const selectedCategory = document.getElementById(categoryId);
    selectedCategory.style.display = 'block';
}
