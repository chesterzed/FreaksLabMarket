document.addEventListener('DOMContentLoaded', function() {
const filtersBtn = document.querySelector('.filters-btn');
const filtersContent = document.querySelector('.filters-content');
const filtersForm = document.getElementById('filters-form');
const resetBtn = document.getElementById('reset-btn');
const allCategoriesCheckbox = document.getElementById('all');
const categoryCheckboxes = document.querySelectorAll('input[name="category"]');
const priceBounds = document.querySelectorAll('input[class="price-input"]');

// Открытие/закрытие меню фильтров
filtersBtn.addEventListener('click', function(e) {
    e.stopPropagation();
    filtersContent.classList.toggle('show');
});

// Закрытие меню при клике вне его
document.addEventListener('click', function() {
    filtersContent.classList.remove('show');
});

// Предотвращение закрытия меню при клике внутри него
filtersContent.addEventListener('click', function(e) {
    e.stopPropagation();
});

// Обработка выбора "Все категории"
allCategoriesCheckbox.addEventListener('change', function() {
    if (this.checked) {
        categoryCheckboxes.forEach(checkbox => {
            checkbox.checked = true;
        });
    } else {
        categoryCheckboxes.forEach(checkbox => {
            checkbox.checked = false;
        });
    }
});

// Обработка выбора отдельных категорий
categoryCheckboxes.forEach(checkbox => {
    if (checkbox !== allCategoriesCheckbox) {
        checkbox.addEventListener('change', function() {
            if (!this.checked) {
                allCategoriesCheckbox.checked = false;
            } else {
                // Проверяем, все ли категории выбраны
                const allChecked = Array.from(categoryCheckboxes)
                    .filter(cb => cb !== allCategoriesCheckbox)
                    .every(cb => cb.checked);

                if (allChecked) {
                    allCategoriesCheckbox.checked = true;
                }
            }
        });
    }
});

// Сброс фильтров
resetBtn.addEventListener('click', function() {
    filtersForm.reset();

    categoryCheckboxes.forEach(checkbox => {
        checkbox.checked = false;
    });
    priceBounds.forEach(textarea => {
        textarea.value = "";
    });
});

// Применение фильтров
// filtersForm.addEventListener('submit', function(e) {
//     e.preventDefault();
//
//     // Сбор данных формы
//     const formData = new FormData(filtersForm);
//     const selectedCategories = [];
//     const priceFrom = formData.get('price-from');
//     const priceTo = formData.get('price-to');
//
//     // Получение выбранных категорий
//     categoryCheckboxes.forEach(checkbox => {
//         if (checkbox.checked && checkbox.value !== 'all') {
//             selectedCategories.push(checkbox.value);
//         }
//     });
//
//     // В реальном приложении здесь будет отправка данных на сервер
//     // или фильтрация элементов на странице
//
//     console.log('Выбранные категории:', selectedCategories);
//     console.log('Диапазон цен:', priceFrom, '-', priceTo);
//
//     // Закрытие меню после применения
//     filtersContent.classList.remove('show');
//
//     // Уведомление пользователя
//     // alert('Фильтры применены! Проверьте консоль для просмотра выбранных параметров.');
// });
});